import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static java.lang.Math.sqrt;

public class boj_11653 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for(int i=2;i<=sqrt(n);i++){ // n이 두개이상 곱일때 인수 하나는 루트 n 보다 작거나 같다
            while(n%i==0){
                System.out.println(i);
                n/=i;
            }
        }
        if(n!=1){
            System.out.println(n);
        }
    }
}
