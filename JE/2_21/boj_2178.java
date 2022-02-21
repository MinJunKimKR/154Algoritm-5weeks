import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_2178 {
    static int n, m;
    static int[][] map;
    static boolean[][] visit;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        visit = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = str.charAt(j) - '0';// 문자를 숫자로 바꾸기 위해
            }
        }
        Queue<Dot> q = new LinkedList<>();
        q.add(new Dot(0, 0));
        visit[0][0] = true;

        // bfs
        while (!q.isEmpty()) {
            Dot dot = q.poll();
            int x = dot.x;
            int y = dot.y;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (map[nx][ny] == 1 && !visit[nx][ny]) {
                        visit[nx][ny] = true;
                        map[nx][ny] = map[x][y] + 1;
                        q.add(new Dot(nx, ny));
                    }
                }
            }
        }

        System.out.println(map[n - 1][m - 1]);
    }

    static class Dot {
        int x;
        int y;

        public Dot(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
