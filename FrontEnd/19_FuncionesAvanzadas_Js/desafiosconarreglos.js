// Función siempre Hambriento
function siempreHambriento(arr) {
    var comida = 0; 
    for(var i=0; i<arr.length; i++){
        if(arr[i] == "comida"){
            console.log("Delicioso");
            comida++; 
        }
    }
    if (comida==0) {
        console.log("Tengo hambre"); 
    }
    
}


siempreHambriento([3.14, "comida", "pastel", true, "comida"]);
siempreHambriento([4, 1, 5, 7, 2]);

//Cutoff

function highPass(arr, cutoff) {
    var filteredArr = [];
    for (var i=0; i< arr.length; i++){
        if (arr[i] > cutoff){
           filteredArr.push(arr[i]); 
        }
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // esperamos de vuelta [6, 8, 10, 9]

//Mejor que el promedio

function betterThanAverage(arr) {
    var sum = 0;
    for(var i=0; i<arr.length; i++) {
        sum += arr[i];
    }
    var promed = sum / arr.length;

    var count = 0; 
    
    for (var i=0; i< arr.length; i++){
        if (arr[i] > promed){
            count++; 
         }
    }

    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // esperamos 4 de vuelta

//Arreglos al revés
function reverse(arr) {
    var reverseArray = arr.reverse(); 
    return reverseArray;
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // esperamos de vuelta ["e", "d", "c", "b", "a"]

// Arreglo de Fibonacci


var i;
var fib = [];

fib[0] = 0;
fib[1] = 1;
function fibonacciArray(n){
    for (i = 2; i <= 10; i++) {
        fib[i] = fib[i - 2] + fib[i - 1];
      console.log(fib[i]);
    }
}

var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]