(function () {
  var header = document.querySelector("[data-header]");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  var toggle = document.querySelector("[data-nav-toggle]");
  var mobile = document.querySelector("[data-nav-mobile]");
  if (toggle && mobile) {
    toggle.addEventListener("click", function () {
      var open = mobile.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  var tabs = document.querySelectorAll("[data-tab]");
  var panels = document.querySelectorAll("[data-panel]");
  if (tabs.length && panels.length) {
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var id = tab.getAttribute("data-tab");
        tabs.forEach(function (t) {
          t.setAttribute("aria-selected", t === tab ? "true" : "false");
        });
        panels.forEach(function (panel) {
          panel.hidden = panel.getAttribute("data-panel") !== id;
        });
      });
    });
  }

  var sheet = document.querySelector("[data-sheet]");
  var backdrop = document.querySelector("[data-sheet-backdrop]");
  if (!sheet || !backdrop) return;

  function openSheet(e) {
    if (e) e.preventDefault();
    sheet.hidden = false;
    backdrop.hidden = false;
    requestAnimationFrame(function () {
      sheet.classList.add("open");
      backdrop.classList.add("open");
    });
  }

  function closeSheet() {
    sheet.classList.remove("open");
    backdrop.classList.remove("open");
    setTimeout(function () {
      sheet.hidden = true;
      backdrop.hidden = true;
    }, 280);
  }

  document.querySelectorAll("[data-open-sheet]").forEach(function (el) {
    el.addEventListener("click", openSheet);
  });
  document.querySelectorAll("[data-close-sheet]").forEach(function (el) {
    el.addEventListener("click", closeSheet);
  });
  backdrop.addEventListener("click", closeSheet);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeSheet();
  });
})();
