import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_9466 {
    static int[] arr;
    static boolean[] visit, done; // 방문, 팀 편성 완료 배열
    static int count; // 팀이 완성된 인원수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            arr = new int[n + 1];
            visit = new boolean[n + 1];
            done = new boolean[n + 1];
            count = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int i = 1; i <= n; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            for (int i = 1; i <= n; i++) {
                if (!done[i]) {
                    dfs(i);
                }
            }
            System.out.println(n - count);
        }
    }

    public static void dfs(int n) {
        // 이미 방문했을 때
        if (visit[n]) {
            done[n] = true; // 팀편성완료했다고 처리
            count++; // 팀편성완료 인원 증가
        } else {
            // 방문하지 않았을 때 -> 방문처리
            visit[n] = true;
        }

        // 다음 학생이 팀 결성을 아직 못했을 경우
        if (!done[arr[n]]) {
            dfs(arr[n]);
        }
        visit[n] = false;
        done[n] = true;

    }
}
