import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class boj_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Stack<String> s = new Stack<>();
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String input1 = st.nextToken();

            switch (input1) {
                case "push":
                    s.push(st.nextToken());
                    break;
                case "pop":
                    if (s.isEmpty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(s.pop()).append("\n");
                    break;
                case "size":
                    sb.append(s.size()).append("\n");
                    break;
                case "empty":
                    if (s.empty())
                        sb.append("1").append("\n");
                    else
                        sb.append("0").append("\n");
                    break;
                case "top":
                    if (s.empty())
                        sb.append("-1").append("\n");
                    else
                        sb.append(s.peek()).append("\n");
                    break;
            }
        }
        System.out.println(sb);

    }
}
