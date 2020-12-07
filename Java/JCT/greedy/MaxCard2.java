package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class MaxCard2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int maxVal = 1;
        for (int i = 0; i < N; i++) {
            int minVal = 10001;
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int nextInt = Integer.parseInt(st.nextToken());
                minVal = min(minVal, nextInt);
            }
            maxVal = max(maxVal, minVal);
        }

        System.out.println(maxVal);
        br.close();
    }

    private static int min(int a, int b) {
        return a < b ? a : b;
    }

    private static int max(int a, int b) {
        return a > b ? a : b;
    }
}
