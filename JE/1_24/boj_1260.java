import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_1260 {
    static int n, m, v;
    static boolean[] visit;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        map = new int[n + 1][n + 1];

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map[a][b] = 1;
            map[b][a] = 1;
        }

        visit = new boolean[n + 1];
        dfs(v);

        System.out.println();

        visit = new boolean[n + 1];
        bfs(v);
    }

    static void dfs(int start) {
        System.out.print(start + " ");
        visit[start] = true;
        for (int i = 1; i < n + 1; i++) {
            if (map[start][i] == 1 && !visit[i]) {
                dfs(i);
            }
        }
    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        visit[v] = true;
        System.out.print(v + " ");
        q.add(start);
        while (!q.isEmpty()) {
            int tmp = q.poll();
            for (int i = 1; i < n + 1; i++) {
                if (map[tmp][i] == 1 && !visit[i]) {
                    System.out.print(i + " ");
                    q.add(i);
                    visit[i] = true;
                }
            }
        }
    }
}