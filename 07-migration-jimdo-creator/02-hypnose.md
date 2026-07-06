# Page — L'hypnose Ericksonienne

**URL Jimdo :** `/hypnose`
**Titre :** `L'hypnose Ericksonienne — Benoît Raffard, Hypnothérapeute Bordeaux`
**Meta description :** `Qu'est-ce que l'hypnose Ericksonienne ? Découvrez comment elle fonctionne, ses indications (stress, sommeil, tabac, phobies) et les réponses à vos questions.`

**Images utilisées :**

| Placeholder | Fichier |
|---|---|
| `[IMG:cabinet-6]` | cabinet-6.png |
| `[IMG:cabinet-5]` | cabinet-5.png |
| `[IMG:cabinet-1]` | cabinet-1.png |

> Comme convenu : laisse les `[IMG:xxx]` tels quels pour l'instant. On fera la passe upload/remplacement d'images en une seule fois, une fois toutes les pages posées.

---

## Rappels avant de commencer (leçons de la page Troubles du sommeil)

- **Ajoute chaque widget au milieu de la page**, jamais dans la colonne étroite de gauche ni collé contre le footer tout en bas — ces zones sont partagées entre toutes les pages sur ce thème et dupliqueront le contenu partout.
- Si un doute sur l'emplacement, test rapide : colle `<h1>TEST</h1>`, enregistre, vérifie sur une autre page (ex: Séance) que ça n'apparaît pas.
- Les liens de nav (`/hypnose`, `/a-propos`, `/contact`, `/troubles-du-sommeil`) restent en placeholder pour l'instant — correction groupée prévue une fois toutes les pages posées, avec les vrais slugs Jimdo.

---

## Widget 0 — Navigation

**Widget Jimdo :** Widget / HTML
**Position :** tout premier élément de la page

```html
<nav id="nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo">
      <img src="[IMG:logo]" alt="Logo Benoît Raffard">
      Benoît <span>Raffard</span>
    </a>
    <ul class="nav-links">
      <li><a href="/">Accueil</a></li>
      <li><a href="/hypnose" class="active">L'hypnose</a></li>
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
  <a href="/">Accueil</a>
  <a href="/hypnose" class="active">L'hypnose</a>
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

## Widget 1 — En-tête de page

**Widget Jimdo :** Widget / HTML
**Position :** 1er élément après la nav

```html
<section class="page-hero">
  <div class="container">
    <div class="section-tag">Comprendre</div>
    <h1>L'hypnose <em>Ericksonienne</em></h1>
    <p>Un état naturel de conscience modifiée, guidé par la communication, pour accéder à vos ressources intérieures.</p>
  </div>
</section>
```

---

## Widget 2 — Introduction

**Widget Jimdo :** Widget / HTML

```html
<section class="section">
  <div class="container">
    <div class="hypno-intro-grid">
      <div class="hypno-intro-text">
        <h2>Ce n'est pas ce que vous croyez</h2>
        <p>Oubliez l'hypnose de spectacle. L'hypnose Ericksonienne est une pratique thérapeutique douce, où vous restez pleinement conscient et maître de vous-même.</p>
        <p>Elle induit un état de rêverie — comme quand vous conduisez en "pilote automatique" — qui permet d'accéder à votre inconscient. D'après Milton Erickson, celui-ci est un réservoir d'expérience et de sagesse, un terreau fertile en solutions.</p>
        <p>Le cerveau produit des endorphines, sources de bien-être. Le thérapeute vous guide afin de créer ou réactiver des connexions inconscientes. Votre implication et votre motivation sont les clés de la réussite de votre démarche et de l'atteinte de vos objectifs.</p>
      </div>
      <div class="hypno-intro-image">
        <img src="[IMG:cabinet-6]" alt="Ambiance cabinet hypnose Bordeaux — salle d'attente">
      </div>
    </div>
  </div>
