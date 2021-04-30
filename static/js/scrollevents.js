function isScrolledIntoView(el) {
    var rect = el.getBoundingClientRect();
    var elemTop = rect.top;
    var elemBottom = rect.bottom;

    // Only completely visible elements return true:
    var isVisible = (elemTop >= 0) && (elemBottom <= window.innerHeight);
    // Partially visible elements return true:
    //isVisible = elemTop < window.innerHeight && elemBottom >= 0;
    return isVisible;
}

const el = document.getElementById("m-cardds")
el.style.display = "none"

window.onscroll = function () {
    if (isScrolledIntoView(el)) {
        el.style.display = "block";
        el.classList.add("animate__animated");
        el.classList.add("animate__fadeInDown");
    }
};