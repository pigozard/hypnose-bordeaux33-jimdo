# Guide de migration — Ce soir (Benoît en ligne demain matin)

**Site :** Benoît Raffard — Hypnothérapeute Bordeaux
**Contexte :** site Jimdo Creator existant, thème Rio de Janeiro actif, migration live
**Durée estimée :** 2h30 à 3h | **Confiance :** ~88%

---

## Vue d'ensemble des 3 phases

| Phase | Durée | Visible par les visiteurs ? |
|---|---|---|
| **0 — Préparation** | ~35 min | Non — travail offline |
| **1 — CSS** | ~10 min | Oui — fond et polices changent |
| **2 — Pages** (5 pages) | ~1h40 | Oui — page par page |
| **3 — Vérifications** | ~15 min | Non |

> **Règle d'or :** toute sauvegarde dans Jimdo est immédiatement live. Prépare tout en Phase 0 avant de toucher quoi que ce soit sur le site.

---

## Phase 0 — Préparation (offline, ~35 min)

### 0A — Ouvrir les bons outils

Avoir en parallèle :
- **Éditeur de texte** : les 5 fichiers `.md` du dossier `07-migration-jimdo-creator/`
- **Navigateur** : le site Jimdo en mode édition, + F12 ouvert
- **Dossier images** : `images/` à la racine du projet

---

### 0B — Uploader les images dans Jimdo (20 min)

Dans Jimdo Creator : **Médiathèque → Uploader**

Uploader ces 8 fichiers dans l'ordre. Pour chaque image, une fois uploadée, cliquer dessus et copier l'URL complète qu'elle fournit.

| Fichier local | Placeholder à remplacer | URL Jimdo |
|---|---|---|
| `images/logo-br.png` | `[IMG:logo]` | ________________ |
| `images/portrait.png` | `[IMG:portrait]` | ________________ |
| `images/facade-1.png` | `[IMG:facade-1]` | ________________ |
| `images/facade-2.png` | `[IMG:facade-2]` | ________________ |
| `images/cabinet-1.png` | `[IMG:cabinet-1]` | ________________ |
| `images/cabinet-3.png` | `[IMG:cabinet-3]` | ________________ |
| `images/cabinet-5.png` | `[IMG:cabinet-5]` | ________________ |
| `images/cabinet-6.png` | `[IMG:cabinet-6]` | ________________ |

---

### 0C — Remplacer les placeholders dans les fichiers (10 min)

Dans chaque fichier `01-accueil.md` à `05-contact-tarifs.md` :

1. **Chercher/remplacer** chaque `[IMG:xxx]` par l'URL Jimdo notée ci-dessus
2. Le plus rapide : ouvrir chaque fichier dans VS Code, `Cmd+H` (Mac) ou `Ctrl+H` (PC), chercher `[IMG:logo]`, remplacer par l'URL

> Faire ça sur les 5 fichiers avant de passer à la suite. Le code sera ainsi prêt à coller directement.

---

### 0D — Identifier les sélecteurs du thème Rio de Janeiro (5 min)

Cette étape permet d'écrire le CSS qui masquera le thème existant.

1. Ouvrir le site en mode **visite normale** (pas édition) dans Chrome/Firefox
2. **F12** → outil de sélection (icône carré+curseur, en haut à gauche de DevTools)
3. Cliquer sur chaque zone et noter le **nom de classe principal** affiché dans l'onglet Elements :

| Zone à inspecter | Classe trouvée |
|---|---|
| Le bandeau image en haut (stage Rio) | `._______` |
| La barre de navigation du thème | `._______` |
| Le footer du thème | `._______` |

Ces sélecteurs serviront si les overrides CSS de la Phase 1 ne cachent pas entièrement le thème. Dans ce cas, ajouter une ligne `{ display: none !important; }` pour chaque sélecteur manquant.

---

## Phase 1 — CSS global (~10 min)

> Cette phase change l'apparence globale immédiatement. Le fond devient beige, les polices changent, le header Rio de Janeiro disparaît.

### 1A — Sauvegarder l'ancien CSS

Dans Jimdo : **Design → Personnaliser → CSS**
Copier tout le CSS existant, le coller dans un fichier texte en local (au cas où).

---

### 1B — Coller le nouveau CSS

