import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.util.Arrays.sort;

public class boj_1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[] arr = new int[k];

        for (int i = 0; i < k; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        sort(arr);


        long min = 1;
        long max = arr[k - 1];
        long middle = 0;


        while (min <= max) {
            long total = 0;
            middle = (min + max) / 2;

            for (int i = 0; i < arr.length; i++) {
                total += arr[i] / middle;
            }

            if (total >= n) {
                min = middle + 1;
            } else {
                max = middle - 1;
            }

        }
        System.out.println(max);

    }


}
