#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    // xp 2 xk 5 dx 0.5 eps 0.0001
    double xp, xk, x, dx, eps, a = 0, R = 0, S = 0;
    int n = 0;
    const double PI = 3.14;

    cout << "xp = "; cin >> xp;
    cout << "xk = "; cin >> xk;
    cout << "dx = "; cin >> dx;
    cout << "eps = "; cin >> eps;

    cout << fixed;
    cout << "-------------------------------------------------" << endl;
    cout << "|" << setw(5) << "x" << " |"
        << setw(10) << "arctg(x)" << " |"
        << setw(7) << "S" << " |"
        << setw(5) << "n" << " |"
        << endl;
    cout << "-------------------------------------------------" << endl;

    x = xp;
    while (x <= xk) {
        n = 0;                // Лічильник кількості доданків
        a = 1.0 / x;           // Перший доданок ряду
        S = a;                 // Початкове значення суми ряду (без pi/2)

        do {
            n++;
            R = -1.0 / (x * x); // Відношення між членами ряду
            a *= R;             // Обчислення наступного члена
            S += a / (2 * n + 1); // Додаємо член, ділимо на (2n + 1)
        } while (abs(a) >= eps); // Поки абсолютне значення доданка більше або дорівнює точності eps

        // Додаємо до суми S константу pi/2
        S = PI / 2 + S;

        // Виводимо результат
        cout << "|" << setw(7) << setprecision(2) << x << " |"
            << setw(10) << setprecision(5) << atan(x) << " |"
            << setw(10) << setprecision(5) << S << " |"
            << setw(5) << n << " |"
            << endl;

        x += dx; // Збільшуємо x на dx
    }

    cout << "-------------------------------------------------" << endl;
    return 0;
}
