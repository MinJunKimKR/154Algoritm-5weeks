import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class boj_10866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<String> d = new LinkedList<>();
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String input1 = st.nextToken();

            switch (input1) {
                case "push_front":
                    d.addFirst(st.nextToken());
                    break;
                case "push_back":
                    d.addLast(st.nextToken());
                    break;
                case "pop_front":
                    if (d.isEmpty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(d.pollFirst()).append("\n");
                    break;
                case "pop_back":
                    if (d.isEmpty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(d.pollLast()).append("\n");
                    break;
                case "size":
                    sb.append(d.size()).append("\n");
                    break;
                case "empty":
                    if (d.isEmpty())
                        sb.append("1").append("\n");
                    else
                        sb.append("0").append("\n");
                    break;
                case "front":
                    if (d.isEmpty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(d.peekFirst()).append("\n");
                    break;
                case "back":
                    if (d.isEmpty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(d.peekLast()).append("\n");
                    break;
            }
        }
        System.out.println(sb);

    }
}
