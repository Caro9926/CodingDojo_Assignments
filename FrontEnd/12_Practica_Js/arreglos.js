let nums = [10, 20, 30, 40, 50];
        //  0   1   2   3   4    i < 5
/*
        console.log( nums );
console.log( nums[2] );
nums[2] = 60;
console.log( nums );
console.log( nums.length );
*/

console.log( nums );
// Agregar elemento al final del arreglo
nums.push( 70 );
console.log( nums );

// Eliminar elemento del final del arreglo
nums.pop();
console.log( nums );

// Agregar elemento al principio del arreglo
nums.unshift( 1 );
console.log( nums );

// Eliminar elemento del principio del arreglo
nums.shift();
console.log( nums );

// Elminar o agregar en cualquier indice del arreglo
nums.splice( 3, 0, 35 ); // El primer número es el indice con el queremos trabajar
//Cuántos quiero eliminar, pongo 0 porque quiero agregar 35 y el tercero es lo que quiero
console.log( nums );

nums.splice( 2, 2 );
console.log( nums );

/*
for( let i = 0; i < nums.length; i ++ ){
    console.log( nums[i] );
}
*/

