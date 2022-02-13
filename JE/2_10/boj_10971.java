import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_10971 {
    static int n; // 도시의 수
    static int[][] w; // 비용
    static boolean[] visited; // 방문표시
    static int min = Integer.MAX_VALUE; // 최소비용값

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        w = new int[n + 1][n + 1];
        visited = new boolean[n + 1];

        // 비용 값 채워준다
        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                w[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited[1] = true; // 여기서 부터 시작이니 미리 방문 해둠
        dfs(1, 1, 1, 0);

        System.out.println(min);

    }

    // start = 시작도시
    // now = 현재 도시
    // cnt = 모든 도시를 다 방문했는지 방문 도시의 개수를 세주기 위한 값
    // cost = 최소 비용
    public static void dfs(int start, int now, int cnt, int cost) {


        if (now == start && cost > 0) { // 순회를 완료했을 때 now == start이고 cost도 n 될것이므로
            min = Math.min(min, cost);
            return;
        }

        for (int j = 1; j <= n; j++) {
            if (w[now][j] > 0) { // 비용 0인 경로 제외하기 위해
                // 인접한 도시가 시작 도시이고(j==start)
                // 모든 도시를 다 방문한 상태인 경우(cnt==n)
                if (j == start && cnt == n) {
                    cost += w[now][j];
                    dfs(start, j, cnt + 1, cost); // 이 함수 실행되면 dfs의 첫번째 if 문에 걸릴 것

                } else if (!visited[j]) { // 방문하지 않은 도시라면
                    visited[j] = true; // 방문표시
                    cost += w[now][j]; // j로 가는 비용 추가

                    dfs(start, j, cnt + 1, cost);

                    cost -= w[now][j]; // ?
                    visited[j] = false; // ?
                }
            }
        }
    }
}
