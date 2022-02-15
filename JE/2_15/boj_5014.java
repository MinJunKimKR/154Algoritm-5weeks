import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_5014 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int F = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());
        int U = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        int[] dx = {U, -D};

        Queue<Integer> q = new LinkedList<>();
        int[] count = new int[F + 1];
        Arrays.fill(count, -1);

        q.add(S);
        count[S] = 0;

        while (!q.isEmpty()) {
            int now = q.poll();

            for (int i = 0; i < 2; i++) {
                int nx = now + dx[i];
                if ((nx <= F && nx >= 1) && count[nx] == -1) { // count[nx]==-1 처음 방문?
                    q.add(nx);
                    count[nx] = count[now] + 1;
                }
            }
        }

        if (count[G] == -1) {
            System.out.println("use the stairs");
        } else {
            System.out.println(count[G]);
        }
    }


}
