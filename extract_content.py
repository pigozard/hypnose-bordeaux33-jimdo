"""
Extraction des contenus des pages Jimdo aspirees vers Markdown.
Parcourt 00-backups/wget-2026-04-27/ et genere un .md par page dans 06-contenus/.
"""

from bs4 import BeautifulSoup
from pathlib import Path
import re

# Chemins
BACKUP_DIR = Path("00-backups/wget-2026-04-27")
OUTPUT_DIR = Path("06-contenus")
OUTPUT_DIR.mkdir(exist_ok=True)


def clean_text(text):
    """Nettoie les espaces multiples et les sauts de ligne excessifs."""
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    return text.strip()


def extract_page(html_file):
    """Extrait le contenu utile d'une page HTML Jimdo."""
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')

    # Title et meta description
    title = soup.find('title')
    title_text = title.get_text(strip=True) if title else "(sans titre)"

    meta_desc = soup.find('meta', attrs={'name': 'description'})
    desc_text = meta_desc.get('content', '') if meta_desc else ''

    # Le contenu principal Jimdo est dans #content ou main
    content_zone = (
        soup.find('div', id='content')
        or soup.find('main')
        or soup.find('div', class_=re.compile(r'content', re.I))
        or soup.body
    )

    # Supprimer les zones non pertinentes
    for tag in content_zone.find_all(['script', 'style', 'nav', 'footer', 'header', 'noscript']):
        tag.decompose()

    # Extraire les Hn et le texte structure
    output_lines = []
    output_lines.append(f"# {title_text}\n")
    if desc_text:
        output_lines.append(f"> **Meta description** : {desc_text}\n")

    for elem in content_zone.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li', 'a']):
        text = elem.get_text(strip=True)
        if not text or len(text) < 2:
            continue

        if elem.name == 'h1':
            output_lines.append(f"\n## H1 : {text}")
        elif elem.name == 'h2':
            output_lines.append(f"\n### H2 : {text}")
        elif elem.name == 'h3':
            output_lines.append(f"\n#### H3 : {text}")
        elif elem.name == 'h4':
            output_lines.append(f"\n##### H4 : {text}")
        elif elem.name == 'p' and len(text) > 15:
            output_lines.append(f"\n{text}")
        elif elem.name == 'li' and len(text) > 5:
            output_lines.append(f"- {text}")
        elif elem.name == 'a' and elem.get('href', '').startswith('http'):
            href = elem.get('href')
            if 'crenolibre' in href or 'jimdo' not in href.lower():
                output_lines.append(f"\n**Lien externe** : [{text}]({href})")

    # Liste des images (utile pour audit alt)
    images = content_zone.find_all('img')
    if images:
        output_lines.append("\n\n---\n\n### Images sur cette page\n")
        for img in images:
            src = img.get('src', '(sans src)')
            alt = img.get('alt', '(SANS ALT)')
            output_lines.append(f"- `{src}` -- alt : {alt}")

    return clean_text('\n'.join(output_lines))


def main():
    # Parcourir tous les index.html du backup
    html_files = list(BACKUP_DIR.rglob("index.html"))
    # Ajouter aussi les .html à la racine (login.html par ex.)
    html_files += [f for f in BACKUP_DIR.glob("*.html") if f.name != "index.html"]

    print(f"Pages trouvees : {len(html_files)}")
    print()

    for html_file in html_files:
        # Nommer le fichier de sortie d'apres le dossier parent
        if html_file.name == "index.html":
            page_name = html_file.parent.name
        else:
            page_name = html_file.stem

        # Cas special : la home est dans le dossier www.hypnose-bordeaux33.com
        if page_name.startswith("www."):
            page_name = "00-home"

        # Nettoyer le nom (accents, etc.)
        safe_name = (page_name
                     .replace('é', 'e').replace('è', 'e').replace('ê', 'e')
                     .replace('à', 'a').replace('ç', 'c'))

        output_file = OUTPUT_DIR / f"{safe_name}.md"

        try:
            content = extract_page(html_file)
            output_file.write_text(content, encoding='utf-8')
            word_count = len(content.split())
            print(f"OK  {output_file.name}  ({word_count} mots)")
        except Exception as e:
            print(f"ERR {html_file}  -- {e}")

    print()
    print(f"Tous les contenus sont dans : {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
