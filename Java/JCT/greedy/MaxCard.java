package greedy;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class MaxCard {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] minArr = new int[N];
        for (int i = 0; i < N; i++) {
            int[] row = split(br.readLine(), M);
            minArr[i] = min(row);
        }

        System.out.println(max(minArr));
        br.close();
    }

    private static int[] split(String str, int M) {
        int[] arr = new int[M];
        int index = 0;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch != ' ') {
                arr[index++] = ch - '0';
            }
        }
        return arr;
    }

    private static int max(int[] arr) {
        int maxVal = 1;
        for (int num : arr) {
            if (maxVal < num) {
                maxVal = num;
            }
        }
        return maxVal;
    }

    private static int min(int[] arr) {
        int minVal = 100;
        for (int num : arr) {
            if (minVal > num) {
                minVal = num;
            }
        }
        return minVal;
    }
}
