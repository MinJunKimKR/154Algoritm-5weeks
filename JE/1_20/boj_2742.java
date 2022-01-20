import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_2742 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = n; i >= 1; i--) {
            System.out.println(i);
        }
    }
}
