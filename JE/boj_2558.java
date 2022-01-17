import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_2558 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        System.out.println(a + b);
    }
}
