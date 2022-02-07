import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Math.sqrt;

public class boj_1978 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int count = 0;
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());

            if (isPrime(num)) count++;

        }

        System.out.println(count);

    }

    public static boolean isPrime(int n) {
        if (n == 1) return false;

        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) return false;
        }

        return true;
    }
}
