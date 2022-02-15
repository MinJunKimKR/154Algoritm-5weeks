import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_2251 {

    static class Bucket {
        int[] tmp;

        public Bucket(int[] tmp) {
            this.tmp = new int[3];
            for (int i = 0; i < 3; i++) {
                this.tmp[i] = tmp[i];
            }
        }

        Bucket move(int from, int to) {
            int[] ttmp = {tmp[0], tmp[1], tmp[2]};
            if (tmp[from] + tmp[to] > limit[to]) {
                ttmp[from] -= limit[to] - tmp[to];
                ttmp[to] = limit[to];
            } else {
                ttmp[from] = 0;
                ttmp[to] = tmp[from] + tmp[to];
            }
            return new Bucket(ttmp);
        }

    }

    static int[] limit, bucket;
    static boolean[][] check;
    static Set<Integer> answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        limit = new int[3];
        bucket = new int[3];
        for (int i = 0; i < 3; i++) {
            limit[i] = Integer.parseInt(st.nextToken());
        }

        answer = new TreeSet<>();
        bfs();

        for (int num : answer) {
            System.out.print(num + " ");
        }
    }

    static void bfs() {
        Queue<Bucket> q = new LinkedList<>();
        q.add(new Bucket(new int[]{0, 0, limit[2]}));
        check = new boolean[201][201];
        check[0][0] = true;
        while (!q.isEmpty()) {
            Bucket p = q.poll();
            if (p.tmp[0] == 0) {
                answer.add(p.tmp[2]);
            }
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (i != j) {
                        Bucket nxt = p.move(i, j);
                        if (!check[nxt.tmp[0]][nxt.tmp[1]]) {
                            check[nxt.tmp[0]][nxt.tmp[1]] = true;
                            q.add(nxt);
                        }
                    }
                }
            }

        }

    }
}
