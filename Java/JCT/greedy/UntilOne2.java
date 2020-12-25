package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class UntilOne2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int count = 0;
        while (N > 1) {
            int quotient = N / K;
            int kMultiple = quotient * K;

            if (N == kMultiple) {
                N = quotient;
                count++;
            } else {
                int diff = N - kMultiple;
                N -= diff;
                count += diff;
            }
        }

        System.out.println(count);
        br.close();
    }
}
