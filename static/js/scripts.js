const btnLogo = document.querySelector(".user");
const navbar = document.querySelector(".navbar");
const divCardUser = document.getElementById("m-card-user");
const iconUser = document.getElementById("icon-user");

divCardUser.style.display = "none";

btnLogo.addEventListener("click", () => {
    if (divCardUser.style.display === "none") {
        divCardUser.style.display = "flex";
        iconUser.src = "/static/img/x-circle.svg";
    } else {
        divCardUser.style.display = "none";
        iconUser.src = "/static/img/imgHome/user.svg";
    }
});

window.onscroll = function () {
    divCardUser.style.display = "none";
}


function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}