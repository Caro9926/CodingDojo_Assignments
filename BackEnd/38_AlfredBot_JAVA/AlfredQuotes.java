import java.util.Date;
public class AlfredQuotes {
    
    public String basicGreeting() {
        // No necesitas codificar aquí, este es un método de ejemplo
        return "Hola, encantado de verte. ¿Cómo estás?";
    }
    
    public String guestGreeting(String name) {
        
        return  "Hola" + "" + name;
    }
    
    public String dateAnnouncement() {
        Date date = new Date();
        return "La fecha actual es:" + date;
    }
    
    public String respondBeforeAlexis(String conversation) {     
        
        if(conversation.indexOf("Alexis") > -1) {   
            System.out.println("De inmediato, señor. Ciertamente no es lo suficientemente sofisticada para eso");
        }
        if (conversation.indexOf("Alfred") >-1) {
            System.out.println("A su servicio. Como desee, naturalmente"); 
        }
        
        return  "Bien. Y con eso, me retiraré"; 
        
    }
    
    public String nuevoMetodo(String conversation) {     
        
        if(conversation.indexOf("Alexis") > -1) {   
            System.out.println("De inmediato, señor. Ciertamente no es lo suficientemente sofisticada para eso");
        }
        if (conversation.indexOf("Alfred") >-1) {
            System.out.println("A su servicio. Como desee, naturalmente"); 
        }
        
        return  "Bien. Y con eso, me retiraré"; 
        
    }
    
    public String nuevoMetodo() {
        Date date = new Date();
        return "La fecha actual es:" + date.getTime();

    }
	// BONUS NINJA
	// Ver las especificaciones para sobrecargar el método guessGreeting="comment from-rainbow">// BONUS SENSEI
    // ¡Escribe tu propio método AlfredQuotes usando cualquiera de los métodos String que has aprendido!
}
       
    