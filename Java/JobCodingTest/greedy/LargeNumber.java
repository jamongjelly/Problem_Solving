import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class LargeNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] numArr = new int[N];
        int[] max = new int[2];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numArr[i] = Integer.parseInt(st.nextToken());
            if (numArr[i] > max[0]) {
                max[1] = max[0];
                max[0] = numArr[i];
            } else if (numArr[i] > max[1]) {
                max[1] = numArr[i];
            }
        }

        int multiple = M / (K + 1) * K;
        int result = multiple * max[0] + (M - multiple) * max[1];
        
        System.out.println(result);
        br.close();
    }
}
