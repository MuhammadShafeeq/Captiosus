function addBoxShadow() {
    var navbar = document.getElementById('navbar')
    var scrollVal = window.scrollY;
    if (scrollVal > 449) {
        navbar.classList.add('box-shadow')
    } else {
        navbar.classList.remove('box-shadow')
    }
}

window.addEventListener('scroll', addBoxShadow)

var button1 = document.getElementById('button-for-login')
var button2 = document.getElementById('mobile-button')
var button3 = document.getElementById('button-for-login-2')

button1.onclick = () => {
    window.location.replace('/login')
}
button2.onclick = () => {
    window.location.replace('/login')
}
button3.onclick = () => {
    window.location.replace('/login')
}