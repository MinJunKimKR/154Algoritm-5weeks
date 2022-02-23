import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj_1967 {
    static class Node {
        int node, dist;

        public Node(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }

    static ArrayList<Node>[] list;
    static boolean[] visit;
    static int max = 0;
    static int n;
    static int maxIdx = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        list = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());

            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            list[parent].add(new Node(child, weight));
            list[child].add(new Node(parent, weight));
        }

        visit = new boolean[n + 1];
        visit[1] = true;
        dfs(1, 0);

        visit = new boolean[n + 1];
        visit[maxIdx] = true;
        dfs(maxIdx, 0);
        System.out.println(max);

    }

    static void dfs(int idx, int dist) {
        if (max < dist) {
            max = dist;
            maxIdx = idx;
        }
        for (Node n : list[idx]) {
            if (!visit[n.node]) {
                visit[n.node] = true;
                dfs(n.node, dist + n.dist);
            }
        }
    }
}