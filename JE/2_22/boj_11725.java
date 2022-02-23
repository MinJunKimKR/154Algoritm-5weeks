import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_11725 {
    static int n;
    static int[] parent;
    static boolean[] visit;
    static ArrayList<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        parent = new int[n + 1];
        visit = new boolean[n + 1];

        //bfs(1);
        dfs(1);

        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= n; i++) {
            sb.append(parent[i]).append("\n");
        }
        System.out.println(sb);
    }

    static void bfs(int u) {
        Queue<Integer> q = new LinkedList<>();
        q.add(u);
        visit[u] = true;
        while (!q.isEmpty()) {
            u = q.poll();
            for (int v : graph[u]) {
                if (!visit[v]) {
                    q.add(v);
                    visit[v] = true;
                    parent[v] = u;
                }
            }
        }
    }

    static void dfs(int u) {
        visit[u] = true;
        for (int v : graph[u]) {
            if (!visit[v]) {
                parent[v] = u;
                dfs(v);
            }
        }
    }
}