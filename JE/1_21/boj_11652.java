import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class boj_11652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<Long, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            long temp = Long.parseLong(br.readLine());
            if (map.containsKey(temp))
                map.put(temp, map.get(temp) + 1);
            else
                map.put(temp, 1);
        }

        Set<Long> keys = map.keySet();
        int count = 0;
        long num = 0;

        for (long key : keys) {
            if (count < map.get(key)) {
                count = map.get(key);
                num = key;
            } else if (count == map.get(key)) {
                num = Math.min(num, key);
                count = map.get(num);
            }
        }
        System.out.println(num);


    }
}
