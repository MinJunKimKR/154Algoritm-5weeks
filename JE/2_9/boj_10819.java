import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_10819 { // 순열구하기
    static int max = 0;

    public static void perm(int[] a, int depth, int n) {
        if (depth == n) {
            sum(a, n);
            return;
        }
        for (int i = depth; i < n; i++) {
            swap(a, i, depth);
            perm(a, depth + 1, n);
            swap(a, i, depth);
        }
    }

    static void swap(int[] a, int depth, int n) {
        int temp = a[depth];
        a[depth] = a[n];
        a[n] = temp;
    }

    static void sum(int[] a, int k) {
        int sum = 0;
        for (int i = 2; i <= k; i++) {
            sum += Math.abs(a[i - 2] - a[i - 1]);
        }
        if (max < sum) {
            max = sum;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int num[] = new int[n];
        String number = br.readLine();
        StringTokenizer st = new StringTokenizer(number, " ");
        for (int i = 0; i < n; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }
        perm(num, 0, n);
        System.out.println(max);
    }
}

