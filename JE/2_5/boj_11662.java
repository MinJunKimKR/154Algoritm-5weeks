import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_11662 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        double aX = Double.parseDouble(st.nextToken());
        double aY = Double.parseDouble(st.nextToken());
        double bX = Double.parseDouble(st.nextToken());
        double bY = Double.parseDouble(st.nextToken());
        double cX = Double.parseDouble(st.nextToken());
        double cY = Double.parseDouble(st.nextToken());
        double dX = Double.parseDouble(st.nextToken());
        double dY = Double.parseDouble(st.nextToken());

        int interval = 1000000;

        double aDX = (bX - aX) / interval;
        double aDY = (bY - aY) / interval;
        double cDX = (dX - cX) / interval;
        double cDY = (dY - cY) / interval;

        int lo = 0;
        int hi = interval;

        while (hi - lo >= 3) {
            int p = (2 * lo + hi) / 3;
            int q = (lo + 2 * hi) / 3;

            double pVal = getDistance(aX + aDX * p, aY + aDY * p, cX + cDX * p, cY + cDY * p);
            double qVal = getDistance(aX + aDX * q, aY + aDY * q, cX + cDX * q, cY + cDY * q);

            if (pVal < qVal) {
                hi = q - 1;
            } else {
                lo = p + 1;
            }
        }

        double min = getDistance(aX + aDX * hi, aY + aDY * hi, cX + cDX * hi, cY + cDY * hi);

        for (int i = lo; i < hi; i++) {
            double temp = getDistance(aX + aDX * i, aY + aDY * i, cX + cDX * i, cY + cDY * i);

            if (temp < min) {
                min = temp;
            }
        }

        System.out.println(min);
    }

    private static double getDistance(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }
}
