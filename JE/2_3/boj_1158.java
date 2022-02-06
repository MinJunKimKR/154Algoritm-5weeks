import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_1158 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            queue.add(i);
        }

        int count = 1;

        sb.append("<");

        while (!queue.isEmpty()) {
            if (count == k) {
                if (queue.size() == 1)
                    sb.append(queue.poll()).append(">");
                else
                    sb.append(queue.poll()).append(", ");
                count = 1;
            } else {
                queue.add(queue.poll());
                count++;
            }
        }

        System.out.println(sb);

    }
}
