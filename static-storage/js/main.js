const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


const slider = document.querySelector(".bd-example");
const nav = document.querySelector("nav");
const options = {
    root: null,
    threshold: 0,
    rootMargin: "-70px"
}

const observer = new IntersectionObserver(function (entries, observer) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            nav.classList.remove('bg-tran');
            nav.classList.add('inverse');
        }
        else {
            console.log(entry.target);
            nav.classList.add('bg-tran');
            nav.classList.remove('inverse');
        }
    })
}, options);

observer.observe(slider);