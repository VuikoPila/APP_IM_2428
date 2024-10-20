#include <iostream>
#include <cmath>
using namespace std;
int main() {
	double k, S, P;
	int n, i;
	P = 1;
	k = 1;
	n = 1;
	while (n <= 10)
	{
		S = 0;
		i = 1;
		while (i <= n)
		{
			S += sin(k * n);
			i++;
		}
		P *= S/k;
		n++;
	}
	cout << P << endl;
	P = 1;
	k = 1;
	n = 1;
	do
	{
		S = 0;
		i = 1;
		do
		{

			S += sin(k * n);
			i++;
		} while (i <= n);
		P *= S / k;
		n++;
	} while (n <= 10);
	cout << P << endl;
	P = 1;
	k = 1;
	for (n = 1; n <= 10; n++)
	{
		S = 0;
		for (i = 1; i <= n; i++)
		{
			S += sin(k * n);
		}
		P *= S/k;
	}
	cout << P << endl;
	P = 1;
	k = 1;
	for (n = 10; n >= 1; n--
		)

	{
		S = 0;
		for (i = n; i >= 1; i--
			)

		{
			S += sin(k * n);


		}
		P *= S / k;
	}
	cout << P << endl;
	return 0;
}