1. **Tout sélectionner** dans l'éditeur CSS de Jimdo (`Ctrl+A` ou `Cmd+A`)
2. **Supprimer**
3. **Ouvrir** `07-migration-jimdo-creator/jimdo-custom.css`
4. **Tout copier** (`Ctrl+A` puis `Ctrl+C`)
5. **Coller** dans l'éditeur Jimdo
6. **Enregistrer**

---

### 1C — Vérifier

Ouvrir le site (mode visite) et vérifier :

- [ ] Fond beige clair (`#FAF7F2`) sur toutes les pages
- [ ] Police changée (plus fine, plus élégante = Cormorant Garamond)
- [ ] Bandeau image Rio de Janeiro disparu
- [ ] Barre de navigation Jimdo disparue
- [ ] Footer Jimdo disparu
- [ ] Contenu existant des pages encore visible (même avec style transitoire)

**Si un élément Rio de Janeiro est encore visible :**
→ F12 → noter sa classe → ajouter à la fin du CSS Jimdo :
```css
.NOM-DE-CLASSE-TROUVE { display: none !important; }
```

**Si Google Fonts ne se charge pas** (texte en Arial/system) :
→ Ajouter ce `<link>` comme première ligne dans le Widget 0 (nav) de n'importe quelle page :
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">
```

---

## Phase 2 — Migration page par page (~1h40)

### Méthode commune à toutes les pages

Pour chaque page :
1. Ouvrir la page dans Jimdo en **mode édition** (`Éditer`)
2. **Supprimer tous les widgets existants** (cliquer sur chaque widget → corbeille)
3. Cliquer sur **"+"** pour ajouter → choisir **"Élément HTML"**
4. Coller le snippet du Widget → **Enregistrer**
5. Répéter pour chaque widget dans l'ordre

> Tip : avoir le fichier `.md` ouvert dans l'éditeur, widgets numérotés dans l'ordre. Aller vite, la page est live dès l'enregistrement.

---

### Page 1 — À propos (~20 min)

**Fichier :** `04-a-propos.md`
**URL Jimdo :** `/a-propos`

| # | Widget | Contenu |
|---|---|---|
| 0 | Navigation | Nav avec lien `/a-propos` en `class="active"` |
| 1 | Présentation | Photo + biographie + badges + citation |
| 2 | Interventions & congrès | 7 événements 2019–2023 |
| 3 | Réseau pluridisciplinaire | Grille 3 colonnes + note apnées + photo façade |
| 4 | Bande CTA | Section sombre avec bouton RDV |
| — | CTA mobile | `<div class="mobile-cta">` — visible uniquement sur mobile |
| 5 | Footer | Footer sombre identique sur toutes les pages |

---

### Page 2 — Contact & tarifs (~20 min)

**Fichier :** `05-contact-tarifs.md`
**URL Jimdo :** `/contact`

| # | Widget | Contenu |
|---|---|---|
| 0 | Navigation | Nav avec lien `/contact` en `class="active"` |
| 1 | En-tête de page | Titre + subtitle |
| 2 | Tarifs | Carte 80€ (featured) + carte tabac 240€ |
| 3 | Politique d'annulation | Texte + règle 24h |
| 4 | Contact + Google Maps | Coordonnées + iframe carte |
| 5 | Mentions légales | Section avec `id="mentions-legales"` |
| 6 | Bande CTA | Section sombre avec bouton RDV |
| — | CTA mobile | `<div class="mobile-cta">` |
| 7 | Footer | Footer standard |

---

### Page 3 — L'hypnose (~25 min)

**Fichier :** `02-hypnose.md`
**URL Jimdo :** `/hypnose`

| # | Widget | Contenu |
|---|---|---|
| 0 | Navigation | Nav avec lien `/hypnose` en `class="active"` |
| 1 | En-tête de page | Titre + subtitle |
| 2 | Introduction | Texte descriptif |
| 3 | Bande photos cabinet | Photos avec `[IMG:cabinet-x]` |
| 4 | Indications | 12 cartes "Pour qui ?" |
| 5 | Traumatismes | Section spécifique |
| 6 | FAQ | Accordéon avec script JS inclus |
| 7 | Bande CTA | Section sombre |
| — | CTA mobile | `<div class="mobile-cta">` |
| 8 | Footer | Footer standard |

> **Important :** le Widget 6 (FAQ) contient un `<script>` pour l'accordéon. Le coller en entier, script inclus.

---

### Page 4 — Troubles du sommeil (~20 min)

**Fichier :** `03-apnee-sommeil.md`
**URL Jimdo :** `/troubles-du-sommeil`

| # | Widget | Contenu |
|---|---|---|
| 0 | Navigation | Nav avec lien `/troubles-du-sommeil` en `class="active"` |
| 1 | Hero apnées | Stats 37% / 1-2 séances / 2019 |
| 2 | Le masque pose problème | Explication |
| 3 | Les freins à l'observance | 6 cartes raisons |
| 4 | Le protocole | 4 étapes |
| 5 | Partenaires médicaux | Section partenaires |
| 6 | Congrès | Dates + lieux |
| 7 | Bande CTA | Section sombre |
| — | CTA mobile | `<div class="mobile-cta">` |
| 8 | Footer | Footer standard |

---

### Page 5 — Accueil (en dernier, ~25 min)

**Fichier :** `01-accueil.md`
**URL Jimdo :** `/` (page d'accueil)

| # | Widget | Contenu |
|---|---|---|
| 0 | Navigation | Nav avec lien `/` en `class="active"` |
| 1 | Hero | Portrait + badge + 2 CTA + 3 trust items |
| 2 | Bande photos | 4 photos cabinet |
| 3 | Indications | 4 cartes "Pour qui ?" |
| 4 | Teaser apnées | Section sombre (brun) avec stats |
| 5 | 3 étapes | Process visuel |
| 6 | Témoignages | 4 cartes témoignages |
| 7 | Bande CTA | Section sombre finale |
| — | CTA mobile | `<div class="mobile-cta">` |
| 8 | Footer | Footer standard |

---

## Phase 3 — Vérifications finales (~15 min)

Ouvrir chaque page en mode visite normale et cocher :

### Navigation
- [ ] La nav reste collée en haut lors du scroll (sticky)
- [ ] Le lien actif est bien mis en évidence sur chaque page
- [ ] Le bouton "Prendre RDV" ouvre crenolibre.fr dans un nouvel onglet
- [ ] Le hamburger mobile s'ouvre et se ferme correctement
- [ ] Les liens de la nav pointent vers les bons slugs Jimdo

### Contenu
- [ ] Les 8 images s'affichent (pas de cadre vide ou d'icône cassée)
- [ ] FAQ (page Hypnose) : l'accordéon s'ouvre/ferme au clic
- [ ] Google Maps (page Contact) : la carte s'affiche
- [ ] Téléphone `tel:0619185999` : déclenche l'appel sur mobile
- [ ] Lien Mentions légales → `/contact#mentions-legales` fonctionne

