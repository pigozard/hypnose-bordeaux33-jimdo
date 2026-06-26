# Page — Accueil

**URL Jimdo :** `/` (page d'accueil)  
**Titre :** `Benoît Raffard — Hypnothérapeute à Bordeaux | Hypnose Ericksonienne`  
**Meta description :** `Benoît Raffard, hypnothérapeute à Bordeaux. Hypnose ericksonienne pour stress, sommeil, tabac, confiance en soi. Cabinet rue Scaliger & visio.`

**Images utilisées :**

| Placeholder | Fichier |
|---|---|
| `[IMG:portrait]` | portrait.png |
| `[IMG:facade-2]` | facade-2.png |
| `[IMG:cabinet-1]` | cabinet-1.png |
| `[IMG:cabinet-5]` | cabinet-5.png |

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
      <li><a href="/" class="active">Accueil</a></li>
      <li><a href="/hypnose">L'hypnose</a></li>
      <li><a href="/troubles-du-sommeil">Troubles du sommeil</a></li>
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
  <a href="/" class="active">Accueil</a>
  <a href="/hypnose">L'hypnose</a>
  <a href="/troubles-du-sommeil">Troubles du sommeil</a>
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

## Widget 1 — Hero

**Widget Jimdo :** Élément HTML  
**Position :** 1er élément

```html
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-content">
      <div class="hero-badge">Hypnothérapeute à Bordeaux</div>
      <h1>Retrouvez votre<br><em>équilibre intérieur</em></h1>
      <p class="hero-subtitle">Je vous accompagne pour dépasser vos blocages et retrouver vos ressources. En cabinet au cœur de Bordeaux ou en visio.</p>
      <div class="hero-actions">
        <a href="https://www.crenolibre.fr/prendre-rdv/15117_benoit-raffard-hypnose-bordeaux-33" target="_blank" class="btn-primary">
          Prendre rendez-vous
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </a>
        <a href="/hypnose" class="btn-ghost">Découvrir l'hypnose</a>
      </div>
      <div class="hero-trust">
        <div class="hero-trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          Adhérent SNH
        </div>
        <div class="hero-trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          Maître Praticien certifié
        </div>
        <div class="hero-trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          En pratique depuis 2018
        </div>
      </div>
    </div>
    <div class="hero-photo">
      <div class="hero-photo-frame">
        <img src="[IMG:portrait]" alt="Benoît Raffard, hypnothérapeute à Bordeaux">
      </div>
      <div class="hero-float-card">
        <div class="hero-float-card-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#5B7E6B" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        </div>
        <div class="hero-float-card-text">
          <strong>28 rue Scaliger</strong>
          Bordeaux centre
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Widget 2 — Bande photos cabinet

**Widget Jimdo :** Élément HTML

```html
<div class="cabinet-band">
  <div class="cabinet-band-img">
    <img src="[IMG:facade-2]" alt="28 rue Scaliger, Bordeaux — entrée du cabinet">
  </div>
  <div class="cabinet-band-img">
    <img src="[IMG:cabinet-1]" alt="Cabinet hypnose Bordeaux — ambiance">
  </div>
  <div class="cabinet-band-img">
    <img src="[IMG:cabinet-5]" alt="Cabinet hypnose Bordeaux — fauteuils">
  </div>
</div>
```

---

## Widget 3 — Indications « Pour qui ? »

**Widget Jimdo :** Élément HTML

```html
<section class="section section-warm">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">Pour qui ?</div>
      <h2 class="section-title">L'hypnose peut <em>vous aider</em></h2>
      <p class="section-desc">Vous portez déjà en vous les ressources pour avancer. Mon rôle est de vous aider à y accéder.</p>
    </div>
    <div class="indications-grid">
      <div class="indication-card">
        <div class="indication-icon">🌿</div>
        <div>
          <h3>Stress & anxiété</h3>
          <p>Retrouvez un état de calme durable en agissant sur les mécanismes profonds de l'angoisse.</p>
        </div>
      </div>
      <div class="indication-card">
        <div class="indication-icon">🌙</div>
        <div>
          <h3>Troubles du sommeil</h3>
          <p>Insomnie, apnées, terreurs nocturnes — une spécialité de mon cabinet avec un réseau médical expert.</p>
        </div>
      </div>
      <div class="indication-card">
        <div class="indication-icon">🚭</div>
        <div>
          <h3>Arrêt du tabac</h3>
          <p>Un protocole en 2 séances pour se libérer durablement, sans substitut.</p>
        </div>
      </div>
      <div class="indication-card">
        <div class="indication-icon">💫</div>
        <div>
          <h3>Traumatismes</h3>
          <p>Un outil pour libérer ce que le temps n'a pas effacé.</p>
        </div>
      </div>
    </div>
    <div class="indications-more">
      <a href="/hypnose" class="btn-ghost">Voir toutes les indications</a>
    </div>
  </div>
</section>
```

---

## Widget 4 — Teaser Apnées du sommeil

**Widget Jimdo :** Élément HTML

```html
<section class="section" style="padding: 48px 0;">
  <div class="container">
    <div class="apnee-teaser">
      <div>
        <div class="apnee-teaser-tag">Spécialité</div>
        <h2>Apnées du sommeil —<br>une approche <em>complémentaire</em></h2>
        <p>Vous portez un masque de ventilation nocturne mais ne supportez pas son port ? Claustrophobie, image de soi, inconfort… l'hypnose agit sur les freins psychologiques qui empêchent l'observance du traitement.</p>
        <div class="apnee-teaser-stats">
          <div>
            <div class="apnee-stat-num">37%</div>
            <div class="apnee-stat-label">des patients non observants<br>devenus observants</div>
          </div>
          <div>
            <div class="apnee-stat-num">1–2</div>
            <div class="apnee-stat-label">séances suffisantes<br>dans la majorité des cas</div>
          </div>
        </div>
        <a href="/troubles-du-sommeil" class="apnee-teaser-cta">
          En savoir plus
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </a>
      </div>
      <div class="apnee-teaser-logo">
        <div class="apnee-partner-tag">Réseau partenaires</div>
        <div class="apnee-partner-pill">Dom'Air Santé</div>
        <div class="apnee-partner-pill">SOS Oxygène</div>
      </div>
    </div>
  </div>
</section>
```

---

## Widget 5 — 3 Étapes « Comment ça se passe ? »

**Widget Jimdo :** Élément HTML

```html
<section class="section">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">La séance</div>
      <h2 class="section-title">Comment ça <em>se passe ?</em></h2>
      <p class="section-desc">Pas de pendule, pas de perte de contrôle. Un moment de rêverie guidée où vous restez pleinement conscient.</p>
    </div>
    <div class="steps-grid">
      <div class="step">
        <div class="step-number">1</div>
        <h3>Échange</h3>
        <p>Vous m'expliquez votre situation. Nous définissons ensemble un objectif clair.</p>
      </div>
      <div class="step">
        <div class="step-number">2</div>
        <h3>Transe guidée</h3>
        <p>Je vous guide dans un état de conscience modifiée. Votre inconscient fait le travail.</p>
      </div>
      <div class="step">
        <div class="step-number">3</div>
        <h3>Bilan</h3>
        <p>On fait le point sur votre ressenti et on décide ensemble de la suite.</p>
      </div>
    </div>
  </div>
</section>
```

---

## Widget 6 — Témoignages

**Widget Jimdo :** Élément HTML

```html
<section class="section section-warm">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">Témoignages</div>
      <h2 class="section-title">Ils m'ont <em>fait confiance</em></h2>
    </div>
    <div class="testimonials-grid">
      <div class="testimonial-card">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-text">« Après deux séances pour un sevrage tabagique j'ai complètement réussi à arrêter de fumer et n'en ressens que du bien. Benoît est très à l'écoute. »</p>
        <div class="testimonial-author">Sebastien B. <span>— Arrêt du tabac</span></div>
      </div>
      <div class="testimonial-card">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-text">« Dès la première séance les changements de mon sommeil ont été incroyables, plus aucun cauchemar. Après une petite semaine d'adaptation, mes nuits ne sont plus les mêmes. Un grand merci à M. Raffard que je recommande vivement ! »</p>
        <div class="testimonial-author">Manon P. <span>— Troubles du sommeil</span></div>
      </div>
      <div class="testimonial-card">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-text">« Je suis venue pour travailler sur ma peur du sang et des aiguilles, maintenant en parler ne me dérange plus et je viens même de faire ma première prise de sang sans malaise ! »</p>
        <div class="testimonial-author">Mélissa C. <span>— Phobie</span></div>
      </div>
      <div class="testimonial-card">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-text">« Après une vingtaine de jours après la deuxième séance, plus rien. J'ai même accueilli un chat chez moi 3 semaines sans aucun signe d'allergies. »</p>
        <div class="testimonial-author">Arthur T. <span>— Allergie/phobie</span></div>
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
      <h2>Prêt à franchir le pas ?</h2>
      <p>Le premier rendez-vous est le plus important.</p>
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
**Position :** dernier élément (remplace le footer natif Jimdo)

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
