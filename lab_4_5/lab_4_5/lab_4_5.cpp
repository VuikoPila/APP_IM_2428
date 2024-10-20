#include <iostream>
#include <iomanip>
#include <time.h>
using namespace std;
int main()
{
	double x, y, R; 
	const double PI = 3.14159265358979323846;
	srand((unsigned)time(NULL));
	for (int i = 0; i < 10; i++)
	{
		cout << "x = "; cin >> x;
		cout << "y = "; cin >> y;
		cout << "R = "; cin >> R;
		if ((x >= 0 && y >= 0 && x * x + y * y <= R * R && atan2(y, x) <= PI / 4) ||
			(x >= 0 && y <= 0 && x * x + y * y <= R * R && atan2(y, x) >= -PI / 4))
			cout << "yes" << endl;
		else
			cout << "no" << endl;
	}
	cout << endl << fixed;

	for (int i = 0; i < 10; i++)
	{
		x = 6. * rand() / RAND_MAX - 3;
		y = 6. * rand() / RAND_MAX - 3;
		if ((x >= 0 && y >= 0 && x * x + y * y <= R * R && atan2(y, x) <= PI / 4) ||
			(x >= 0 && y <= 0 && x * x + y * y <= R * R && atan2(y, x) >= -PI / 4))
			cout << setw(8) << setprecision(4) << x << " "
			<< setw(8) << setprecision(4) << y << " " << "yes" << endl;
		else
			cout << setw(8) << setprecision(4) << x << " "
			<< setw(8) << setprecision(4) << y << " " << "no" << endl;
		}
	return 0;
}