#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double s(double x);

int main() {
    double r_start, r_end;
    int n;
    cout << "r_start: "; cin >> r_start;
    cout << "r_end: "; cin >> r_end;
    cout << "n: "; cin >> n;

    double dr = (r_end - r_start) / n;
    double r = r_start;

    cout << setw(10) << "r" << setw(15) << "s(sqrt(r+1)) - s(sqrt(r-1)) + 1" << endl;
    cout << "--------------------------------------------" << endl;

    while (r <= r_end) {
        double result = s(sqrt(r + 1)) - s(sqrt(r - 1)) + 1;
        cout << setw(10) << r << setw(15) << result << endl;
        r += dr;
    }

    return 0;
}

double s(double x) {
    if (abs(x) >= 1) {
        return (1 + x * x) / sqrt(1 + abs(sin(x)));
    }
    else {
        double sum1 = 0, sum2 = 0;
        for (int i = 0; i <= 6; i++) {
            sum1 += pow(x, i) / tgamma(i + 1); 
        }
        for (int k = 1; k <= 6; k++) {
            sum2 += pow(x, k) / tgamma(k + 1); 
        }
        return sum1 + sum2;
    }
}
