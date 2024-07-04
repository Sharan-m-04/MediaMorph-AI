// const header = document.querySelector(".header");

// navLinks.addEventListener("click", () => {
//   header.classList.toggle("header-expanded");
// });

// function toggleMenu() {
//   const navLinks = document.querySelectorAll(".nav-links");
//   navLinks.forEach((nav) => nav.classList.toggle("active"));
//   document.querySelector(".hamburger").classList.toggle("active");
// }

function loginBtn() {
  window.open("/accounts/login", (target = "_self"));
}

function getstarted() {
  window.open("/accounts/signup", (target = "_self"));
}

function reveal() {
    var reveals = document.querySelectorAll(".reveal");

    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;

        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add("acti");
        } else {
            reveals[i].classList.remove("acti");
        }
    }
}

window.addEventListener("scroll", reveal);

// window.toggleMenu = toggleMenu;