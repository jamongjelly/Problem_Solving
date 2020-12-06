import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Change {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("금액을 입력하세요: ");
        int N = Integer.parseInt(br.readLine());
        System.out.println(getMinCoins(N));
        br.close();
    }

    private static int getMinCoins(int N) {
        int[] coins = { 500, 100, 50, 10 };
        int numOfCoins = 0;

        for (int coin : coins) {
            numOfCoins += N / coin;
            N %= coin;
        }

        return numOfCoins;
    }
}