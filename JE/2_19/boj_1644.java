import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class boj_1644 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        boolean[] prime = new boolean[n + 1];
        prime[0] = prime[1] = true;

        for (int i = 0; i * i <= n; i++) {
            if (!prime[i]) {
                for (int j = i + i; j <= n; j+=i) {
                    prime[j] = true;
                }
            }
        }

        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            if (!prime[i]) arr.add(i);
        }

        int sum = 0;
        int start = 0, end = 0, count = 0;
        while (true) {
            if (sum >= n) sum -= arr.get(start++);
            else if (end == arr.size()) break;
            else sum += arr.get(end++);

            if (sum == n) count++;
        }

        System.out.println(count);

    }
}
