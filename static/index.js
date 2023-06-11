// Navigation Bar JS Start
const navBar = document.getElementById("navbar");
const showNav = document.getElementById("showNav");
const hideNav = document.getElementById("hideNav");

showNav.onclick = function showNavBar() {
  navBar.classList.remove("hidden");
};

hideNav.onclick = function hideNavBar() {
  navBar.classList.add("hidden");
};
// Navigation Bar JS End

// Geolocation Code JS Start

const getLocationBtn = document.getElementById("getLocationBtn");
let latitudeBox = document.getElementById("latitude");
let longitudeBox = document.getElementById("longitude");

if (!latitudeBox){
  latitudeBox = document.getElementById("id_latitude");
  longitudeBox = document.getElementById("id_longitude");
}

if (getLocationBtn) {
  getLocationBtn.addEventListener("click", function () {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function (position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        latitudeBox.value = latitude;
        longitudeBox.value = longitude;
      });
    } else {
      alert("Geolocation is not supported by this browser.");
    }
  });
}
// Geolocation Code JS End
