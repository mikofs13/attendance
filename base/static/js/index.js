const ham = document.getElementById("ham");
const nav2 = document.getElementById("nav2");
const nav = document.getElementById("myNav");

ham.addEventListener("click", () => {
    ham.classList.toggle("change");
    nav.classList.toggle("overlay1");
  });