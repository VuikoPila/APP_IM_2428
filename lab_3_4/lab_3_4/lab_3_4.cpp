// Lab_03_4.cpp
// < Лагуш Любомир >
// Лабораторна робота No 3.4
// Розгалуження, задане плоскою фігурою.
// Варіант 0.1
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double x, y, R;

    cout << "R = "; cin >> R;
    cout << "x = "; cin >> x;
    cout << "y = "; cin >> y;

    const double PI = 3.14159265358979323846;

    if ((x >= 0 && y >= 0 && x * x + y * y <= R * R && atan2(y, x) <= PI / 4) ||
        (x >= 0 && y <= 0 && x * x + y * y <= R * R && atan2(y, x) >= -PI / 4)) {
        cout << "yes" << endl;
    }
    else {
        cout << "no" << endl;
    }

    cin.get();
    return 0;
}