### Mobile (redimensionner la fenêtre à < 768px)
- [ ] Le hamburger remplace les liens de navigation
- [ ] La barre "Prendre rendez-vous" apparaît en bas de l'écran
- [ ] Les sections s'empilent correctement (pas de débordement horizontal)
- [ ] Les textes sont lisibles (pas trop petits)

### Visuel global
- [ ] Fond beige `#FAF7F2` partout
- [ ] Polices Cormorant Garamond (titres) et DM Sans (textes)
- [ ] Bandeau Rio de Janeiro complètement masqué
- [ ] Footer natif Jimdo complètement masqué

---

## Troubleshooting — 4 problèmes courants

### Problème 1 : La nav n'est pas sticky (elle défile avec la page)

**Diagnostic :** Jimdo a un container avec `overflow: hidden` qui bloque sticky.

**Fix :** Dans Design → CSS, chercher `#nav` et remplacer par :
```css
#nav {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  z-index: 9999 !important;
}
/* Puis ajouter sur le container du contenu principal pour éviter le chevauchement : */
.j-content, .cc-content { padding-top: 72px !important; }
```

---

### Problème 2 : Un élément du thème Rio de Janeiro est encore visible

**Diagnostic :** notre liste de sélecteurs CSS ne couvre pas le sélecteur exact utilisé par ce thème.

