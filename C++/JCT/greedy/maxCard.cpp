#include <iostream>

using namespace std;

int min(int n1, int n2);
int max(int n1, int n2);

int main(void)
{
	int N, M;
	cin >> N >> M;
	

	int result = INT_MIN;
	for (int i = 0; i < N; i++)
	{
		int minVal = INT_MAX;
		for (int j = 0; j < M; j++)
		{
			int num;
			cin >> num;
			minVal = min(minVal, num);
		}
		result = max(result, minVal);
	}

	cout << result << endl;
	return 0;
}

int min(int n1, int n2)
{
	return n1 < n2 ? n1 : n2;
}
int max(int n1, int n2)
{
	return n1 > n2 ? n1 : n2;
}
