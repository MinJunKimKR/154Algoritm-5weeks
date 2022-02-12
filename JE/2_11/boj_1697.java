
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_1697 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());


        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] check = new int[100001];

        if (n == k) {
            System.out.println(0);
            return;
        }

        bfs(check, n, k);

        System.out.println(check[k]);

    }


    static void bfs(int[] check, int x, int k) {
        Queue<Integer> q = new LinkedList<>();

        q.offer(x);
        check[x] = 0;

        while (!q.isEmpty()) {
            int n = q.poll();

            if (check[k] != 0) break;

            //if(n+1 >=check.length || n-1<0 || n*2 >= check.length) continue;

            if (n + 1 < check.length && check[n + 1] == 0) {
                check[n + 1] = check[n] + 1;
                q.offer(n + 1);
            }
            if (n - 1 >= 0 && check[n - 1] == 0) {
                check[n - 1] = check[n] + 1;
                q.offer(n - 1);
            }
            if (n * 2 < check.length && check[n * 2] == 0) {
                check[n * 2] = check[n] + 1;
                q.offer(n * 2);
            }

        }
    }

}