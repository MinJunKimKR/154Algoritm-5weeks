import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_2448 {
    public static int n;
    public static char[][] arr;
    public static StringBuilder sb;

    public static void printStar(int row, int col, int num) {
        if (num == 3) {
            // 다 쪼개줌, 재귀 끝 -> 별찍기
            // 중간 지점을 기준으로 별을 찍을 것 -> 공백은 신경쓰지 않아도 됨 어차피 첨에 공백으로 초기화
            arr[row][col] = '*';
            arr[row + 1][col + 1] = arr[row + 1][col - 1] = '*';
            arr[row + 2][col - 2] = arr[row + 2][col - 1] = arr[row + 2][col]
                    = arr[row + 2][col + 1] = arr[row + 2][col + 2] = '*';
        } else {
            int n = num / 2;
            // 계속 3등분씩 잘라줄 것
            // 1행
            printStar(row, col, n);
            // 2행
            printStar(row + (num / 2), col + (num / 2), n);
            // 3행
            printStar(row + (num / 2), col - (num / 2), n);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        int num = n * 2 - 1;

        arr = new char[n][num];

        // 공백으로 채워넣기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < num; j++) {
                arr[i][j] = ' ';
            }
        }

        printStar(0, n - 1, n);
        // n-1인 이유는 딱 정중앙에 별이 찍히도록 하기 위해 n-1이 열의 중간지점

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < num; j++) {
                sb.append(arr[i][j]);
            }
            sb.append('\n');
        }

        System.out.println(sb);
    }
}
