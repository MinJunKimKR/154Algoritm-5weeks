import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st2.nextToken());
        }

        int sum=0;
        int start=0,end=0,count=0;

        while(true){
            if(sum>=m){
                sum-=arr[start++];
            }
            else if(end==n){
                break;
            }else{
                sum+=arr[end++];
            }

            if(sum==m){
                count++;
            }
        }
        System.out.println(count);

    }
}
