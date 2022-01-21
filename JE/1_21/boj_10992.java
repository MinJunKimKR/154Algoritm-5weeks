import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_10992 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 첫줄
        for (int i = 1; i < n; i++) {
            System.out.print(" ");
        }
        System.out.println("*");

        // 중간줄
        for (int i = 2; i < n; i++) {
            for (int j = n - i; j > 0; j--) { // 앞공백
                System.out.print(" ");
            }
            System.out.print("*");
            for (int j = 1; j <= 2 * (i - 1) - 1; j++) { // 가운데 공백
                System.out.print(" ");
            }
            System.out.println("*");
        }

        // 막줄 (n=1일 때 출력하지않음)
        if (n != 1) {
            for (int i = 1; i <= 2 * n - 1; i++) {
                System.out.print("*");
            }
            System.out.println();
        }


    }
}