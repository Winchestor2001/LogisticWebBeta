let main_container = document.querySelector(".main_container");
let signin_modal = document.querySelector(".signin_form");
let signup_modal = document.querySelector(".signup_form");
let right_toper_btn = document.querySelector(".right_toper_btn");
let stars_rate = document.querySelectorAll(".stars_rate");
let order_success_form = document.querySelector(".order_success_form");
let header_menu = document.querySelector(".header_menu");

function starsRate() {
  stars_rate.forEach((item) => {
    let stars = item.getAttribute("data-stars");
    let star_tag1 = `<i class="fa-regular fa-star single_star"></i>`;
    let star_tag2 = `<i class="fa-solid fa-star single_star yes"></i>`;
    for (let i = 0; i < 5; i++) {
      if (i >= stars) {
        item.insertAdjacentHTML("beforeend", star_tag1);
      } else {
        item.insertAdjacentHTML("beforeend", star_tag2);
      }
    }
  });
}

function signinModal() {
  main_container.classList.toggle("active2");
  signin_modal.classList.toggle("active2");
}
function signupModal() {
  main_container.classList.toggle("active2");
  signup_modal.classList.toggle("active2");
}
function orderSuccessModal() {
  main_container.classList.toggle("active2");
  order_success_form.classList.toggle("active2");
}

right_toper_btn.onclick = () => {
  document.documentElement.scrollTop = 0;
};
window.onscroll = () => {
  if (window.pageYOffset > 400) {
    right_toper_btn.classList.add("active3");
  } else {
    right_toper_btn.classList.remove("active3");
  }
  if (window.pageYOffset > 50) {
    header_menu.style.position = 'fixed';
    header_menu.style.backdropFilter = 'blur(15px)';
  } else {
    header_menu.style.position = 'sticky';
    header_menu.style.backdropFilter = 'none';
  }
};

starsRate();



