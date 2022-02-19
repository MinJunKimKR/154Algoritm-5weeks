import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1806 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int min = Integer.MAX_VALUE;

        int start = 0, end = 0;
        int sum = 0;

        while (true) {
            if (sum >= s) {
                sum -= arr[start];
                min = Math.min(end-start, min);
                start++;
            } else if (end == n) {
                break;
            } else {
                sum += arr[end++];
            }


        }
        if(min ==Integer.MAX_VALUE) System.out.println(0);
        else System.out.println(min);
    }
}
