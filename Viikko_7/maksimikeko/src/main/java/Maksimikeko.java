
import java.util.Collections;
import java.util.PriorityQueue;


/**
 *
 * @author Syke-409
 */
public class Maksimikeko {
    public static void main(String[] args) {
        PriorityQueue<Integer> jono = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 1; i <= 10; ++i) {
            jono.add(i);
        }
        System.out.println("Jono lisäysten jälkeen: " + jono);
        for(int i = 0; i < 3; ++i) {
            jono.poll();
        }
        System.out.println("Jono poistojen jälkeen: " + jono);
    }
}
