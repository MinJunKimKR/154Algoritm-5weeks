
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_9095 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        int[] dp = new int[11]; // 혹시 모를 컴파일 에러 방지
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());

            for (int i = 4; i <= n; i++) {
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
            }
            System.out.println(dp[n]);
        }
    }
}
