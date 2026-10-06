/* TNRN Digital Hub — small progressive enhancements (site works without JS). */
(function () {
  "use strict";

  // Review mode: append ?review to any page URL to outline all draft copy
  // (elements marked with data-draft) for content reviewers.
  if (new URLSearchParams(window.location.search).has("review")) {
    document.documentElement.classList.add("review-mode");
  }

  // Current year in footer
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Close the mobile menu with Escape and return focus to the toggle button
  var nav = document.getElementById("mainNav");
  var toggler = document.querySelector('[data-bs-target="#mainNav"]');
  if (nav && toggler && window.bootstrap) {
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("show")) {
        bootstrap.Collapse.getOrCreateInstance(nav).hide();
        toggler.focus();
      }
    });
  }
})();
