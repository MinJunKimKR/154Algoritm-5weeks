import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_9613 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            String[] arr = br.readLine().split(" ");
            int n = Integer.parseInt(arr[0]);
            int count = 0;

            for (int i = 1; i <= n - 1; i++) {
                for (int j = i + 1; j <= n; j++) {
                    int a = Integer.parseInt(arr[i]);
                    int b = Integer.parseInt(arr[j]);
                    count += gcd(a, b);
//                    count += gcd(Math.max(a, b), Math.min(a, b));
                }
            }
            System.out.println(count);
        }
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
