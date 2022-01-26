import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_10820 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str;
        while ((str = br.readLine()) != null) {
            int lower = 0;
            int upper = 0;
            int num = 0;
            int space = 0;
            for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                if (ch >= 97 && ch <= 122) {
                    lower++;
                } else if (ch >= 65 && ch <= 90) {
                    upper++;
                } else if (ch >= 48 && ch <= 57) {
                    num++;
                } else {
                    space++;
                }
            }
            System.out.println(lower + " " + upper + " " + num + " " + space);
        }
    }
}
