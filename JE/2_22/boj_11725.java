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

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 주어진 값 저장
        n = Integer.parseInt(st.nextToken());
        ArrayList<Integer>[] graph = new ArrayList[n + 1];
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

        // bfs를 통해 트리 순회하여 부모찾기
        parent = new int[n + 1];
        visit = new boolean[n + 1];
        Queue<Integer> q = new LinkedList<>();

        q.offer(1);
        visit[1] = true;
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : graph[u]) {
                if (!visit[v]) {
                    // 아직 미방문한 각노드를 다음 탐색대상에 넣고
                    // 각 노드의 부모를 현재 노드로 지정
                    q.offer(v);
                    visit[v] = true;
                    parent[v] = u;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= n; i++) {
            sb.append(parent[i]).append("\n");
        }
        System.out.println(sb);
    }

}
