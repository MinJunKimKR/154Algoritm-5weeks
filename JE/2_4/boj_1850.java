import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1850 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        Long a = Long.parseLong(st.nextToken());
        Long b = Long.parseLong(st.nextToken());

        Long n = gcd(Math.max(a, b), Math.min(a, b));

        for (int i = 0; i < n; i++) {
            sb.append(1);
        }
        System.out.println(sb);
    }

    public static Long gcd(Long a, Long b) {
        while (b != 0) {
            Long temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
