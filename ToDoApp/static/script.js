const btnScroolTo = document.querySelector(".btn--scroll-to");
const section1 = document.querySelector("#section--1");
btnScroolTo.addEventListener("click", () =>
  section1.scrollIntoView({ behavior: "smooth" })
);

document.querySelector(".nav__links").addEventListener("click", (e) => {
  e.preventDefault();
  if (e.target.classList.contains("nav__link")) {
    const id = e.target.getAttribute("href");
    document.querySelector(id).scrollIntoView({
      behavior: "smooth",
    });
  }
});
