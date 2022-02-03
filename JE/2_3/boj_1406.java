import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class boj_1406 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Stack<String> left = new Stack<>();
        Stack<String> right = new Stack<>();

        String input = br.readLine();
        for (int i = 0; i < input.length(); i++) {
            left.push(input.substring(i, i + 1));
        }
        int m = Integer.parseInt(br.readLine());

        while (m-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String a = st.nextToken();

            switch (a) {
                case "L":
                    if (!left.empty()) {
                        right.push(left.pop());
                    }
                    break;
                case "D":
                    if (!right.empty()) {
                        left.push(right.pop());
                    }
                    break;
                case "B":
                    if (!left.empty()) {
                        left.pop();
                    }
                    break;
                case "P":
                    String b = st.nextToken();
                    left.push(b);
                    break;
            }
        }

        while (left.size() > 0) {
            right.push(left.pop());
        }

        while (right.size() > 0) {
            sb.append(right.pop());
        }


        System.out.println(sb);

    }
}
