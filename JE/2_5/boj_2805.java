import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.util.Arrays.sort;

public class boj_2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st2.nextToken());
        }

        sort(arr);
        long min = 0;
        long max = arr[n - 1];
        long result = 0;

        while (min <= max) {
            long mid = (min + max) / 2;
            long total = 0;
            for (int i = 0; i < n; i++) {
                if (arr[i] > mid)
                    total += arr[i] - mid;

            }
            if (total >= m) {
                min = mid + 1;
            } else {
                max = mid - 1;

            }
        }
        System.out.println(max);

    }
}
