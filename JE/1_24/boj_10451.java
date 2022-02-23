import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_10451 {
    static int n;
    static boolean[] visited;
    static int[] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            n = Integer.parseInt(br.readLine());
            map = new int[n + 1];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i < n + 1; i++) {
                map[i] = Integer.parseInt(st.nextToken());
            }

            visited = new boolean[n + 1];

            int cnt = 0;
            for (int i = 1; i < n + 1; i++) {
                if (!visited[i]) {
                    bfs(i);
                    cnt++;
                }
            }
            System.out.println(cnt);
        }

    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            start = q.poll();
            int next = map[start];
            if (!visited[next]) {
                q.add(next);
                visited[next] = true;
            }
        }
    }

    static void dfs(int start) {
        visited[start] = true;
        int next = map[start];
        if (!visited[next]) {
            dfs(next);
        }
    }
}