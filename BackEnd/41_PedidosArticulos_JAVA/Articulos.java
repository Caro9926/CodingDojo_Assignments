
public class Articulos{
    private String nombre;
    private double price;


    public Articulos(){
        this.nombre = "N/A";
        this.price = -1;
        
    }
    
    //Constructor
    public Articulos( String nombre, double price){
        this.nombre = nombre;
        this.price = price;
      
    }

    public String getNombre(){
        return this.nombre;
    }

    public double getPrice(){
        return this.price;
    }

   
    public void setNombre( String nombre ){
        this.nombre = nombre;
    }

    public void setPrice( double price ){
        this.price = price;
    }

    


    
}
