import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2745 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String a = st.nextToken();
        int b = Integer.parseInt(st.nextToken());

        int result = 0;
        int idx = 0; // 승 0, 1, 2, 3
        int num = 0; // 계산하기 위해 각 자리 숫자를 10진수로 바꿔준다
        for (int i = a.length() - 1; i >= 0; i--) {
            char c = a.charAt(i);
            if (c >= '0' && c <= '9') {
                num = c - '0';
            } else {
                num = c - 55; // A-Z는 숫자로 변경
            }
            result += num * Math.pow(b, idx++);
        }
        System.out.println(result);

    }
}
