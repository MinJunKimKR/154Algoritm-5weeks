import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static java.util.Arrays.sort;

public class boj_10610 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String str = br.readLine();

        int count = 0;
        int[] arr = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            count += str.charAt(i) - '0';
            arr[i] = str.charAt(i) - '0';
        }

        if (!str.contains("0") || count % 3 != 0)
            System.out.println(-1);
        else {
            sort(arr);
            for (int i = arr.length - 1; i >= 0; i--) {
                sb.append(arr[i]);
            }
        }
        System.out.println(sb);

    }
}
