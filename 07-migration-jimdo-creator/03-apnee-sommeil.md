# Page — Troubles du sommeil & Apnées

**URL Jimdo :** `/troubles-du-sommeil`  
**Titre :** `Hypnose & Apnées du Sommeil — Benoît Raffard, Bordeaux`  
**Meta description :** `Hypnose et apnées du sommeil à Bordeaux. Benoît Raffard accompagne les patients non observants à leur traitement CPAP. Réseau médical structuré, résultats prouvés.`

**Images utilisées :**

| Placeholder | Fichier |
|---|---|
| `[IMG:cabinet-6]` | cabinet-6.png |

---

## Widget 0 — Navigation

**Widget Jimdo :** Élément HTML  
**Position :** tout premier élément de la page  
**Remplace la nav native Jimdo** (masquée via CSS override — voir guide)

```html
<nav id="nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo">
      <img src="[IMG:logo]" alt="Logo Benoît Raffard">
      Benoît <span>Raffard</span>
    </a>
    <ul class="nav-links">
      <li><a href="/">Accueil</a></li>
      <li><a href="/hypnose">L'hypnose</a></li>
      <li><a href="/troubles-du-sommeil" class="active">Troubles du sommeil</a></li>
      <li><a href="/a-propos">À propos</a></li>
      <li><a href="/contact">Contact & tarifs</a></li>
      <li><a href="https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33" target="_blank" class="nav-cta">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        Prendre RDV
      </a></li>
    </ul>
    <button class="nav-mobile-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="nav-mobile-menu">
  <a href="/">Accueil</a>
  <a href="/hypnose">L'hypnose</a>
  <a href="/troubles-du-sommeil" class="active">Troubles du sommeil</a>
  <a href="/a-propos">À propos</a>
  <a href="/contact">Contact & tarifs</a>
  <a href="https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33" target="_blank" class="nav-mobile-cta">Prendre rendez-vous</a>
</div>
<script>
(function() {
  var nav = document.getElementById('nav');
  window.addEventListener('scroll', function() {
    if (window.scrollY > 30) nav.classList.add('scrolled'); else nav.classList.remove('scrolled');
  });
  var toggle = document.querySelector('.nav-mobile-toggle');
  var mobileMenu = document.querySelector('.nav-mobile-menu');
  if (toggle && mobileMenu) {
    toggle.addEventListener('click', function() { mobileMenu.classList.toggle('open'); });
    document.querySelectorAll('.nav-mobile-menu a').forEach(function(a) {
      a.addEventListener('click', function() { mobileMenu.classList.remove('open'); });
    });
  }
})();
</script>
```

---

## Widget 1 — Hero Apnées

**Widget Jimdo :** Élément HTML  
**Position :** 1er élément

```html
<section class="apnee-hero">
  <div class="container">
    <div class="section-tag">Spécialité</div>
    <h1>Hypnose &<br><em>apnées du sommeil</em></h1>
    <p>Vous souffrez d'apnées du sommeil mais ne supportez pas votre masque de ventilation ? L'hypnose Ericksonienne agit sur les freins psychologiques qui empêchent l'observance du traitement — et les résultats sont mesurables.</p>
    <div class="apnee-hero-stats">
      <div>
        <div class="apnee-hero-stat-num">37%</div>
        <div class="apnee-hero-stat-label">des patients non observants<br>devenus observants</div>
      </div>
      <div>
        <div class="apnee-hero-stat-num">1–2</div>
        <div class="apnee-hero-stat-label">séances dans la majorité<br>des cas</div>
      </div>
      <div>
        <div class="apnee-hero-stat-num">2019</div>
        <div class="apnee-hero-stat-label">début du partenariat<br>avec les PSAD</div>
      </div>
    </div>
    <p class="apnee-hero-note">*Observation menée depuis 2019 en partenariat avec des prestataires de santé à domicile (PSAD).</p>
  </div>
</section>
```

---

## Widget 2 — Pourquoi le masque pose problème

**Widget Jimdo :** Élément HTML

```html
<section class="section">
  <div class="container">
    <div class="apnee-why-grid">
      <div class="apnee-why-text">
        <h2>Le masque : pas un problème technique, un problème psychologique</h2>
        <p>L'apnée du sommeil se traite efficacement avec une ventilation en pression positive (CPAP). Pourtant, une part significative des patients abandonne ce traitement — non pas parce qu'il ne fonctionne pas, mais parce qu'ils ne parviennent pas à tolérer le port du masque.</p>
        <p>Les raisons sont rarement mécaniques. Elles sont plus souvent psychologiques : une claustrophobie latente activée par le masque, une difficulté à accepter l'image renvoyée, ou simplement une résistance inconsciente à un objet perçu comme intrusif.</p>
        <p>C'est précisément là qu'intervient l'hypnose Ericksonienne. En travaillant sur l'inconscient — là où se logent ces résistances — elle permet de lever les freins qui bloquent l'observance, souvent en une à deux séances.</p>
      </div>
      <div class="apnee-why-image">
        <img src="[IMG:cabinet-6]" alt="Cabinet Benoît Raffard — consultation hypnose sommeil Bordeaux">
      </div>
    </div>
  </div>
</section>
```

