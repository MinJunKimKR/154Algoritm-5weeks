import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1780 {
    public static int[][] board;
    public static int gray = 0; // -1
    public static int white = 0; // 0
    public static int black = 0; // 1

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        partition(0, 0, n);
        System.out.println(gray);
        System.out.println(white);
        System.out.println(black);

    }

    public static void partition(int row, int col, int size) {
        // 만약 같은 색상으로 이루어져있다면 해당 색상 카운트를 증가시킴
        if (colorCheck(row, col, size)) {
            if (board[row][col] == -1) {
                gray++;
            } else if (board[row][col] == 0) {
                white++;
            } else {
                black++;
            }
            return;
        }

        int newSize = size / 3;

        partition(row, col, newSize); // 왼쪽 위
        partition(row, col + newSize, newSize); // 중앙 위
        partition(row, col + 2 * newSize, newSize); // 오른쪽 위

        partition(row + newSize, col, newSize); // 왼쪽 위
        partition(row + newSize, col + newSize, newSize); // 중앙 위
        partition(row + newSize, col + 2 * newSize, newSize); // 오른쪽 위


        partition(row + 2 * newSize, col, newSize); // 왼쪽 위
        partition(row + 2 * newSize, col + newSize, newSize); // 중앙 위
        partition(row + 2 * newSize, col + 2 * newSize, newSize); // 오른쪽 위
    }

    // 해당 영역이 같은 색인지 검사하는 메소드
    public static boolean colorCheck(int row, int col, int size) {
        int color = board[row][col];

        // 각 블럭의 시작점(row, col)부터 블럭의 끝(row+size, col+size)까지 검사
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                if (color != board[i][j])
                    return false;
            }
        }
        return true;
    }

}
