import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_11728 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int len = n + m;

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        StringTokenizer st3 = new StringTokenizer(br.readLine());

        int[] arr = new int[len];

        int idx = 0;
        for (int i = 0; i < n; i++) {
            arr[idx++] = Integer.parseInt(st2.nextToken());
        }
        for (int i = 0; i < m; i++) {
            arr[idx++] = Integer.parseInt(st3.nextToken());
        }

        Arrays.sort(arr);

        for (int i = 0; i < len; i++) {
            sb.append(arr[i]).append(" ");
        }
        System.out.println(sb);

    }
}
