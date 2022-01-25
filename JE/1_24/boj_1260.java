import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_1260 {
    public static boolean[] visited;
    public static int[][] arr;
    public static int n, m, v;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        arr = new int[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st2.nextToken());
            int b = Integer.parseInt(st2.nextToken());
            arr[a][b] = 1;
            arr[b][a] = 1;
        }

        visited = new boolean[n + 1];
        dfs(v);

        System.out.println();

        visited = new boolean[n + 1];
        bfs(v);


    }

    public static void dfs(int start) {
        visited[start] = true;

        System.out.print(start + " ");

        for (int i = 1; i <= n; i++) {
            if (arr[start][i] == 1 && visited[i] == false) {
                dfs(i);
            }
        }
    }

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();

        q.add(start);
        visited[start] = true;
        System.out.print(start + " ");

        while (!q.isEmpty()) {
            int temp = q.poll();

            for (int i = 1; i <= n; i++) {
                if (arr[temp][i] == 1 && visited[i] == false) {
                    q.add(i);
                    visited[i] = true;
                    System.out.print(i + " ");
                }
            }
        }
    }
}
