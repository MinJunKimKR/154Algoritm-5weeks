import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_10808 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringBuilder sb = new StringBuilder();

        int[] arr = new int[26];
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            arr[ch - 97] += 1;
        }

        for (int i = 0; i < 26; i++) {
            sb.append(arr[i] + " ");
        }
        System.out.println(sb);

    }
}
