import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_2110 {

    public static int[] house;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        house = new int[N];

        for (int i = 0; i < N; i++) {
            house[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(house);    // 이분탐색을 하기 위해선 반드시 정렬 되어있어야 한다.


        int lo = 1;        // 최소 거리가 가질 수 있는 최솟값
        int hi = house[N - 1] - house[0] + 1;    // 최소 거리가 가질 수 있는 최댓값

        while (lo < hi) {    // Upper Bound 형식

            int mid = (hi + lo) / 2;

            /*
             * mid 거리에 대해 설치 가능한 공유기 개수가 M 개수에 못미치면
             * 거리를 좁혀야 하기 때문에 hi 를 줄인다.
             */
            if (canInstall(mid) < M) {
                hi = mid;
            } else {
                /**
                 * 설치 가능한 공유기 개수가 M 개수보다 크거나 같으면
                 * 거리를 벌리면서 최소거리가 가질 수 있는 최대 거리를
                 * 찾아낸다.
                 */
                lo = mid + 1;
            }
        }

        /*
         *  Upper Bound는 탐색 값을 초과하는 첫 번째 값을 가리키므로,
         *  1을 빼준 값이 조건식을 만족하는 최댓값이 된다.
         */
        System.out.println(lo - 1);
    }

    // distance에 대해 설치 가능한 공유기 개수를 찾는 메소드
    public static int canInstall(int distance) {

        // 첫 번째 집은 무조건 설치한다고 가정
        int count = 1;
        int lastLocate = house[0];

        for (int i = 1; i < house.length; i++) {
            int locate = house[i];

            /*
             *  현재 탐색하는 집의 위치와 직전에 설치했던 집의 위치간 거리가
             *  최소 거리(distance)보다 크거나 같을 때 공유기 설치 개수를 늘려주고
             *  마지막 설치 위치를 갱신해준다.
             */
            if (locate - lastLocate >= distance) {
                count++;
                lastLocate = locate;
            }
        }
        return count;

    }


}