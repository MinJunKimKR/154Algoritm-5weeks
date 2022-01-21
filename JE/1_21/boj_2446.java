import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_2446 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int k = n * 2 - 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < k; j++) {
                System.out.print("*");
            }
            k -= 2;
            System.out.println();
        }
        k += 2;
        for (int i = n - 1; i > 0; i--) {
            k += 2;
            for (int j = 1; j < i; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < k; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
