# Guide de migration — Jimdo Creator

Site : **Benoît Raffard — Hypnothérapeute à Bordeaux**  
Objectif : reproduire à l'identique le site GitHub Pages dans Jimdo Creator.  
Date : 2026-06-26

---

## Vue d'ensemble de la stratégie

Jimdo Creator permet d'insérer du HTML brut via le widget **Élément HTML**. Chaque section de chaque page est collée dans un widget HTML séparé. Les styles (CSS) sont centralisés dans l'éditeur CSS de Jimdo.

| Étape | Action |
|---|---|
| 1 | Générer et coller le CSS global dans l'éditeur Jimdo |
| 2 | Uploader toutes les images dans la médiathèque Jimdo |
| 3 | Configurer la navigation (5 pages + bouton CTA) |
| 4 | Configurer le footer |
| 5 | Créer chaque page et y coller les widgets HTML |

---

## Étape 1 — CSS global

### Générer le fichier CSS

Dans le terminal, depuis la racine du projet :

```bash
cat css/style.css css/home.css css/hypnose.css css/apnee-sommeil.css css/a-propos.css css/contact.css > 07-migration-jimdo-creator/jimdo-custom.css
```

### Coller dans Jimdo

1. Dans Jimdo Creator : **Design → Personnaliser → CSS**
2. Copier **tout** le contenu de `jimdo-custom.css` (le `@import` Google Fonts et les variables `:root` sont déjà inclus en tête du fichier — ne pas les rajouter)
3. Coller dans l'éditeur CSS de Jimdo et enregistrer

> **Si `@import` est bloqué par Jimdo :** le premier widget HTML de chaque page (Widget 0 — Navigation) charge déjà les polices via une balise `<link>` — ajouter cette ligne dans le HTML du Widget 0, juste avant `<nav id="nav">` :
> ```html
> <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">
> ```

### Masquer le footer natif de Jimdo

Ajouter également dans le CSS :

```css
/* Masquer le footer natif Jimdo pour utiliser le footer HTML personnalisé */
.cc-footer { display: none !important; }
```

> Si le sélecteur `.cc-footer` ne fonctionne pas, utiliser l'inspecteur du navigateur (F12) pour identifier la classe exacte du footer Jimdo, puis remplacer.

---

## Étape 2 — Images

Uploader ces fichiers dans **Médiathèque Jimdo** (icône image → Ajouter des images) et noter l'URL fournie par Jimdo pour chacun.

| Fichier local | Description | Placeholder dans les snippets |
|---|---|---|
| `images/logo-br.png` | Logo Benoît Raffard | `[IMG:logo]` |
| `images/portrait.png` | Portrait Benoît | `[IMG:portrait]` |
| `images/facade-1.png` | Façade — vue entrée 1 | `[IMG:facade-1]` |
| `images/facade-2.png` | Façade — vue entrée 2 | `[IMG:facade-2]` |
| `images/cabinet-1.png` | Cabinet — fauteuils | `[IMG:cabinet-1]` |
| `images/cabinet-3.png` | Cabinet — vue 3 | `[IMG:cabinet-3]` |
| `images/cabinet-5.png` | Cabinet — espace consultation | `[IMG:cabinet-5]` |
| `images/cabinet-6.png` | Cabinet — salle d'attente | `[IMG:cabinet-6]` |

**Dans chaque snippet des pages, remplacer `[IMG:nom]` par l'URL Jimdo correspondante.**

---

## Étape 3 — Navigation

> **Stratégie :** la nav native Jimdo est masquée via le CSS override. La vraie nav (logo, liens, bouton CTA, menu mobile, scroll JS) est incluse comme **Widget 0** en tête de chaque page. C'est la seule façon d'avoir un rendu identique à l'original.

Dans Jimdo, éditer la navigation (cliquer dessus en mode édition) :

| # | Titre affiché | Slug / URL |
|---|---|---|
| 1 | Accueil | `/` |
| 2 | L'hypnose | `/hypnose` |
| 3 | Troubles du sommeil | `/troubles-du-sommeil` |
| 4 | À propos | `/a-propos` |
| 5 | Contact & tarifs | `/contact` |

**Bouton CTA :** ajouter un 6ème lien de navigation avec le titre `Prendre RDV` pointant vers l'URL externe :
```
https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33
```

Personnaliser l'apparence du bouton CTA dans le CSS :

```css
/* Bouton Prendre RDV dans la nav */
nav a[href*="crenolibre"] {
  background: #C17A5A !important;
  color: #fff !important;
  border-radius: 9px !important;
  padding: 8px 18px !important;
  font-weight: 600 !important;
}
nav a[href*="crenolibre"]:hover {
  background: #A8623F !important;
}
```

---

## Étape 4 — Footer

Le footer est reproduit via un widget HTML en dernier élément de chaque page (voir chaque fichier de page). Jimdo's footer natif est masqué via CSS (voir Étape 1).

Informations du footer :
- Adresse : 28 rue Scaliger, Bordeaux → lien Google Maps
- Tél : 06 19 18 59 99 → `tel:0619185999`
- Mentions légales → `/contact#mentions-legales`

---

## Étape 5 — Ordre de création des pages

Créer les 5 pages dans cet ordre, puis construire chaque page en suivant le fichier correspondant :

1. **Accueil** → `01-accueil.md`
2. **L'hypnose** (`/hypnose`) → `02-hypnose.md`
3. **Troubles du sommeil** (`/troubles-du-sommeil`) → `03-apnee-sommeil.md`
4. **À propos** (`/a-propos`) → `04-a-propos.md`
5. **Contact & tarifs** (`/contact`) → `05-contact-tarifs.md`

**Méthode pour chaque page :**
1. Créer la page dans Jimdo
2. Supprimer les éléments par défaut de Jimdo (texte, image placeholder)
3. Ajouter les widgets HTML **dans l'ordre numéroté** du fichier de la page
4. Coller le snippet HTML dans chaque widget
5. Remplacer tous les `[IMG:nom]` par les URLs Jimdo correspondantes

---

## Correspondance des liens internes

| Lien dans le HTML | Page Jimdo |
|---|---|
| `index.html` | `/` |
| `hypnose.html` | `/hypnose` |
| `apnee-sommeil.html` | `/troubles-du-sommeil` |
| `a-propos.html` | `/a-propos` |
| `contact.html` | `/contact` |
| `contact.html#mentions-legales` | `/contact#mentions-legales` |

---

## Données de référence globales

| Donnée | Valeur |
|---|---|
| Nom complet | Benoît Raffard |
| Activité | Hypnothérapeute |
| Adresse | 28 rue Scaliger, 33000 Bordeaux |
| Téléphone | 06 19 18 59 99 |
| Email | benoithypnose33@gmail.com |
| SIRET | 834 833 641 |
| Prise de RDV | https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33 |
| Google Maps | https://maps.google.com/?q=28+rue+Scaliger+33000+Bordeaux |

**Palette de couleurs :**

| Rôle | Valeur |
|---|---|
| Accent principal | `#C17A5A` (terre cuite) |
| Accent foncé | `#A8623F` |
| Fond accent | `#F5E8E0` |
| Or / étoiles | `#E8884E` |
| Fond page | `#FAF7F2` |
| Fond chaud | `#F0E8DF` |
| Texte principal | `#2C2825` |

---

*Kit généré le 2026-06-26*
