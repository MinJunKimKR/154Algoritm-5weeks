import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class boj_1744 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ans = 0;

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        int left = 0;
        int right = n - 1;

        for (; left < right; left += 2) {
            if (arr[left] < 1 && arr[left + 1] < 1) {
                ans += arr[left] * arr[left + 1];
            } else {
                break;
            }

        }

        for (; right > 0; right -= 2) {
            if (arr[right] > 1 && arr[right - 1] > 1) {
                ans += arr[right] * arr[right - 1];
            } else {
                break;
            }
        }

        for (; right >= left; right--) {
            ans += arr[right];
        }

        System.out.println(ans);

    }
}
