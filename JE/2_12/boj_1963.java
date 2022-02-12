import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_1963 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 에라토스테네스의 체
        List<Boolean> prime = new ArrayList<>();

        // 0과 1을 소수가 아닌걸로 처리
        prime.add(false);
        prime.add(false);

        for (int i = 2; i < 10000; i++) {
            prime.add(true);
        }
        for (int i = 2; i < 10000; i++) {
            if (prime.get(i)) {
                for (int j = i + i; j < 10000; j += i) {
                    prime.set(j, false);
                }
            }
        }

//        boolean[] prime = new boolean[10000];
//        prime[0]=prime[1]=true;
//        for(int i=2;i<10000;i++){
//            if(!prime[i]){
//                for(int j=i+i;j<10000;j+=i){
//                    prime[i] = true;
//                }
//            }
//        }


        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            Queue<Integer> q = new LinkedList<>();
            int[] d = new int[10000]; // 최소횟수 저장하는 배열
            boolean[] bb = new boolean[10000]; // 방문처리위해

            q.add(a);
            bb[a] = true;

            while (!q.isEmpty()) {
                int v = q.poll();
                for (int i = 0; i < 4; i++) {
                    for (int j = 0; j <= 9; j++) {
                        if (i == 0 && j == 0) // 0번째 자리를 0으로 바꾸면 안된다
                            continue;
                        int k = change(v, i, j); // 변경가능한 수 모두 구해보기
                        if (prime.get(k) && !bb[k]) { // k가 소수이고 k를 방문하지 않았을 때?
                            d[k] = d[v] + 1;// 횟수를 센다
                            bb[k] = true; // 방문처리 한다
                            q.add(k);
                        }
                    }
                }
            }

            System.out.println(d[b]);


        }
    }

    static int change(int num, int index, int v) {
        StringBuilder sb = new StringBuilder(String.valueOf(num));
        sb.setCharAt(index, (char) (v + '0')); //(인덱스, 바꿀문자)  (char) (v + '0') = int v를 문자 v로 만듬
        return Integer.parseInt(sb.toString());
    }
}
