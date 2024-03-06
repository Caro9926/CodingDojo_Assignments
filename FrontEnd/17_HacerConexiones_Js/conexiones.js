var element = document.querySelector("#name"); 

console.log(element);


function b1(element) {
    element.innerText ="Frank Sinatra";
    console.log(element); 

}

var solicitud = document.querySelector("#solicitud");
var listamigos = document.querySelector("#amigos");

function rechazar(id) {
    var element = document.querySelector(id);
    element.remove();
    solicitud.innerText--;
}


function aceptar(id) {
    var element = document.querySelector(id);
    element.remove();
    solicitud.innerText--;
    listamigos.innerText++;
}


