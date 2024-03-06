public class CafeJava {
    public static void main(String[] args) {
        // VARIABLES DE LA APP
        // Líneas de texto que aparecerán en la app 
        String saludoGeneral = "Bienvenido al Café Java, ";
        String mensajePendiente = ", tu pedido estará listo en breve";
        String mensajeListo = ", tu pedido está listo";
        String mensajeMostrarTotal = "Tu total es $";
        
        // Variables de menú (agrega las tuyas a continuación)
        double precioMocha = 3.5;
        double precioFiltro = 4.5; 
        double precioLeche = 5.9;
        double precioCapuchino = 6.9;
    
        // Variables de nombre de cliente (agrega las tuyas a continuación)
        String cliente1 = "Cindhuri";
        String cliente2 = "Sam"; 
        String cliente3 = "Jimmy"; 
        String cliente4 = "Noah"; 
    
        // Finalizaciones de pedidos (agrega las tuyas a continuación)
        boolean estaListoOrden1 = false;
        boolean estaListoOrden2 = true; 
        boolean estaListoOrden3 = false;
        boolean estaListoOrden4 = true; 


           
        // SIMULACIÓN DE INTERACCIÓN DE APP(Agrega tu código para los desafíos a continuación)
        // Ejemplo:
        System.out.println(saludoGeneral + cliente1); // Muestra "Bienvenido a Café Java, Cindhuri"
    	// ** Las sentencias print sobre las interacciones con el cliente irán aquí ** //
        System.out.println("Hola"+ "" + cliente1 + mensajePendiente );  //Cindhuri pide un café

        if(estaListoOrden4) {   //Noah pedido de café
            System.out.println(cliente4 + mensajeListo);
            System.out.println(mensajeMostrarTotal + precioCapuchino); 
        }
        else {
            System.out.println(cliente4 + mensajePendiente);
        }
       
        if(estaListoOrden2) { //Sam pidió dos cafés con leche
            System.out.println(cliente4 + mensajeListo);
            System.out.println(mensajeMostrarTotal + precioCapuchino); 
        }
        else {
            System.out.println(cliente4 + mensajePendiente);
        }

        System.out.println(mensajeMostrarTotal + (precioLeche * 2) );

        System.out.println(mensajeMostrarTotal + (precioCapuchino - precioLeche));

        


    }
}