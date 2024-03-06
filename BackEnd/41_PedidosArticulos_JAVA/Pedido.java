import java.util.ArrayList;
import java.text.MessageFormat;
import java.text.NumberFormat;

public class Pedido{
    private String nombre; 
    private boolean listo; 
    private ArrayList<Articulos> items = new ArrayList<Articulos>(); //Aquí le agrego la clase del tipo de artículos

   //Constructor
    public Pedido(){
            this.nombre = "Invitado";
            this.items = new ArrayList<Articulos>();  
    }
   
        
    public Pedido(String nombre) {
        this.nombre = nombre;
    }

    //Gets and setters
    public String getNombre(){
        return this.nombre;
    }

    public boolean getListo(){
        return this.listo;
    }

    public ArrayList<Articulos> getItems(){
        return this.items;
    }

   
    public void setNombre( String nombre ){
        this.nombre = nombre;
    }

    public void setListo( boolean listo ){
        this.listo = listo;
    }

    public void setItems( ArrayList<Articulos> items ){
        this.items = items;
    }
    
    public void addItem(Articulos item) {
        this.items.add(item);
    }

    public double getPedidoTotal() {
        double total = 0.0;

        for (Articulos items : this.getItems()) {
            total += items.getPrice();
        }

        return total;
    }

    public String getStatusMessage() {
        String message = MessageFormat.format("Gracias por esperar, {0}. ¡Tu orden estará lista pronto!", this.getNombre());

        if (this.getListo()) {
            message = MessageFormat.format("¡Tu orden está lista, {0}!", this.getNombre());
        }

        return message;
    }
    
    

    public void display() {
        System.out.println(MessageFormat.format("Nombre de Cliente: {0}", this.getNombre()));

        

        for (Articulos items : this.getItems()) {
            System.out.println(MessageFormat.format("{0}: {1}", items.getNombre(), items.getPrice()));
        }

        System.out.println(MessageFormat.format("Total: {0}", this.getPedidoTotal()));
        System.out.println("---------------------------- \n");
    }


    



}