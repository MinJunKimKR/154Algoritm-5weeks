import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_10872 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int result =1;
        if(n==0){
            System.out.println(1);
        }
        else{
            for(int i=n;i>0;i--){
                result*=i;
            }
            System.out.println(result);
        }

    }
}
