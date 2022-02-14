import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_1525 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int start = 0;
        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                int k = Integer.parseInt(st.nextToken());
                if (k == 0) k = 9; // 0을 9로 바꿈
                start = (start * 10) + k; // 2차원 배열을 하나의 정수로 나타내기 위해
            }
        }

        Queue<Integer> q = new LinkedList<>();
        Map<Integer, Integer> m = new HashMap<>();
        int[] dx = {0, 0, 1, -1}; // 우, 좌, 하, 상
        int[] dy = {1, -1, 0, 0};

        m.put(start, 0);
        q.add(start);

        while (!q.isEmpty()) {
            int nowNum = q.poll();
            String now = String.valueOf(nowNum);
            int nine = now.indexOf("9"); // 9의 인덱스를 찾는다
            int x = nine / 3; // 9가 2차원 배열에서 몇번째 행인지 계산
            int y = nine % 3; // 9가 2차원 배열에서 몇번째 열인지 계산
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];// 이동할 상하좌우의 행계산
                int ny = y + dy[i];// 이동할 상하좌우의 열계산
                int move = nx * 3 + ny;// 이동할 상하좌우의 1차원 배열에서의 인덱스
                if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
                    StringBuilder next = new StringBuilder(now);
                    // 9와 이동할 상하좌우 스왑하기
                    char temp = next.charAt(move);
                    next.setCharAt(move, '9'); // 이동할 인덱스에 9를
                    next.setCharAt(nine, temp); // 원래 9자리에 이동한 곳의 수를
                    int nextNum = Integer.parseInt(next.toString());
                    if (!m.containsKey(nextNum)) { // 맵에 몇번이동했는지 저장
                        m.put(nextNum, m.get(nowNum) + 1);
                        q.add(nextNum);
                    }
                }
            }
        }
        if (m.containsKey(123456789)) {
            System.out.println(m.get(123456789));
        } else {
            System.out.println(-1);
        }

    }
}
