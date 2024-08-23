const openBtn = document.querySelector('.open-btn');
const closeBtn = document.querySelector('.close-btn');
const offcanvasMenu = document.querySelector('.offcanvas-menu');
openBtn.addEventListener('click',function(e){
    e.preventDefault()
    console.log(offcanvasMenu) 
    console.log(openBtn)
    offcanvasMenu.classList.add('active');
});
closeBtn.addEventListener('click',function (e){
    e.preventDefault();
    offcanvasMenu.classList.remove('active');
});

// book

let newbook = document.getElementById("new-book");
let newbookinstance = document.getElementById("new-book-instance");
let form1 = document.getElementById("form-1");
let form2 = document.getElementById("form-2");

newbook.onclick = function () {
    form1.style.display = "block";
    form2.style.display = "none";
}

newbookinstance.onclick = function () {
    form1.style.display = "none";
    form2.style.display = "block";
}


