import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_1759 {
    private static String[] arr;
    private static int l, c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        arr = br.readLine().split(" "); // 입력값이 크지 않으니
        Arrays.sort(arr);

        solve(0, "");

    }

    private static void solve(int idx, String str) {
        if (str.length() == l) {// 길이가 l개 이고
            if (isPossible(str)) { // 모음 하나 이상, 자음 2개 이상 맞으면
                System.out.println(str);
            }
            return;
        }
        if (idx >= c) { // idx 값이 맨 끝에 왔으면 종료
            return;
        }

        // 자기 자신을 포함한것, 자기자신을 포함하지 않은 것 가지치기 시작
        solve(idx + 1, str + arr[idx]);// 자기 자신과 다음 문자까지 같이
        solve(idx + 1, str);//자기자신만

    }

    // 자음 2개이상 모음 한개 이상인지 확인
    private static boolean isPossible(String str) {
        int vowel = 0, consonant = 0;
        for (int i = 0; i < str.length(); i++) {
            if (isVowel(str.charAt(i))) {
                vowel++;
            } else {
                consonant++;
            }
        }
        return vowel >= 1 && consonant >= 2;
    }

    // 모음인지 확인
    private static boolean isVowel(char ch) {
        return ch == 'a' | ch == 'e' | ch == 'i' | ch == 'o' | ch == 'u';
    }

}
