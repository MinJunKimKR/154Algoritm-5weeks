import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_4963 {
    static int cnt;
    static int[] dx = {-1, 1, 0, 0, -1, 1, 1, -1};
    static int[] dy = {0, 0, -1, 1, 1, 1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        while (true) {
            int[][] map = new int[h][w];
            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < w; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }


            cnt = 0;
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (map[i][j] == 1) {
                        cnt++;
//                        bfs(i, j, w, h, map);
                        dfs(i, j, w, h, map);
                    }
                }
            }
            sb.append(cnt).append('\n');

            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            if (w == 0 && h == 0)
                break;

        }
        System.out.println(sb);

    }

    static void dfs(int x, int y, int w, int h, int[][] map) {
        map[x][y] = 0;
        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < h && ny >= 0 && ny < w) {
                if (map[nx][ny] == 1) {
                    dfs(nx, ny, w, h, map);
                }
            }
        }

    }

    static void bfs(int x, int y, int w, int h, int[][] map) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        while (!q.isEmpty()) {
            x = q.peek()[0];
            y = q.peek()[1];
            q.poll();
            for (int i = 0; i < 8; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < h && ny >= 0 && ny < w) {
                    if (map[nx][ny] == 1) {
                        q.add(new int[]{nx, ny});
                        map[nx][ny] = 0;
                    }
                }

            }
        }

    }

}
