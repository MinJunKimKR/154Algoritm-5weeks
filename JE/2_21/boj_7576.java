import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_7576 {
    static int n;
    static int m;
    static int[][] box;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    static class Dot {
        int x;
        int y;
        int day;

        public Dot(int x, int y, int day) {
            this.x = x;
            this.y = y;
            this.day = day;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        box = new int[m][n];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        bfs();
    }

    static void bfs() {
        Queue<Dot> q = new LinkedList<>();
        int day = 0;
        // 토마토가 있는 좌표 찾아 Queue에 넣기
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (box[i][j] == 1)
                    q.offer(new Dot(i, j, 0));
            }
        }

        // bfs 시작
        while (!q.isEmpty()) {
            Dot dot = q.poll();
            day = dot.day;

            for (int i = 0; i < 4; i++) {
                int nx = dot.x + dx[i];
                int ny = dot.y + dy[i];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                    if (box[nx][ny] == 0) {
                        box[nx][ny] = 1;
                        q.add(new Dot(nx, ny, day + 1));
                    }
                }
            }
        }

        // 토마토 다익었는지 확인
        if (checkTomato())
            System.out.println(day);
        else
            System.out.println(-1);
    }

    static boolean checkTomato() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (box[i][j] == 0)
                    return false;
            }
        }
        return true;
    }
}
