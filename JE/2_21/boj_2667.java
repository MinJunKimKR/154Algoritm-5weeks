import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class boj_2667 {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int cntDfs; // dfs에서 필요

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = str.charAt(j) - '0';//문자 '숫자'에서 -'숫자'를 해야 숫자가 됨
            }
        }

        PriorityQueue<Integer> q = new PriorityQueue<>(); // 오름차순이므로 우선순위 큐 선언

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1) {
                    // bfs
//                    q.add(bfs(n, i, j, map));
                    // dfs
                    cntDfs = 0;// cnt 0으로 초기화
                    dfs(n, i, j, map);
                    q.add(cntDfs);
                }
            }
        }

        System.out.println(q.size());
        while (!q.isEmpty()) {
            System.out.println(q.poll());
        }
    }

    static int bfs(int n, int x, int y, int[][] map) {
        Queue<int[]> que = new LinkedList<>();
        int cnt = 0;
        que.add(new int[]{x, y});
        map[x][y] = 0;

        while (!que.isEmpty()) {
            x = que.peek()[0];
            y = que.peek()[1];
            que.poll();
            cnt++; // 갯수 증가
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    if (map[nx][ny] == 1) {
                        que.add(new int[]{nx, ny});
                        map[nx][ny] = 0;

                    }
                }
            }
        }
        return cnt;
    }

    static void dfs(int n, int x, int y, int[][] map) {
        map[x][y] = 0;
        cntDfs++;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                if (map[nx][ny] == 1)
                    dfs(n, nx, ny, map);
            }
        }
    }
}
