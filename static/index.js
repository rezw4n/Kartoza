const navBar = document.getElementById("navbar");
const showNav = document.getElementById("showNav");
const hideNav = document.getElementById("hideNav");

showNav.onclick = function showNavBar() {
    navBar.classList.remove("hidden");
}

hideNav.onclick = function hideNavBar() {
    navBar.classList.add("hidden");
}