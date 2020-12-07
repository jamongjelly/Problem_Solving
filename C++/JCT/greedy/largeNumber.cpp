#include <iostream>

using namespace std;

int main(void)
{
	int N, M, K;
	cin >> N >> M >> K;
	int* numArr = new int[N];
	int first = 0, second = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> numArr[i];
		if (numArr[i] > first)
		{
			second = first;
			first = numArr[i];
		}
		else if (numArr[i] > second)
		{
			second = numArr[i];
		}
	}

	int secondCount = M / (K + 1);
	int result = (M - secondCount) * first + secondCount * second;

	cout << result << endl;
	return 0;
}