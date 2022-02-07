import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_1992 {
    public static int[][] img;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        img = new int[n][n];

        for (int i = 0; i < n; i++) {
            String str = br.readLine();

            for (int j = 0; j < n; j++) {
                img[i][j] = str.charAt(j) - '0';
            }
        }

        QuadTree(0, 0, n);
        System.out.println(sb);
    }

    public static void QuadTree(int x, int y, int size) {
        // 압축이 가능할 경우 하나의 색상으로 압축
        if (isPossible(x, y, size)) {
            sb.append(img[x][y]);
            return;
        }
        int newSize = size / 2; //압축이 불가능할 경우 사이즈를 절반으로 나누어야함

        sb.append('(');// 각 레벨에서 여는 괄호로 시작해야함

        QuadTree(x, y, newSize); // 왼쪽 위
        QuadTree(x, y + newSize, newSize); // 오른쪽 위
        QuadTree(x + newSize, y, newSize); // 왼쪽 아래
        QuadTree(x + newSize, y + newSize, newSize); // 오른쪽 아래

        sb.append(')'); // 해당 레벨이 끝나면 닫는 괄호도 닫아줌

    }

    // 압축 가능한지 해당 공간을 체크해주는 함수
    public static boolean isPossible(int x, int y, int size) {
        int value = img[x][y];

        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (value != img[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}
