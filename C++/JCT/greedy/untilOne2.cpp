#include <iostream>

using namespace std;

int main(void)
{
	int N, K;
	cin >> N >> K;

	int count = 0;
	while (N > 1)
	{
		int quotient = N / K;
		int kMultiple = quotient * K;

		if (N == kMultiple)
		{
			N = quotient;
			count++;
		}
		else
		{
			int diff = N - kMultiple;
			N -= diff;
			count += diff;
		}
	}

	cout << count << endl;
	return 0;
}
