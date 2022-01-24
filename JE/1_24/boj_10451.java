import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_10451 {
    static int[] arr;
    static boolean[] visit;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());

            arr = new int[n + 1];
            count = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            visit = new boolean[n + 1];
            for (int i = 1; i <= n; i++) {
                if (!visit[i]) {
                    dfs(i);
                    count++;
                }
            }
            System.out.println(count);
        }
    }

    public static void dfs(int start) {
        visit[start] = true;

        int next = arr[start];
        if (!visit[next]) {
            dfs(next);
        }
    }
}
