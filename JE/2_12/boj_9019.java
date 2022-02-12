import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_9019 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            String[] command = new String[10000]; // 정답을 담는 곳
            boolean[] visited = new boolean[10000]; // BFS 탐색의 방문 여부 체크

            Queue<Integer> q = new LinkedList<>();

            visited[a] = true;
            q.add(a);
            Arrays.fill(command, "");

            while (!q.isEmpty() && !visited[b]) {
                int now = q.poll(); // 큐에서 뺀다
                int D = (2 * now) % 10000;
                int S = (now == 0) ? 9999 : now - 1;
                int L = (now % 1000) * 10 + now / 1000; // 계산으로 자릿수 바꾸는 거 기억 !
                int R = (now % 10) * 1000 + now / 10;


                if (!visited[D]) {
                    q.add(D);
                    visited[D] = true;
                    command[D] = command[now] + "D";
                }

                if (!visited[S]) {
                    q.add(S);
                    visited[S] = true;
                    command[S] = command[now] + "S";
                }

                if (!visited[L]) {
                    q.add(L);
                    visited[L] = true;
                    command[L] = command[now] + "L";
                }

                if (!visited[R]) {
                    q.add(R);
                    visited[R] = true;
                    command[R] = command[now] + "R";
                }
            }
            System.out.println(command[b]);
        }
    }
}