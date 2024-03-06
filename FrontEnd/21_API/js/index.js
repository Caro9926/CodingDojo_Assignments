function buscadorDeImagenesDePerritos( event ){
    event.preventDefault();
    let cantidad = document.querySelector( '#cantidad' ).value;
    let url = `https://dog.ceo/api/breeds/image/random/${cantidad}`;

    let config = {
        method : "GET"
    };

    //En este api no especifican las configuraciones, puede ser un token. 
    // FETCH obtener información del API
    // Es asíncrona porque nos permite obtener información 
    fetch( url, config )  //Nos pide dos parámetros,url obligatorio y luego las congifuraciones en el api 
        .then( function( respuesta ){ // Después de que me llega la respuesta (then)
            console.log( respuesta );
            if( respuesta.ok ){   //El ok es parte de la estructura
                return respuesta.json(); //Objeto de respuesta
            }
            else{
                throw Error( "El sitio no fue encontrado 404" + respuesta.statusText );
            }
        })
        .then( function( respuestaJSON ){
            console.log( respuestaJSON );
            let resultados = document.querySelector( '.resultados' );
            resultados.innerHTML = "";

            for( let i = 0; i < respuestaJSON.message.length; i ++ ){
                resultados.innerHTML += `<div>
                                            <img src="${respuestaJSON.message[i]}" alt="Imagen de un perrito" />
                                         </div>`;
            }
        })
        .catch( function( error ){
            let resultados = document.querySelector( '.resultados' );
            resultados.innerHTML = error;
        });

    console.log( "Esto se imprime primero!!!" );

}

//Forma más rápida
async function buscadorDeImagenesDePerritosAsync( event ){
    event.preventDefault();
    let cantidad = document.querySelector( '#cantidad' ).value;
    let url = `https://dog.ceo/api/breeds/image/random/${cantidad}`;

    let config = {
        method : "GET"
    };
    try{
        let respuesta = await fetch( url, config );
        if( respuesta.ok ){
            let respuestaJSON = await respuesta.json();
            let resultados = document.querySelector( '.resultados' );
            resultados.innerHTML = "";

            for( let i = 0; i < respuestaJSON.message.length; i ++ ){
                resultados.innerHTML += `<div>
                                            <img src="${respuestaJSON.message[i]}" alt="Imagen de un perrito" />
                                            </div>`;
            }
        }
        else{
            throw Error( "El sitio no fue encontrado 404" + respuesta.statusText );
        }
    }
    catch( error ){
        let resultados = document.querySelector( '.resultados' );
            resultados.innerHTML = error;
    }

}

let dogForm = document.querySelector( '.dogForm' );
dogForm.addEventListener( 'submit', buscadorDeImagenesDePerritosAsync );