// Lab_03_2.cpp
// < ����� ������� >
// ����������� ������ No 3.2
// ������������, ������ ��������: ������� � �����������.
// ������ 0.1
#include <iostream>
using namespace std;
int main()
{
	//������ �����
	double x; 
	double a; 
	double c; 
	double F; 
	cout << "a = "; cin >> a;
	cout << "c = "; cin >> c;
	cout << "x = "; cin >> x;

	if (c < 0 && a != 0)
		F = -1 * a * pow(x, 2);
	if (c > 0 && a == 0)
		F = (a - x) / (c * x);
	if (!(c < 0 && a != 0) && !(c > 0 && a == 0))
		F = x / c;
	
	cout << endl;
	cout << "1. F= " << F;

	// ������ �����
	if (c < 0 && a != 0)
		F = -1 * a * pow(x, 2);
	else
		if (c > 0 && a == 0)
			F = (a - x) / (c * x);
		else
			F = x / c;
	cout << endl;
	cout << "2. F= " << F;

	cin.get();
	return 0;
}
