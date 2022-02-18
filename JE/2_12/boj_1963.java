import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_1963 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 에라토스테네스의 체
        // false 가 소수
        boolean[] prime = new boolean[10000];
        prime[0] = prime[1] = true;
        for (int i = 2; i < 10000; i++) {
            if (!prime[i]) {
                for (int j = i + i; j < 10000; j += i) {
                    prime[j] = true;
                }
            }
        }

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            Queue<Integer> q = new LinkedList<>();
            boolean[] visited = new boolean[10000];// 방문여부 확인
            int[] count = new int[10000]; // 최소 횟수 저장배열

            // a를 큐에 넣고 방문처리한다
            q.add(a);
            visited[a] = true;

            while (!q.isEmpty()) { // 큐가 빌 때까지 반복
                int num = q.poll(); // 큐에서 값을 꺼낸다
                for (int i = 0; i < 4; i++) { // 바꿀 자리 반복문 0,1,,2,3번째 자리인 경우
                    for (int j = 0; j <= 9; j++) { // i번째 자리를 0-9의 값으로 바꾼다
                        if (i == 0 && j == 0) { // 0번째 자리를 0으로 바꾸면 안된다
                            continue;
                        }
                        int k = change(num, i, j); // i번째를 j값으로 변경한 수
                        if (!prime[k] && !visited[k]) { // k가 소수이고 k를 방문하지 않았을 때
                            q.add(k); // 큐에 넣고
                            visited[k] = true; // 방문처리한다
                            count[k] = count[num] + 1; // 방문횟수를 증가시킨다
                        }
                    }
                }
            }
            System.out.println(count[b]);
        }


    }

    // 특정 자릿수를 들어온 값으로 바꾸기 위한 함수
    public static int change(int num, int i, int j) {
        StringBuilder sb = new StringBuilder(String.valueOf(num)); // int를 stringBuilder로 바꿈
        sb.setCharAt(i, (char) (j + '0')); //(인덱스, 바꿀문자)  (char) (v + '0') = int v를 문자 v로 만듬
        return Integer.parseInt(sb.toString()); // 그냥 sb 하면 안되는 이유는 괄호안에 타입이 string이기 때문

    }
}
