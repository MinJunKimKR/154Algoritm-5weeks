import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1451 {
    static int N, M;
    static int[][] map;
    static long[][] sum;
    static long ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N + 1][M + 1];

        // 거리계산시 나올 수 있는 최댓값 넣어두기
        for (int i = 1; i <= N; i++) {
            String input = " " + br.readLine();
            for (int j = 1; j <= M; j++) {
                map[i][j] = input.charAt(j) - '0';
            }
        }


        sum = new long[N + 1][M + 1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + (long) map[i][j];
            }
        }


        ans = 0;
        for (int i = 1; i <= M - 2; i++) {
            for (int j = i + 1; j <= M - 1; j++) {
                long r1 = sum(1, 1, N, i);
                long r2 = sum(1, i + 1, N, j);
                long r3 = sum(1, j + 1, N, M);
                if (ans < r1 * r2 * r3) {
                    ans = r1 * r2 * r3;
                }
            }
        }

        for (int i = 1; i <= N - 2; i++) {
            for (int j = i + 1; j <= N - 1; j++) {
                long r1 = sum(1, 1, i, M);
                long r2 = sum(i + 1, 1, j, M);
                long r3 = sum(j + 1, 1, N, M);
                if (ans < r1 * r2 * r3) {
                    ans = r1 * r2 * r3;
                }
            }
        }

        for (int i = 1; i <= N - 1; i++) {
            for (int j = 1; j <= M - 1; j++) {
                long r1 = sum(1, 1, N, j);
                long r2 = sum(1, j + 1, i, M);
                long r3 = sum(i + 1, j + 1, N, M);
                if (ans < r1 * r2 * r3) {
                    ans = r1 * r2 * r3;
                }
                r1 = sum(1, 1, i, j);
                r2 = sum(i + 1, 1, N, j);
                r3 = sum(1, j + 1, N, M);
                if (ans < r1 * r2 * r3) {
                    ans = r1 * r2 * r3;
                }
                r1 = sum(1, 1, i, M);
                r2 = sum(i + 1, 1, N, j);
                r3 = sum(i + 1, j + 1, N, M);
                if (ans < r1 * r2 * r3) {
                    ans = r1 * r2 * r3;
                }
                r1 = sum(1, 1, i, j);
                r2 = sum(1, j + 1, i, M);
                r3 = sum(i + 1, 1, N, M);
                if (ans < r1 * r2 * r3) {
                    ans = r1 * r2 * r3;
                }
            }
        }
        System.out.println(ans);
    }

    private static long sum(int x1, int y1, int x2, int y2) {
        return sum[x2][y2] - sum[x2][y1 - 1] - sum[x1 - 1][y2] + sum[x1 - 1][y1 - 1];
    }
}
