const btnLogo = document.querySelector(".user");
const navbar = document.querySelector(".navbar");
const divCardUser = document.getElementById("m-card-user");
divCardUser.style.display = "none";

btnLogo.addEventListener("click", () => {
    if (divCardUser.style.display === "none") {
        divCardUser.style.display = "flex";
    } else {
        divCardUser.style.display = "none";
    }
});