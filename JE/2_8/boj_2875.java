import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2875 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int max = 0;
        for (int i = 0; i <= k; i++) {
            int woman = n - i;
            int man = m - (k - i);

            if (woman / 2 >= man) {
                max = Math.max(man, max);
            } else {
                max = Math.max(woman / 2, max);
            }


        }
        System.out.println(max);
    }
}
