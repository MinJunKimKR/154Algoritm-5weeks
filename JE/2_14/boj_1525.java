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

        // 방향
        int[] dx = {0, 0, 1, -1}; // 우, 좌, 하, 상
        int[] dy = {1, -1, 0, 0};

        Queue<Integer> q = new LinkedList<>(); // bfs를 위한 큐 생성
        Map<Integer, Integer> m = new HashMap<>(); // 이동회수 저장할 맵 생성

        q.add(start); // 큐에 시작 상태 넣기
        m.put(start, 0); // 맵에 시작 상태에 최소이동횟수 0 넣기

        while (!q.isEmpty()) {
            int nowNum = q.poll(); // 큐에서 빼기
            String now = String.valueOf(nowNum); // int -> string
            int nine = now.indexOf("9");// 9의 인덱스 뽑기
            // 1차원 배열의 인덱스를 2차원 행과 열의 인덱스로 구하기
            int x = nine / 3; // 행
            int y = nine % 3; // 열
            // 방향 순환하기
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                int move = nx * 3 + ny; // 그것으로 1차원 배열 인덱스로 다시 만들기
                if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
                    // 9와 move 자리에 있는 값 swap 하기
                    StringBuilder next = new StringBuilder(now);
                    char temp = next.charAt(move);
                    next.setCharAt(nine, temp);
                    next.setCharAt(move, '9');
                    int nextNum = Integer.parseInt(next.toString()); // String -> int
                    if (!m.containsKey(nextNum)) { // 결과가 맵에 없다면
                        q.add(nextNum); // 큐에 넣기
                        m.put(nextNum, m.get(nowNum) + 1); // 맵에 +1 해서 넣기

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
