import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class boj_11576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(br.readLine());

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int[] arr = new int[m + 1];
        for (int i = 1; i <= m; i++) {
            arr[i] = Integer.parseInt(st2.nextToken());
        }

        int ten = 0;
        for (int i = 1; i <= m; i++) {
            ten += arr[i] * Math.pow(a, m - i);
        }

        Stack<Integer> stack = new Stack<>();

        while (ten != 0) {
            stack.push(ten % b);
            ten /= b;
        }
        while (!stack.isEmpty()) {
            if (stack.size() == 1) {
                System.out.println(stack.peek());
            } else {
                System.out.print(stack.peek() + " ");
            }
            stack.pop();
        }

    }
}
