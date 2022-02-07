import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_1212 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String input = br.readLine();

        sb.append(Integer.toBinaryString(input.charAt(0) - '0'));

        for (int i = 1; i < input.length(); i++) {
            int a = input.charAt(i) - '0';

            if (Integer.toBinaryString(a).length() == 1) {
                sb.append("00").append(Integer.toBinaryString(a));
            } else if (Integer.toBinaryString(a).length() == 2) {
                sb.append("0").append(Integer.toBinaryString(a));
            } else {
                sb.append(Integer.toBinaryString(a));
            }


        }
        System.out.println(sb);
    }
}