---

## Widget 3 — Les freins à l'observance

**Widget Jimdo :** Élément HTML

```html
<section class="section section-warm">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">Les freins</div>
      <h2 class="section-title">Pourquoi certains patients <em>ne sont pas observants</em> ?</h2>
      <p class="section-desc">Derrière le rejet du masque se cachent des mécanismes psychologiques bien identifiés.</p>
    </div>
    <div class="raisons-grid">
      <div class="raison-card">
        <div class="raison-icon">😰</div>
        <h3>Claustrophobie</h3>
        <p>La sensation d'enfermement provoquée par le masque réactive une peur profonde, souvent inconsciente, de l'espace confiné.</p>
      </div>
      <div class="raison-card">
        <div class="raison-icon">🪞</div>
        <h3>Image de soi</h3>
        <p>Accepter de dormir appareillé implique une transformation de l'image corporelle nocturne difficile à intégrer pour certains patients.</p>
      </div>
      <div class="raison-card">
        <div class="raison-icon">😤</div>
        <h3>Désagrément sensoriel</h3>
        <p>Le bruit, la pression, la sensation mécanique du masque peuvent devenir insupportables lorsqu'une résistance inconsciente s'y ajoute.</p>
      </div>
      <div class="raison-card">
        <div class="raison-icon">🌙</div>
        <h3>Autres plaintes du sommeil</h3>
        <p>Certains patients sont orientés sans diagnostic d'apnées confirmé mais présentent des troubles : somnambulisme, terreurs nocturnes, éveils nocturnes fréquents.</p>
      </div>
      <div class="raison-card">
        <div class="raison-icon">🧠</div>
        <h3>Résistance inconsciente</h3>
        <p>Le traitement est compris et accepté rationnellement — mais une part du patient s'y oppose malgré tout. L'hypnose agit à ce niveau.</p>
      </div>
      <div class="raison-card">
        <div class="raison-icon">🤝</div>
        <h3>Manque d'accompagnement</h3>
        <p>Le suivi médical ne couvre pas toujours la dimension psychologique de l'observance. C'est le chaînon manquant que l'hypnose vient compléter.</p>
      </div>
    </div>
  </div>
</section>
```

---

## Widget 4 — Le protocole en pratique

**Widget Jimdo :** Élément HTML

```html
<section class="section">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">Comment ça se passe</div>
      <h2 class="section-title">Le protocole <em>en pratique</em></h2>
    </div>
    <div class="apnee-process">
      <div class="process-step">
        <div class="process-num">1</div>
        <div class="process-content">
          <h3>Orientation par un PSAD ou un médecin</h3>
          <p>Dom'Air Santé, SOS Oxygène ou votre pneumologue vous orientent vers le cabinet. Un compte-rendu peut être transmis au prescripteur si souhaité.</p>
        </div>
      </div>
      <div class="process-step">
        <div class="process-num">2</div>
        <div class="process-content">
          <h3>Entretien de cadrage (première séance)</h3>
          <p>Nous identifions ensemble la nature du frein : claustrophobie, image de soi, résistance inconsciente. Cette étape oriente le travail hypnotique.</p>
        </div>
      </div>
      <div class="process-step">
        <div class="process-num">3</div>
        <div class="process-content">
          <h3>Séance d'hypnose Ericksonienne</h3>
          <p>La séance travaille directement sur le mécanisme identifié. Vous restez pleinement conscient et acteur du processus.</p>
        </div>
      </div>
      <div class="process-step">
        <div class="process-num">4</div>
        <div class="process-content">
          <h3>Suivi et bilan</h3>
          <p>Dans la majorité des cas, 1 à 2 séances suffisent. Un bilan à distance permet de mesurer l'évolution de l'observance.</p>
        </div>
      </div>
    </div>
    <div class="apnee-legal-note">
      L'hypnose Ericksonienne est une approche complémentaire du traitement médical. Elle ne remplace pas la prise en charge par votre médecin ou votre prestataire de santé à domicile.
    </div>
  </div>
</section>
```

---

## Widget 5 — Partenaires médicaux

