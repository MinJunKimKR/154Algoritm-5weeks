import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1987 {
    static int r, c;
    static int[][] map;
    static boolean[] visit = new boolean[26];
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int ans = 0;

    public static void dfs(int x, int y, int count) {
        System.out.println(x+" "+y+" "+count);
        if (visit[map[x][y]]) { // 0,0에 저장된 알파벳이 이미 한번 방문한 알파벳이면
            ans = Math.max(ans, count); //정답을 갱신
            return; // 조건에 만족하므로 리턴
        } else {
            visit[map[x][y]] = true;
            for (int i = 0; i < 4; i++) {
                int cx = x + dx[i];
                int cy = y + dy[i];
                if (cx >= 0 && cy >= 0 && cx < r && cy < c) {
                    dfs(cx, cy, count + 1);
                }
            }
            System.out.println("**");
            visit[map[x][y]] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        map = new int[r][c];
        for (int i = 0; i < r; i++) {
            String str = br.readLine();
            for (int j = 0; j < c; j++) {
                map[i][j] = str.charAt(j) - 'A';
            }

        }
        dfs(0, 0, 0);// 0,0부터 시작하며 현재 이동한 위치는 0회

        System.out.println(ans);
    }
}
