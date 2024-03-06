function pizzaDojo( tipoCorteza, tipoSalsa, quesos, salsas) {
    var pizza = {};
    pizza.tipoCorteza = tipoCorteza;
    pizza.tipoSalsa = tipoSalsa;
    pizza.quesos = quesos;
    pizza.salsas = salsas;

    return pizza;
}



var p1 = pizzaDojo("estilo Chicago", "tradicional",  ["mozzarella"], ["pepperoni", "salchicha"]);
var p2 = pizzaDojo("lanzada a mano", "marinara",  ["mozzarella", "feta"], ["champiñones", "aceitunas", "cebollas"]);
var p3 = pizzaDojo("gruesa siciliana", "picante",  ["mozzarella", "feta", "fresco"], [ "chorizo", "ají"]);
var p4 = pizzaDojo("gruesa tradicional", "marinara",  ["cheddar",  "fresco"], [ "chorizo", "piña", "durazno"]);





console.log(p1);
console.log(p2);
console.log(p3);
console.log(p4);



var pizzas = [p1, p2, p3, p4];
var p5 = pizzas[Math.floor(Math.random() * pizzas.length)];
console.log(p5); 


