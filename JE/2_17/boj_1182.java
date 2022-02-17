import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1182 {
    private static int n,s;
    private static int count=0;
    private static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        arr = new int[n];
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st2.nextToken());
        }


        for (int i = 0; i < n; i++) {
           backtracking(arr[i],i);
        }
        System.out.println(count);
    }

    public static void backtracking(int total, int depth){
        if(depth ==n-1&&total==s){
            count++;
        }
        depth++;
        if(depth<n){
            backtracking(total+arr[depth], depth);
            backtracking(total, depth);
        }
    }
}
