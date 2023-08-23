const side_menu = document.querySelectorAll('#sidebar .side-bar-menu li a')

side_menu.forEach(item => {
    const li = item.parentElement;
    item.addEventListener('click', function(){
        side_menu.forEach(i=> {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    });
});


const menuBar = document.querySelector('#body nav .bx.bx-menu');
const sideBar = document.getElementById('sidebar')

menuBar.addEventListener('click', function () {
    var brand = document.getElementById('branded')
    brand.classList.toggle('branded');
    sideBar.classList.toggle('hide');
    var brand = document.getElementById('brand')
    if (brand.innerHTML == "C") {
        brand.textContent = "Captiosus"
    }else {
        brand.textContent = "C"
    }
})

if (window.innerWidth < 768)     {
    sideBar.classList.add('hide')
    if (brand.innerHTML == "C") {
        brand.textContent = "Captiosus"
    }else {
        brand.classList.toggle('branded')
        brand.textContent = "C"
    }
}