</section>
```

---

## Widget 3 — Bande photos cabinet

**Widget Jimdo :** Widget / HTML

```html
<div class="container" style="margin-bottom: 0;">
  <div class="photo-strip">
    <div class="photo-strip-img">
      <img src="[IMG:cabinet-5]" alt="Cabinet hypnose Bordeaux — espace de consultation">
    </div>
    <div class="photo-strip-img">
      <img src="[IMG:cabinet-1]" alt="Cabinet hypnose Bordeaux — fauteuils">
    </div>
  </div>
</div>
```

---

## Widget 4 — Indications (12 cartes)

**Widget Jimdo :** Widget / HTML

```html
<section class="section section-warm">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">Indications</div>
      <h2 class="section-title">Pour quelles <em>situations ?</em></h2>
      <p class="section-desc">L'hypnose Ericksonienne s'applique à un large éventail de troubles et d'objectifs de développement personnel.</p>
    </div>
    <div class="indications-full-grid">
      <div class="indication-full-card">
        <div class="icon">😰</div>
        <h3>Angoisse & stress</h3>
        <p>Gestion du stress chronique, crises d'angoisse, anxiété généralisée.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">🌙</div>
        <h3>Troubles du sommeil</h3>
        <p>Insomnie, apnées du sommeil, terreurs nocturnes, somnambulisme, difficultés d'endormissement, éveils nocturnes, paralysie du sommeil.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">🚭</div>
        <h3>Addictions</h3>
        <p>Tabac, alcool, jeu, travail — se libérer des comportements compulsifs.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">😟</div>
        <h3>États dépressifs</h3>
        <p>Accompagnement complémentaire pour sortir d'un état dépressif.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">🕷️</div>
        <h3>Peurs & phobies</h3>
        <p>Phobie de l'avion, claustrophobie, arachnophobie, peur du vide…</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">🔁</div>
        <h3>TOC & compulsions</h3>
        <p>Comportements répétitifs, compulsions alimentaires, rituels envahissants.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">⚖️</div>
        <h3>Surpoids</h3>
        <p>Travailler sur la relation à la nourriture et les comportements alimentaires.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">💔</div>
        <h3>Traumatismes & étapes de vie</h3>
        <p>Deuil, divorce, chocs émotionnels — traverser et dépasser les moments difficiles.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">💪</div>
        <h3>Confiance en soi</h3>
        <p>Estime de soi, gestion des émotions, créativité, écoute de soi.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">🎯</div>
        <h3>Préparation mentale</h3>
        <p>Examens, compétitions sportives, entretiens, prise de parole en public.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">🔄</div>
        <h3>Reconversion professionnelle</h3>
        <p>Lever les freins et développer ses capacités pour une nouvelle carrière.</p>
      </div>
      <div class="indication-full-card">
        <div class="icon">🧒</div>
        <h3>Aide scolaire</h3>
        <p>Concentration, mémoire, stress des examens, bégaiement, énurésie.</p>
      </div>
    </div>
    <div class="disclaimer">
      <strong>Important :</strong> une séance d'hypnose ne remplace en aucun cas un avis ou un traitement médical. Seul un médecin est habilité à poser un diagnostic et à prescrire un traitement. L'hypnose peut vous accompagner en complément — parlez-en avec votre médecin.
    </div>
  </div>
