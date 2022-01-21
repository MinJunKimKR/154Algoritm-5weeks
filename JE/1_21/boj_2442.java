import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_2442 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < i + k; j++) {
                System.out.print("*");
            }
            k++;
            System.out.println();

        }
    }
}
