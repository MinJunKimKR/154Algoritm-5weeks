import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class boj_10825 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        String[][] arr = new String[n][4];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = st.nextToken();
            arr[i][1] = st.nextToken();
            arr[i][2] = st.nextToken();
            arr[i][3] = st.nextToken();
        }

        Arrays.sort(arr, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                if (Integer.parseInt(o1[1]) == Integer.parseInt(o2[1])) {
                    if (Integer.parseInt(o1[2]) == Integer.parseInt(o2[2])) {
                        if (Integer.parseInt(o1[3]) == Integer.parseInt(o2[3])) {
                            // 국영수 점수가 같다면 사전 오름차순
                            return o1[0].compareTo(o2[0]);
                        }

                        // 국어점수 같고 영어점수 같을 때, 수학점수는 내림차순
                        return Integer.compare(Integer.parseInt(o2[3]), Integer.parseInt(o1[3]));
                    }

                    // 국어점수 같을 때, 영어점수는 오름차순
                    return Integer.compare(Integer.parseInt(o1[2]), Integer.parseInt(o2[2]));
                }
                // 국어점수는 내림차순
                return Integer.compare(Integer.parseInt(o2[1]), Integer.parseInt(o1[1]));
            }
        });

        for (int i = 0; i < n; i++) {
            sb.append(arr[i][0] + "\n");
        }

        System.out.println(sb);
    }
}
