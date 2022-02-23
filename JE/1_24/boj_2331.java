import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class boj_2331 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        List<Integer> list = new ArrayList<>();
        list.add(a);
        while (true) {
            int tmp = list.get(list.size() - 1);
            int result = 0;
            while (tmp != 0) {
                result += (int) Math.pow(tmp % 10, p);
                tmp /= 10;

            }
            if (list.contains(result)) {
                int ans = list.indexOf(result);
                System.out.println(ans);
                break;
            }

            list.add(result);
        }
    }
}