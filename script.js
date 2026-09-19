(function () {
  var header = document.querySelector("[data-header]");
  var toTop = document.querySelector("[data-to-top]");

  function onScroll() {
    var y = window.scrollY || 0;
    if (header) header.classList.toggle("is-scrolled", y > 24);
    if (toTop) toTop.classList.toggle("is-on", y > 480);
  }

  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  var toggle = document.querySelector("[data-nav-toggle]");
  var mobile = document.querySelector("[data-nav-mobile]");
  if (toggle && mobile) {
    toggle.addEventListener("click", function () {
      var open = mobile.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll("[data-dd]").forEach(function (dd) {
    var btn = dd.querySelector("button");
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      document.querySelectorAll("[data-dd]").forEach(function (other) {
        if (other !== dd) other.classList.remove("is-open");
      });
      dd.classList.toggle("is-open");
    });
  });

  document.addEventListener("click", function (e) {
    document.querySelectorAll("[data-dd].is-open").forEach(function (dd) {
      if (!dd.contains(e.target)) dd.classList.remove("is-open");
    });
  });

  var words = document.querySelectorAll("[data-hero-word]");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (words.length > 1 && !reduce.matches) {
    var i = 0;
    setInterval(function () {
      words[i].classList.remove("is-active");
      i = (i + 1) % words.length;
      words[i].classList.add("is-active");
    }, 2800);
  }

  function hideVideo(video) {
    video.classList.add("is-missing");
    video.removeAttribute("src");
    video.querySelectorAll("source").forEach(function (s) {
      s.removeAttribute("src");
    });
    try { video.load(); } catch (err) {}
  }

  function playVideo(video) {
    if (reduce.matches) {
      video.pause();
      video.removeAttribute("autoplay");
      return;
    }
    video.muted = true;
    video.playsInline = true;
    var play = video.play();
    if (play && play.catch) play.catch(function () {});
  }

  document.querySelectorAll("video[data-auto-loop]").forEach(function (video) {
    var source = video.querySelector("source");
    var url = source && source.getAttribute("src");
    video.addEventListener("error", function () { hideVideo(video); });
    if (source) {
      source.addEventListener("error", function () { hideVideo(video); });
    }
    if (!url) {
      hideVideo(video);
      return;
    }
    fetch(url, { method: "HEAD" })
      .then(function (res) {
        if (res.ok || res.status === 405) {
          playVideo(video);
          return;
        }
        hideVideo(video);
      })
      .catch(function () {
        hideVideo(video);
      });
  });

  if (reduce.addEventListener) {
    reduce.addEventListener("change", function () {
      document.querySelectorAll("video[data-auto-loop]").forEach(function (video) {
        if (reduce.matches) {
          video.pause();
        } else {
          video.muted = true;
          var play = video.play();
          if (play && play.catch) play.catch(function () {});
        }
      });
    });
  }

  var sheet = document.querySelector("[data-sheet]");
  var backdrop = document.querySelector("[data-sheet-backdrop]");
  if (sheet && backdrop) {
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
  }
})();
