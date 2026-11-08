---
layout: page
title: Contact
permalink: /contact/
description: Get in touch about Betterbox, or join the waitlist for a printed deck.
---

# Contact

Get in touch about Betterbox, or join the waitlist for a printed deck.

<form class="form" action="https://formspree.io/f/mdeevqro" method="POST" data-formspree>
  <input type="hidden" name="_subject" value="Betterbox contact form">
  <div class="form__field">
    <label for="cf-name">Name</label>
    <input id="cf-name" name="name" type="text" autocomplete="name" required>
  </div>
  <div class="form__field">
    <label for="cf-email">Email</label>
    <input id="cf-email" name="email" type="email" autocomplete="email" required>
  </div>
  <div class="form__field">
    <label for="cf-message">Message <span class="form__optional">(optional)</span></label>
    <textarea id="cf-message" name="message" rows="6"></textarea>
  </div>
  <div class="form__check">
    <input id="cf-waitlist" name="waitlist" type="checkbox" value="Yes, add me to the printed deck waitlist">
    <label for="cf-waitlist">Add me to the waitlist for a printed deck</label>
  </div>
  <p class="form__gotcha" aria-hidden="true"><label>Leave this empty <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
  <button class="btn" type="submit">Send</button>
  <p class="form__status" role="status" aria-live="polite"></p>
</form>

<script>
// Send the form without leaving the page when JavaScript is available.
// Without JavaScript the form posts to Formspree as normal.
(function () {
  var form = document.querySelector('form[data-formspree]');
  if (!form || !window.fetch) return;
  var status = form.querySelector('.form__status');
  if (location.search.indexOf('waitlist') !== -1) form.querySelector('#cf-waitlist').checked = true;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var button = form.querySelector('button[type=submit]');
    button.disabled = true;
    status.textContent = 'Sending…';
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
      .then(function (r) {
        if (r.ok) {
          form.reset();
          status.textContent = 'Thanks, your message has been sent.';
        } else {
          status.textContent = 'Sorry, something went wrong. Please try again.';
        }
      })
      .catch(function () { status.textContent = 'Sorry, something went wrong. Please try again.'; })
      .then(function () { button.disabled = false; });
  });
})();
</script>