**Widget Jimdo :** Élément HTML

```html
<section class="section section-warm">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">Réseau</div>
      <h2 class="section-title">Des partenaires <em>médicaux structurés</em></h2>
      <p class="section-desc">Depuis 2019, je travaille en partenariat avec des prestataires de santé à domicile de la région pour les patients apnéiques.</p>
    </div>
    <div class="reseau-cards">
      <div class="reseau-card">
        <div class="reseau-card-name">Dom'Air Santé</div>
        <p>Partenariat historique — Symposia 2019 (Andorra) et 2023. Présentation des résultats aux pneumologues et ORL des Pyrénées Atlantique et Hautes-Pyrénées.</p>
      </div>
      <div class="reseau-card">
        <div class="reseau-card-name">SOS Oxygène</div>
        <p>Atelier "Hypnose & Trouble du Sommeil" au Congrès Cardiosleep (Corse, 2022). Collaboration active sur l'accompagnement des patients apnées.</p>
      </div>
    </div>
  </div>
</section>
```

---

## Widget 6 — Congrès

**Widget Jimdo :** Élément HTML

```html
<section class="section section-warm" style="padding-top: 0;">
  <div class="container">
    <div class="section-header" style="margin-top: 0; padding-top: 0;">
      <div class="section-tag">Congrès</div>
      <h2 class="section-title">Présenté devant <em>les professionnels</em></h2>
    </div>
    <div class="congres-mini">
      <div class="congres-mini-item">
        <div class="congres-mini-date">Mars 2023</div>
        <div class="congres-mini-text">Symposia Dom'Air Santé — résultats de 4 ans de partenariat (37% d'observance retrouvée)</div>
      </div>
      <div class="congres-mini-item">
        <div class="congres-mini-date">Nov. 2022</div>
        <div class="congres-mini-text">Congrès ORL & Pneumologie de l'Océan Indien — 2ème participation</div>
      </div>
      <div class="congres-mini-item">
        <div class="congres-mini-date">Juil. 2022</div>
        <div class="congres-mini-text">Congrès Cardiosleep, Corse — Atelier Hypnose & Trouble du Sommeil</div>
      </div>
      <div class="congres-mini-item">
        <div class="congres-mini-date">Déc. 2019</div>
        <div class="congres-mini-text">Congrès international, Île Maurice — Plénière "Hypnose et Sommeil"</div>
      </div>
      <div class="congres-mini-item">
        <div class="congres-mini-date">Mars 2019</div>
        <div class="congres-mini-text">Association des Pneumologues du Sud Ouest, Biarritz — Pneumologie et Hypnose</div>
      </div>
      <div class="congres-mini-item">
        <div class="congres-mini-date">Mars 2019</div>
        <div class="congres-mini-text">Symposia Dom'Air Santé, Andorra — présentation aux pneumologues, généralistes et ORL</div>
      </div>
    </div>
  </div>
</section>
```

---

## Widget 7 — Bande CTA

**Widget Jimdo :** Élément HTML

```html
<section class="cta-band">
  <div class="container">
    <div class="cta-inner">
      <h2>Vous êtes patient ou professionnel de santé ?</h2>
      <p>Prenez rendez-vous directement ou contactez-moi pour discuter d'une orientation.</p>
      <a href="https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33" target="_blank" class="btn-white">
        Prendre rendez-vous
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </div>
  </div>
</section>
```

---

## Widget — Bouton CTA mobile (visible mobile uniquement)

**Widget Jimdo :** Élément HTML  
**Position :** juste avant le footer

```html
<div class="mobile-cta">
  <a href="https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33" target="_blank">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
    Prendre rendez-vous
  </a>
</div>
```

---

## Widget 8 — Footer

**Widget Jimdo :** Élément HTML  
**Position :** dernier élément (identique sur toutes les pages)

```html
<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <div class="footer-left">
        <div class="footer-brand">Benoît <span>Raffard</span></div>
        <div class="footer-contact">
          <a href="https://maps.google.com/?q=28+rue+Scaliger+33000+Bordeaux" target="_blank">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            28 rue Scaliger, Bordeaux
          </a>
          <a href="tel:0619185999">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.11 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            06 19 18 59 99
          </a>
        </div>
      </div>
      <div class="footer-right">
        <a href="/contact#mentions-legales">Mentions légales</a><span class="footer-sep">·</span>
        <a href="/contact#confidentialite">Confidentialité</a><span class="footer-sep">·</span>
        <span style="font-size:0.75rem;color:rgba(255,255,255,0.35);">© 2026</span>
      </div>
    </div>
  </div>
</footer>
```
