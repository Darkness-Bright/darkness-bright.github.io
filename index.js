function dark(){localStorage.setItem("theme", "dark");document.body.classList.remove("light");document.body.classList.add("dark");document.querySelector(".theme").setAttribute("name","sunny");}
function light(){localStorage.setItem("theme", "light");document.body.classList.remove("dark");document.body.classList.add("light");document.querySelector(".theme").setAttribute("name","moon");}

if(localStorage.getItem("theme")==="light"){light();}else{dark();}

function theme(){if(localStorage.getItem("theme")==="dark"){light();}else{dark();}document.querySelector(".theme").classList.toggle("rotated");}

function nav() {
  document.getElementById("nav").classList.toggle("full");
  document.querySelector(".line-1").classList.toggle("bent-1");
  document.querySelector(".line-2").classList.toggle("bent-2");
  document.querySelector("body").classList.toggle("overflow-hidden");
  var all = document.getElementsByClassName("nav-link");
  for (var i = 0; i < all.length; i++) {
    all[i].classList.toggle("link-show");
    all[i].addEventListener("click", nav);
  }
}
