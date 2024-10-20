#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	double k, N, i;
	double S;
	cout << "k = "; cin >> k;
	cout << "N = "; cin >> N;
	S = 0;
	i = k;
	while (i <= N)
	{
		S += (k/i) + (i/N);
		i++;
	}
	cout << S << endl;
	S = 0;
	i = k;
	do {
		S += (k / i) + (i / N);
		i++;
	} while (i <= N);
	cout << S << endl;
	S = 0;
	for (i = k; i <= N; i++)
	{
		S += (k / i) + (i / N);
	}
	cout << S << endl;
	S = 0;
	for (i = N; i >= k; i--)
	{
		S += (k / i) + (i / N);
	}
	cout << S << endl;
	return 0;
}