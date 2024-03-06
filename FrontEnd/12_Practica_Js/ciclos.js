let i = 1;  // Variable de control 1
while( i <= 10 ){  // Condición 2
    console.log( i );  // Instrucciones dentro del ciclo 3
    // i = i + 1;
    i ++;    // Actualiza variable de control 4. Si no actualizo mi var de control correrá indefinidamente 
    // i += 1;
}

for( let i = 1; i <= 10; i ++ ){  //let i es 1, i<=10 es la condición, 3 es console log y 4 es la actualización
    console.log( i );
}

let j = 1; //1
do{
    console.log( j ); // 2
    j ++; // 3
}
while( j <= 10 ); //4 