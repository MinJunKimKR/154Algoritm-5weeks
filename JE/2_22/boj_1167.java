import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj_1167 {
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
    static int node, v;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        v = Integer.parseInt(br.readLine());

        list = new ArrayList[v + 1];
        for (int i = 1; i <= v; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < v; i++) {
            st = new StringTokenizer(br.readLine());

            int nodenum = Integer.parseInt(st.nextToken());

            String str;
            while (!(str = st.nextToken()).equals("-1")) {
                int node = Integer.parseInt(str);
                int dist = Integer.parseInt(st.nextToken());
                list[nodenum].add(new Node(node, dist));
            }
        }

        visit = new boolean[v + 1];
        dfs(1, 0);

        visit = new boolean[v + 1];
        dfs(node, 0);

        System.out.println(max);
    }

    static void dfs(int v, int len) {
        if (len > max) {
            max = len;
            node = v;
        }

        visit[v] = true;

        for (Node n : list[v]) {
            if (!visit[n.node]) {
                visit[n.node] = true;
                dfs(n.node, n.dist + len);
            }
        }
    }
}