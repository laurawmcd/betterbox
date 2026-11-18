// Shrink the text on each drawn card until all of it fits inside the card,
// so the pictures show the full printed text instead of cutting it off.
(function () {
  var MIN = 0.5;   // never go below half the normal size
  var STEP = 0.04;

  function fit(card) {
    var body = card.querySelector('.card-face__body');
    if (!body) return;
    body.style.fontSize = '';
    var scale = 1;
    while (body.scrollHeight > body.clientHeight + 1 && scale > MIN) {
      scale = Math.max(MIN, scale - STEP);
      body.style.fontSize = scale + 'em';
    }
  }

  function fitAll() {
    var cards = document.querySelectorAll('.card-face:not(.card-face--lg):not(.card-face--blank)');
    for (var i = 0; i < cards.length; i++) fit(cards[i]);
  }

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(fitAll);
  } else {
    window.addEventListener('load', fitAll);
  }
  var t;
  window.addEventListener('resize', function () {
    clearTimeout(t);
    t = setTimeout(fitAll, 150);
  });
})();
