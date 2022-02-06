import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_1373 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String input = br.readLine();

        if (input.length() % 3 == 2) {
            sb.append(Integer.parseInt(input.substring(0, 1)) * 2 + Integer.parseInt(input.substring(1, 2)));
        }
        if (input.length() % 3 == 1) {
            sb.append(Integer.parseInt(input.substring(0, 1)));
        }


        for (int i = input.length() % 3; i < input.length(); i += 3) {
            if (i == input.length() - 3) {
                sb.append(Integer.parseInt(input.substring(i, i + 1)) * 4 + Integer.parseInt(input.substring(i + 1, i + 2)) * 2 + Integer.parseInt(input.substring(i + 2)));
            } else {
                sb.append(Integer.parseInt(input.substring(i, i + 1)) * 4 + Integer.parseInt(input.substring(i + 1, i + 2)) * 2 + Integer.parseInt(input.substring(i + 2, i + 3)));
            }
        }

        System.out.println(sb);
    }
}
