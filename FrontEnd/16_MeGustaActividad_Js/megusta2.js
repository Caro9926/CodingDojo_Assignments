var likes = [9, 12, 9];
var  boton= [
    document.querySelector("#l1"),
    document.querySelector("#l2"),
    document.querySelector("#l3")
];


function add1(id) {
    likes[id]++;
    boton[id].innerHTML = likes[id] + " like(s)";
}

