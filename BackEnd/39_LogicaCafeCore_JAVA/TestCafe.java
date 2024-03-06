import java.util.ArrayList;
import java.util.Arrays;
import java. util. Scanner;
public class TestCafe {
    public static void main(String[] args) {
        CafeUtil CafeUtilCore = new CafeUtil();  // Crea una instancia de CafeUtil para acceder a todos tus métodos  
        
         	
        /* ============ Casos de prueba de la App ============= */
    
        System.out.println("\n----- Prueba Meta café -----");
        int resultado = CafeUtilCore.getStreakGoal();
        System.out.printf("Compras necesarias para la semana 10:" + resultado);
    
        System.out.println("----- Prueba Total Orden -----");
        double[] lineItems = {3.5, 1.5, 4.0, 4.5};
        double resultado2 = CafeUtilCore.getOrderTotal(lineItems);
        //System.out.printf("Total orden:" + resultado2 );
        System.out.printf("Total orden: %s \n\n",CafeUtilCore.getOrderTotal(lineItems));
        
        System.out.println("----- Prueba Mostrar Menú-----");
        
        ArrayList<String> menu = new ArrayList<String>();
        menu.add("café de goteo");
        menu.add("capuchino");
        menu.add("latte");
        menu.add("moka");
        CafeUtilCore.displayMenu(menu);
    
        System.out.println("\n----- Prueba agregar cliente-----");
        ArrayList<String> customers = new ArrayList<String>();
        //--- Probar 4 veces ---
        for (int i = 0; i < 2; i++) {
             CafeUtilCore.addCustomer(customers);
             System.out.println("\n");
        }
    
      
    }

   

} 