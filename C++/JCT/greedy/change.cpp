#include <iostream>

using namespace std;

int getMinCoins(int N);

int main(void)
{
	int N;
	cout << "금액을 입력해주세요: ";
	cin >> N;
	cout << getMinCoins(N) << endl;
	return 0;
}

int getMinCoins(int N)
{
	int coins[4] = { 500, 100, 50, 10 };
	int numOfCoins = 0;
	int arrSize = sizeof(coins) / sizeof(*coins);

	for (int i = 0; i < arrSize; i++)
	{
		int quotient = N / coins[i];
		numOfCoins += quotient;
		N %= coins[i];
	}

	return numOfCoins;
}