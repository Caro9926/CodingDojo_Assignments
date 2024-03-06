import java.util.Date;
import java.util.ArrayList;
import java.util.Arrays;
import java. util. Scanner;
public class CafeUtil {
    
    public String basicGreeting() {
        // No necesitas codificar aquí, este es un método de ejemplo
        return "Hola, encantado de verte. ¿Cómo estás?";
    }
    
    
    public int getStreakGoal(){
        int suma =0; 
        for(int k=0; k<=10; k++){
          suma = suma+k; 
        }
    return suma; 
    }

    public double getOrderTotal(double[] arr){
        double sum = 0;
        //double arr[] = {};
        for (int i = 0; i < arr.length; i++) {
            sum= sum + arr[i];
        }
        return sum; 
        
    }

    public static void displayMenu(ArrayList<String> numeros){
                     
        for( int i = 0; i < numeros.size(); i ++ ){
            System.out.println( i + " " + numeros.get(i) );
        }
         
        
    }  
   
    public static void addCustomer(ArrayList<String> customers){
        
        System.out.print("Please write your name: ");  
        Scanner input = new Scanner(System.in); 
        String name = input.nextLine();              //reads string   
        System.out.println( "Hello " + name + "!");
        System.out.println("There are " + customers.size() + " people ahead of you");
        customers.add(name);
        System.out.println(Arrays.toString(customers.toArray()));
    }

    
    

}  

    
      
