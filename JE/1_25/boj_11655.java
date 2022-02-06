import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_11655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch >= 97 && ch <= 109) {
                sb.append((char) (ch + 13));
            } else if (ch >= 110 && ch <= 122) {
                sb.append((char) (ch - 13));
            } else if (ch >= 65 && ch <= 77) {
                sb.append((char) (ch + 13));
            } else if (ch >= 78 && ch <= 90) {
                sb.append((char) (ch - 13));
            } else {
                sb.append(ch);
            }
        }

        System.out.println(sb);

    }
}
