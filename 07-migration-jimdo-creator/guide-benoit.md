# Guide — Gérer son site seul (hypnose-bordeaux33.com)

## Les 3 règles d'or

1. **Ne jamais toucher au CSS** (Design → Personnaliser → Design perso CSS), sauf si ce guide te le dit explicitement. C'est ce qui fait tenir tout le design (couleurs, mise en page, mobile). Une seule ligne cassée peut faire planter l'affichage de tout le site.

2. **Chaque page a des blocs "Widget / HTML"** — c'est là qu'est tout le contenu (textes, images, boutons). Modifier le texte à l'intérieur d'un widget est sans risque. Supprimer ou déplacer un widget peut casser la mise en page.

3. **Ne jamais ajouter de contenu dans la colonne étroite à gauche** de l'éditeur, ni juste après le dernier bloc en bas de page (avant le pied de page). Ces deux zones sont partagées par TOUTES les pages du site — tout ce qu'on y met apparaît sur les 5 pages en même temps, et supprimer un élément là-bas le supprime partout.

## Modifier un texte

1. Ouvre la page en mode édition
2. Clique sur le bloc de texte à modifier
3. Un code apparaît (ça ressemble à du HTML) — repère le texte en français au milieu des balises `<...>`, modifie-le sans toucher aux balises autour
4. Enregistre

## Ajouter/changer une image

1. Ouvre le widget qui contient l'image (`<img src="...">`)
2. Ne touche pas à l'`src=` toi-même — demande à quelqu'un de compétent, ou :
   - Uploade la nouvelle image via un widget "Image" classique ailleurs (page brouillon non publiée par exemple)
   - Clique sur l'image une fois en ligne → clic droit → "Copier l'adresse de l'image"
   - Reviens dans le widget HTML, remplace l'ancienne URL entre les guillemets de `src="..."` par la nouvelle

## Ce qui NE FAUT PAS faire seul (demander de l'aide)

- Modifier le CSS
- Ajouter une nouvelle page avec navigation (les liens du menu doivent être mis à jour partout, sur les 5 pages)
- Toucher au bloc "Modifier le head" (Paramètres avancés)
- Réactiver le toggle "Version mobile" (Design → Version mobile) — il casse l'affichage actuel s'il est activé

## Pourquoi le site a cette structure (pour comprendre, pas à modifier)

Ces 3 lignes de CSS masquent l'ancien thème Jimdo par défaut ("Rio de Janeiro") pour ne garder que le nouveau design :
```css
#header { display: none !important; }
[data-container="navigation"] { display: none !important; }
#footer { display: none !important; }
```
Si un jour le menu du haut ou le pied de page d'origine Jimdo réapparaît bizarrement, c'est probablement que ces lignes ont été supprimées par erreur — il suffit de les remettre.

## En cas de problème

- Si une page affiche n'importe quoi après une modif : annule (bouton "Annuler" avant d'enregistrer si possible), ou contacte-moi
- Ne jamais paniquer : rien n'est perdu tant qu'on n'a pas supprimé le CSS en entier
