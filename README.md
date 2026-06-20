# hypnose-bordeaux33 — Refonte site web

Site vitrine de **Benoît Raffard**, hypnothérapeute à Bordeaux.  
Refonte complète à partir de l'ancien site Jimdo, hébergé sur **GitHub Pages**.

---

## Structure du projet

```
├── index.html              Accueil
├── hypnose.html            L'hypnose Ericksonienne
├── apnee-sommeil.html      Spécialité apnées du sommeil
├── a-propos.html           Parcours & réseau
├── contact.html            Contact, tarifs & mentions légales
│
├── css/
│   ├── style.css           Styles globaux (nav, footer, boutons, typographie…)
│   ├── home.css            Styles spécifiques à l'accueil
│   ├── hypnose.css         Styles spécifiques à la page hypnose
│   ├── apnee-sommeil.css   Styles spécifiques à la page apnées
│   ├── a-propos.css        Styles spécifiques à la page à propos
│   └── contact.css         Styles spécifiques à la page contact
│
├── js/
│   └── main.js             Nav scroll, menu mobile, accordéon FAQ
│
├── images/                 Photos du cabinet, portrait, logo, façade
│
├── 00-backups/             Sauvegarde wget du site Jimdo original (2026-04-27)
├── 04-design/              Maquettes validées, palette, logo original
└── 06-contenus/            Contenus source en Markdown par page
```

---

## Stack

- HTML5 / CSS3 / JavaScript vanilla — aucune dépendance
- Polices Google Fonts : **Cormorant Garamond** (titres) + **DM Sans** (corps)
- Hébergement : **GitHub Pages** (branche `main`)
- Prise de RDV : [Crenolibre](https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33)

---

## Palette

| Rôle | Valeur |
|------|--------|
| Accent principal | `#C17A5A` (terre cuite) |
| Accent foncé | `#A8623F` |
| Fond accent | `#F5E8E0` |
| Or / étoiles | `#E8884E` |
| Fond page | `#FAF7F2` |
| Fond chaud | `#F0E8DF` |
| Texte principal | `#2C2825` |

---

## Déploiement

Le site est servi directement depuis la racine de la branche `main`.  
Aucun build nécessaire — pousser sur `main` suffit à mettre en ligne.

```bash
git add .
git commit -m "..."
git push origin main
```

---

## Client

**Benoît Raffard** — Hypnothérapeute  
28 rue Scaliger, 33000 Bordeaux  
`benoithypnose33@gmail.com` · `06 19 18 59 99`
