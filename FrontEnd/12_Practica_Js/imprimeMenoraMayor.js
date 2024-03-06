let a = 4
let b = 7
let c = 1

if( a<b ){
    if (a<c){
        console.log( a );
        if (b < c){
            console.log(b);
            console.log(c);
        }
        else{
        console.log(c);
        console.log(b);    
     }
    }
    else {
        console.log(c);
        console.log(b);
        console.log(a);
        }
}
else{
    if( b<c ){
        console.log(b);
    if (a<c) {
        console.log(a);
        console.log(c);
    }
    else{
        console.log( c );
        console.log( a );
    }
}
else{
    console.log( c );
    console.log( b );
    console.log( a );
    }
}