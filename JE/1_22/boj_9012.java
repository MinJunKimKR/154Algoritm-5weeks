import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class boj_9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            String str = br.readLine();
            Stack<String> s = new Stack<>();

            boolean finish = false;
            for (int i = 0; i < str.length(); i++) {
                int input = str.charAt(i);
                if (input == '(')
                    s.push("(");
                else if (input == ')') {
                    if (s.empty()) {
                        finish = true;
                        break;
                    } else {
                        s.pop();
                    }
                }

            }

            if (!s.empty() || finish)
                System.out.println("NO");
            else
                System.out.println("YES");
        }
    }

}
