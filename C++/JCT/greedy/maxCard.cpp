#include <iostream>

using namespace std;

int min(int n1, int n2);
int max(int n1, int n2);

int main(void)
{
	int N, M;
	cin >> N >> M;
	int* minArr = new int [N];
	for (int i = 0; i < N; i++) {
		minArr[i] = INT_MAX;
		for (int j = 0; j < M; j++) {
			int num;
			cin >> num;
			minArr[i] = min(minArr[i], num);
		}
	}

	int result = INT_MIN;
	for (int i = 0; i < N; i++) {
		result = max(minArr[i], result);
	}

	cout << result << endl;
	return 0;
}

int min(int n1, int n2) {
	return n1 < n2 ? n1 : n2;
}
int max(int n1, int n2) {
	return n1 > n2 ? n1 : n2;
}