</section>
```

---

## Widget 5 — Traumatismes

**Widget Jimdo :** Widget / HTML

```html
<section class="section">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">Traumatismes</div>
      <h2 class="section-title">Un outil <em>puissant</em> sur les chocs émotionnels</h2>
    </div>
    <div class="trauma-grid">
      <div class="trauma-text">
        <h2>Ce que les mots ne suffisent pas à défaire</h2>
        <p>Certaines expériences s'inscrivent dans le corps et l'inconscient bien au-delà de ce que la réflexion consciente peut atteindre. Un accident, une agression, un deuil brutal, une rupture dévastatrice — le traumatisme laisse une empreinte qui peut continuer à agir des années après les faits.</p>
        <p>L'hypnose Ericksonienne est particulièrement adaptée à ce type de travail. En accédant directement à l'inconscient — là où la mémoire émotionnelle est stockée — elle permet de modifier la charge affective associée à un souvenir sans nécessairement le revivre, et de créer de nouveaux ancrages plus apaisants.</p>
        <p>Ce n'est pas un effacement. C'est une transformation de la relation que vous entretenez avec ce qui s'est passé.</p>
        <div class="trauma-exemples">
          <span class="trauma-tag">Accidents</span>
          <span class="trauma-tag">Agression</span>
          <span class="trauma-tag">Deuil brutal</span>
          <span class="trauma-tag">Rupture</span>
          <span class="trauma-tag">Choc émotionnel</span>
          <span class="trauma-tag">Burn-out</span>
          <span class="trauma-tag">Violence passée</span>
        </div>
      </div>
      <div class="trauma-quote">
        <div class="trauma-quote-text">« L'inconscient est un réservoir de ressources — il contient aussi la capacité de guérir ce qu'il a subi. »</div>
        <div class="trauma-quote-sub">L'hypnose Ericksonienne ne force rien. Elle crée les conditions pour que votre inconscient trouve, à son rythme, le chemin vers un rapport apaisé avec votre vécu.<br><br>Ce travail se fait en complément d'un suivi psychologique ou psychiatrique si nécessaire.</div>
      </div>
    </div>
  </div>
</section>
```

---

## Widget 6 — FAQ (accordéon + script inclus)

**Widget Jimdo :** Widget / HTML

> ⚠️ Le script fait partie intégrante du widget — colle-le en entier, ne le sépare pas dans un autre bloc. Il gère l'ouverture/fermeture des questions au clic.

```html
<section class="section section-warm">
  <div class="container">
    <div class="section-header">
      <div class="section-tag">FAQ</div>
      <h2 class="section-title">Questions <em>fréquentes</em></h2>
    </div>
    <div class="faq-list">
      <div class="faq-item">
        <button class="faq-question">
          Est-ce que je perds le contrôle sous hypnose ?
          <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">Non. Vous restez pleinement conscient, comme lors d'une rêverie. Vous êtes apaisé et toujours maître de vous-même. Il n'y a aucune perte de contrôle.</div>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          Combien de séances faut-il ?
          <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">Cela dépend du sujet : certaines problématiques se traitent en 1 à 3 séances, d'autres demandent un suivi plus long. On fait le point ensemble à chaque fois.</div>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          L'hypnose fonctionne-t-elle sur tout le monde ?
          <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">Oui, tout le monde peut entrer en état d'hypnose — c'est un état naturel que vous vivez au quotidien. La clé repose sur votre motivation et votre participation active.</div>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          C'est remboursé ?
          <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">Pas par la sécurité sociale, mais de plus en plus de complémentaires santé proposent un forfait "médecines douces" qui couvre une partie des séances. Renseignez-vous auprès de la vôtre.</div>
        </div>
      </div>
    </div>
    <div style="text-align:center; margin-top: 40px;">
      <a href="/contact" class="btn-ghost">Une question ? Contactez-moi</a>
    </div>
  </div>
</section>
<script>
(function() {
  document.querySelectorAll('.faq-item').forEach(function(item) {
    var btn = item.querySelector('.faq-question');
    var answer = item.querySelector('.faq-answer');
    btn.addEventListener('click', function() {
      var isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function(openItem) {
        openItem.classList.remove('open');
        openItem.querySelector('.faq-answer').style.maxHeight = null;
      });
      if (!isOpen) {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });
})();
</script>
```

---

## Widget 7 — Bande CTA

**Widget Jimdo :** Widget / HTML

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

**Widget Jimdo :** Widget / HTML
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

**Widget Jimdo :** Widget / HTML
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

---

## Checklist spécifique à cette page

- [ ] FAQ : l'accordéon s'ouvre/ferme au clic (script du Widget 6 bien collé en entier)
- [ ] Grille indications (12 cartes) : s'affiche en 3 colonnes desktop, 1 colonne mobile
- [ ] Aucun widget posé dans la colonne de gauche ou collé au footer (risque de duplication sur toutes les pages)
- [ ] Lien actif "L'hypnose" bien surligné dans la nav sur cette page uniquement
