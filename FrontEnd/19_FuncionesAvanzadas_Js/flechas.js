/* 
function nombreFuncion (){ //Forma antigua 

}

let nombreFuncion = (num1, num2) => {  //Forma nueva de codificar

}
*/

function sumadosNumeros ( num1, num2 ){
    let resultado = num1 + num2; 
    return num1 + num2; 

}

let sumadosNumerosFlecha = (num1, num2) => num1 + num2; 

let res1 = sumadosNumeros(20, 30);
let res2 = sumadosNumerosFlecha (20, 30);

console.log (res1, res2); 

let imprimeHola = nombre => console.log ("Hola", nombre);

imprimeHola("Alex"); 
