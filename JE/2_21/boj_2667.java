import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class boj_2667 {
    static int[][] map;
    static int n;
    static int cnt;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        map = new int[n][n];
        PriorityQueue<Integer> que = new PriorityQueue<>();

        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = str.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1) {
                    cnt = 0;
                    dfs(i, j);
//                    bfs(i, j);
                    que.add(cnt);


                }
            }
        }

        System.out.println(que.size());
        while (!que.isEmpty()) {
            System.out.println(que.poll());
        }

    }

    static void bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        map[x][y] = 0;
        cnt++;
        while (!q.isEmpty()) {
            x = q.peek()[0];
            y = q.peek()[1];
            q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    if (map[nx][ny] == 1) {
                        map[nx][ny] = 0;
                        q.add(new int[]{nx, ny});
                        cnt++;
                    }
                }
            }
        }
    }

    static void dfs(int x, int y) {
        map[x][y] = 0;
        cnt++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                if (map[nx][ny] == 1) {
                    dfs(nx, ny);
                }
            }
        }

    }


}