**Fix :**
1. F12 → sélectionner l'élément visible
2. Copier sa classe (ex: `.j-stage--rio`, `.cc-masthead-overlay`, etc.)
3. Dans Design → CSS, ajouter à la fin :
```css
.NOM-DE-CLASSE-EXACT { display: none !important; }
```

---

### Problème 3 : La nav n'est pas full-width (elle est centrée ou plus étroite)

**Diagnostic :** le wrapper Jimdo autour du widget HTML a une `max-width` contrainte.

**Fix :** Dans Design → CSS, décommenter ces 2 lignes dans le bloc `#nav` :
```css
#nav {
  /* ... autres propriétés ... */
  width: 100vw !important;
  margin-left: calc(50% - 50vw) !important;
}
```

---

### Problème 4 : Les images n'apparaissent pas

**Diagnostic :** l'URL Jimdo dans le code HTML n'est pas correcte, ou l'image n'a pas été uploadée.

**Fix :**
1. Vérifier dans la Médiathèque Jimdo que l'image existe
2. Cliquer sur l'image → copier l'URL exacte
3. Ouvrir le widget HTML de la page → remplacer `src="..."` par la bonne URL
4. Enregistrer


LIENS DES IMAGES

[IMG:logo] -> https://image.jimcdn.com/app/cms/image/transf/none/path/s05b5a39f7afee65f/image/i64eb8329cd8ca10a/version/1783376574/image.png
[IMG:portrait] -> https://image.jimcdn.com/app/cms/image/transf/none/path/s05b5a39f7afee65f/image/i5a8f69d85ac00634/version/1783376588/image.png
[IMG:facade-1] -> https://image.jimcdn.com/app/cms/image/transf/none/path/s05b5a39f7afee65f/image/i6380f66241e92016/version/1783376547/image.jpg
[IMG:facade-2] -> https://image.jimcdn.com/app/cms/image/transf/none/path/s05b5a39f7afee65f/image/i4d33fc3fb8bf84c5/version/1783376560/image.jpg
[IMG:cabinet-1] -> https://image.jimcdn.com/app/cms/image/transf/none/path/s05b5a39f7afee65f/image/i60dd9e0c810a6b56/version/1783376625/image.jpg
[IMG:cabinet-3] -> https://image.jimcdn.com/app/cms/image/transf/none/path/s05b5a39f7afee65f/image/i13ef10392be3f5e9/version/1783376508/image.jpg
[IMG:cabinet-5] -> https://image.jimcdn.com/app/cms/image/transf/none/path/s05b5a39f7afee65f/image/i91bf794463f24f2b/version/1783376521/image.jpg
[IMG:cabinet-6] -> https://image.jimcdn.com/app/cms/image/transf/none/path/s05b5a39f7afee65f/image/i78b5af14837728fa/version/1783376534/image.jpg

---

## Correspondance des slugs

| Lien dans le HTML | Slug Jimdo à configurer |
|---|---|
| `href="/"` | Page d'accueil |
| `href="/hypnose"` | URL de la page L'hypnose |
| `href="/troubles-du-sommeil"` | URL de la page Troubles du sommeil |
| `href="/a-propos"` | URL de la page À propos |
| `href="/contact"` | URL de la page Contact & tarifs |

> Vérifier dans Jimdo que les slugs de chaque page correspondent exactement. Jimdo Creator → mode édition de la page → Paramètres (icône engrenage) → URL de la page.

---

## Données de référence

| Donnée | Valeur |
|---|---|
| Adresse | 28 rue Scaliger, 33000 Bordeaux |
| Téléphone | 06 19 18 59 99 |
| Email | benoithypnose33@gmail.com |
| SIRET | 834 833 641 |
| Lien RDV | https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33 |
| Google Maps embed | https://maps.google.com/maps?q=28+rue+Scaliger,+33000+Bordeaux&output=embed |

---

## Checklist finale avant d'aller dormir

- [ ] Les 5 pages affichent la nav custom (pas le thème Rio)
- [ ] Toutes les images s'affichent sur toutes les pages
- [ ] La page d'accueil est la dernière à avoir été migrée
- [ ] Aucun `[IMG:xxx]` résiduel dans le code (faire une recherche rapide dans DevTools → Ctrl+F dans le code source)
- [ ] Mobile : vérifier rapidement sur son propre téléphone

---

*Guide finalisé le 2026-06-26 — bonne migration !*
