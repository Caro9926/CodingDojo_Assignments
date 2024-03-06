function sumaDosNumeros( num1, num2 ){ //Tener código para reutilizarlo
    let resultado = num1 + num2;
    return resultado;
}

function restaDosNumeros( num1, num2 ){
    let resultado = num1 - num2;
    return resultado;
}

function imprimeHola(){
    console.log( "¡Hola como estan!");
}

function imprimerArreglo( arr ){
    for( let i = 0; i < arr.length; i ++ ){
        console.log( arr[i] );
    }
}

let res = sumaDosNumeros( 20, 30 );
console.log( res );

let res2 = sumaDosNumeros( 80, 100 );
console.log( res2 );

let x = 1;
let y = 2;

let res3 = sumaDosNumeros( x, y );
console.log( res3 );

imprimeHola();
imprimeHola();
imprimeHola();

let nums = [10, 20, 30, 40, 50];
imprimerArreglo( nums );
let nombres = ["Alex", "Martha", "Roger", "Alan"];
imprimerArreglo( nombres );