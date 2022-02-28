import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_11652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        Arrays.sort(arr);

        long check = arr[0];
        int count = 1;
        int max = 1;

        for (int i = 1; i < n; i++) {
            if (arr[i] == arr[i - 1])
                count++;
            else
                count = 1;

            if (count > max) {
                max = count;
                check = arr[i];
            }

        }

        System.out.println(check);


    }
}