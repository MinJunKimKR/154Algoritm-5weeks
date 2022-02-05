import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2004 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        long n = Long.parseLong(st.nextToken());
        long m = Long.parseLong(st.nextToken());

        long count5 = five_fower_n(n) - five_fower_n(n - m) - five_fower_n(m);
        long count2 = two_fower_n(n) - two_fower_n(n - m) - two_fower_n(m);

        System.out.println(Math.min(count5,count2));
    }

    // 5의 승수를 구하는 함수
    static long five_fower_n(long num) {
        int count = 0;
        while (num >= 5) {
            count += (num / 5);
            num /= 5;
        }
        return count;
    }

    // 2의 승수를 구하는 함수
    static long two_fower_n(long num) {
        int count = 0;
        while (num >= 2) {
            count += (num / 2);
            num /= 2;
        }
        return count;
    }
}
