import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_10818 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
//        int[] arr = new int[n];
//        int index = 0;
//        while (st.hasMoreTokens()) {
//            arr[index] = Integer.parseInt(st.nextToken());
//            index++;
//        }
//        Arrays.sort(arr);
//
//        System.out.println(arr[0] + " " + arr[n - 1]);

        int max = -1000001;
        int min = 1000001;
        while (st.hasMoreTokens()) {
            int val = Integer.parseInt(st.nextToken());
            if (max < val) {
                max = val;
            }
            if (min > val) {
                min = val;
            }
        }
        System.out.println(min + " " + max);
    }
}
