#include <iostream>

using namespace std;

int main(void)
{
	int N, K;
	cin >> N >> K;

	int count = 0;
	while (N > 1)
	{
		if (N % K == 0)
		{
			N /= K;
		}
		else
		{
			N--;
		}
		count++;
	}

	cout << count << endl;
	return 0;
}
