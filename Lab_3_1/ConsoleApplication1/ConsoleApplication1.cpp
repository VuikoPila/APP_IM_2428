// Lab_03_1.cpp
// < ����� ������� >
// ����������� ������ No 3.1
// ������������, ������ ��������: ������� ���� �����.
// ������ 8
#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    double x;
    double y;
    double A;
    double B;

    cout << "x = "; cin >> x;

    A = 2 + 6 * x;

    // ������ ����� (�������� if)

    if (x <= 0)
        B = log(cos(x)) + pow(x, 5);

    if (0 < x && x <= 3 && tan(x) != 0)
        B = 1.0 / ((1.0 + log(x)) / 3);

    if (x > 3)
        B = 12.0 * x - pow(x, 8);

    y = A + B;

    cout << endl;
    cout << "1. y = " << y;

    // ������ ����� (����� if) 

    if (x <= 0)
        B = log(cos(x)) + pow(x, 5);
    else 
        if (0 < x && x <= 3 && tan(x) != 0)
            B = 1.0 / ((1.0 + log(x)) / 3);
        else
            B = 12.0 * x - pow(x, 8);

    y = A + B;

    cout << endl;
    cout << "2. y = " << y;

    cin.get();
    return 0;

}