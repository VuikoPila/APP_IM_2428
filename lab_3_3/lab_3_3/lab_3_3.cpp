// Lab_03_3.cpp
// < Лагуш Любомир >
// Лабораторна робота No 3.3
// Розгалуження, задане графіком функції.
// Варіант 0.1
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	double x; 
	double R; 
	double y; 

	cout << "R = "; cin >> R;
	cout << "x = "; cin >> x;

	if (x < (-8 - R))
		y = 0;
	else
		if ((-8 - R) <= x && x < (-8 + R))
			y = -R + sqrt(pow(R, 2) - pow((x + 8), 2));
		else
			if ((-8 + R) <= x && x < 0)
				y = ((2 + R) / (8 + R)) * (x + 8 + R);
			else
				if (0 <= x && x < 2)
					y = 0;
				else
					if (2 <= x && x < 6)
						y = -1 * (1 / 4) * (x - 2) + 2;
					else
						if (6 <= x)
							y = pow((x - 6), 2);
	cout << endl;
	cout << "y = " << y << endl;
	cin.get();
	return 0;
}
