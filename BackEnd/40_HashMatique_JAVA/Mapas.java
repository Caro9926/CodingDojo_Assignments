import java.util.HashMap;
import java.util.Set;
import java.util.Collection;

public class Mapas{
    public static void main( String args[] ){
        HashMap<Integer, String> listSongs = new HashMap<Integer, String>();
        listSongs.put( 1, "Shape of you" );
        listSongs.put( 2, "Let it be" );
        listSongs.put( 3, "Don't stop me now" );
        listSongs.put( 4, "I will survive" );

        System.out.println( listSongs.get( 1 ) ); //Extraer la canción por su título

        
        Set<Integer> setIds = listSongs.keySet();
        Collection<String> colleccionSongs = listSongs.values();
       
        for( Integer llave : setIds ){
            System.out.println( llave );
            System.out.println( listSongs.get( llave ) );
        }

    }
}