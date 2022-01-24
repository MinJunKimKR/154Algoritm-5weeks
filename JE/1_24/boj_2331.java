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
            int temp = list.get(list.size() - 1);

            int result = 0;
            // 어떤 수의 각 자리에 대해 p제곱만큼하여 각자리를 더한 값을 구함
            while (temp != 0) {
                result += (int) Math.pow(temp % 10, (double) p);
                temp /= 10;
            }

            // result가 이미 리스트에 포함되어있다면
            // 그 result가 가리키는 인덱스를 반환
            if (list.contains(result)) {
                int ans = list.indexOf(result);
                System.out.println(ans);
                break;
            }
            list.add(result);
        }


    }
}
