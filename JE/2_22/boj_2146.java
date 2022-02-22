import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_2146 {
    static int[][] map;
    static boolean[][] visit;
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    static int n, min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        map = new int[n][n];

        // 입력
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int cnt = 2;// 섬에 번호를 매긴다 2부터 시작
        visit = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1) { // 1이면 아직 번호를 매기지 않은 섬
                    map[i][j] = cnt;
                    visit[i][j] = true;
                    dfs(i, j, cnt++); // dfs를 이용해 번호를 매김
                }
                if (map[i][j] != 0) { // 현재 위치가 섬이라면
                    bfs(i, j); // bfs를 이용해서 다른 섬까지 도달하는데 필요한 다리의 길이를 구함
                }
            }
        }

        System.out.println(min);
    }

    public static void dfs(int y, int x, int cnt) {
        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (isMovable(nx, ny) && !visit[ny][nx] && map[ny][nx] == 1) {
                visit[ny][nx] = true;
                map[ny][nx] = cnt;
                dfs(ny, nx, cnt);
            }
        }
    }

    public static void bfs(int y, int x) {
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(y, x, 0));
        boolean[][] visit = new boolean[n][n];
        visit[y][x] = true;

        while (!q.isEmpty()) {
            Pos p = q.poll();
            // 가지치기 , 다리길이가 이전에 구한 가장 짧은 다리의 길이보다 길면 더이상조사할 필요없다
            if (p.dist >= min)
                return;

            for (int i = 0; i < 4; i++) {
                int ny = p.y + dy[i];
                int nx = p.x + dx[i];

                if (isMovable(ny, nx) && !visit[ny][nx]) {
                    if (map[ny][nx] == 0) { // 바다라면
                        visit[ny][nx] = true;
                        q.add(new Pos(ny, nx, p.dist + 1)); // 다리길이 +1
                    } else if (map[ny][nx] != map[y][x]) { // 다른 섬에 도달했다면
                        min = Math.min(min, p.dist);// 다리길이를 비교해 작은 값을 저장
                    }
                }
            }
        }
    }

    public static boolean isMovable(int y, int x) {
        if (y < 0 || x < 0 || y >= n || x >= n) {
            return false;
        }
        return true;
    }

    static class Pos {
        int y;
        int x;
        int dist;

        public Pos(int y, int x, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
}
