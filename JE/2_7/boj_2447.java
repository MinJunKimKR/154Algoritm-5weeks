import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_2447 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        String[][] arr = new String[n][n];

        // 일단 빈칸
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                arr[i][j] = " ";
            }
        }

        star(arr, 0, 0, n);

        for (String[] strings : arr) {
            for (String string : strings) {
                sb.append(string);
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static void star(String[][] arr, int x, int y, int n) {
        if (n == 1) {
            arr[x][y] = "*";
            return;
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (!(i == 1 && j == 1)) { // 가운데 부분은 별 채우면 안되기 때문에 제외 !
                    star(arr, x + i * (n / 3), y + j * (n / 3), n / 3);
                }
            }
        }
    }
}
