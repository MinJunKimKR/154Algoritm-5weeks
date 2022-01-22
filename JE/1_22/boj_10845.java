import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Queue<String> q = new LinkedList<>();
        int t = Integer.parseInt(br.readLine());
        String last = "";
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String input1 = st.nextToken();

            switch (input1) {
                case "push":
                    String x = st.nextToken();
                    q.add(x);
                    last = x;
                    break;
                case "pop":
                    if (q.isEmpty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(q.poll()).append("\n");
                    break;
                case "size":
                    sb.append(q.size()).append("\n");
                    break;
                case "empty":
                    if (q.isEmpty())
                        sb.append("1").append("\n");
                    else
                        sb.append("0").append("\n");
                    break;
                case "front":
                    if (q.isEmpty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(q.peek()).append("\n");
                    break;
                case "back":
                    if (q.isEmpty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(last).append("\n");
                    break;
            }
        }
        System.out.println(sb);

    }
}
