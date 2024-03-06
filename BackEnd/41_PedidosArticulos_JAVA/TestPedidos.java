import java.util.ArrayList;
public class TestPedidos {
    public static void main(String[] args) {

        String saludoGeneral = "Bienvenido al Café Java, ";
        String mensajePendiente = ", tu pedido estará listo en breve";
        String mensajeListo = ", tu pedido está listo";
        String mensajeMostrarTotal = "Tu total es $";
    
        // Elementos del menú
        
        Articulos articulo1 = new Articulos("Moka", 16.3);
        Articulos articulo2 = new Articulos("Latte", 18.5);
        Articulos articulo3 = new Articulos("Café de goteo", 6.5);
        Articulos articulo4 = new Articulos("Capuchino", 10.8);
        
        //Pedidos sin nombre
        Pedido pedido1 = new Pedido();
        Pedido pedido2 = new Pedido();
        //Pedidos con nombre
        Pedido pedido3 = new Pedido("Alex");
        Pedido pedido4 = new Pedido("Caro");
        Pedido pedido5 = new Pedido("Helen");
        
        pedido1.addItem(articulo1);
        pedido1.addItem(articulo2);
        pedido1.addItem(articulo3);

        pedido2.addItem(articulo2);
        pedido2.addItem(articulo3);
        pedido2.addItem(articulo4);

        pedido3.addItem(articulo3);
        pedido3.addItem(articulo4);
        pedido3.addItem(articulo1);

        pedido4.addItem(articulo4);
        pedido4.addItem(articulo1);
        pedido4.addItem(articulo2);
        
        pedido1.display();
        pedido2.display();
        pedido3.display();
        pedido4.display();
        pedido5.display();

        pedido5.setListo(true);      
        pedido1.setListo(true);

        System.out.println(pedido4.getStatusMessage());
        System.out.println(pedido1.getStatusMessage());
    
        
    
        
   

       

    }
}

    