// NAV scroll state
const nav = document.getElementById('nav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });
}

// Mobile menu toggle
const toggle = document.querySelector('.nav-mobile-toggle');
const mobileMenu = document.querySelector('.nav-mobile-menu');
if (toggle && mobileMenu) {
  toggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
  });
  document.addEventListener('click', (e) => {
    if (!nav.contains(e.target)) mobileMenu.classList.remove('open');
  });
}

// FAQ accordion
document.querySelectorAll('.faq-question').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const answer = item.querySelector('.faq-answer');
    const isOpen = item.classList.contains('open');

    // Fermer tous
    document.querySelectorAll('.faq-item').forEach(i => {
      i.classList.remove('open');
      i.querySelector('.faq-answer').style.maxHeight = '0';
    });

    // Ouvrir si était fermé
    if (!isOpen) {
      item.classList.add('open');
      answer.style.maxHeight = answer.scrollHeight + 'px';
    }
  });
});

// Ouvrir le premier FAQ par défaut
const firstFaq = document.querySelector('.faq-item');
if (firstFaq) {
  firstFaq.classList.add('open');
  const ans = firstFaq.querySelector('.faq-answer');
  if (ans) ans.style.maxHeight = ans.scrollHeight + 'px';
}
