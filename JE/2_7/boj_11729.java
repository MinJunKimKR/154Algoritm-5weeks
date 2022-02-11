import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_11729 {
    public static StringBuilder sb = new StringBuilder();
    public static int count=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int n = Integer.parseInt(br.readLine());

        Hanoi(n, 1, 2, 3);
        System.out.println(count);
        System.out.println(sb);

    }

    /*
     n - 원판의 개수
     start - 출발지
     mid - 옮기기 위해 이동하는 장소
     to - 목적지
    */
    public static void Hanoi(int n, int start, int mid, int to) {
        count++;
        // 이동한 원반의 수가 1개라면 ?
        if (n == 1) {
            sb.append(start + " " + to + "\n");
            return;
        }

        // a->c로 옮긴다고 가정할 떄
        // 1. n-1개를 a에서 b로 이동 = start 지점의 n-1개의 원판을 mid 지점으로 옮긴다
        Hanoi(n - 1, start, to, mid);

        // 2. 1개를 a에서 c로 이동 = start 지점의 n번째 원판을 to 지점으로 옮김
        sb.append(start + " " + to + "\n");

        // 3. n-1개를 b에서 c로 이동 = mid 지점의 n-1개의 원판을 to 지점으로 옮긴다
        Hanoi(n - 1, mid, start, to);
    }
}
