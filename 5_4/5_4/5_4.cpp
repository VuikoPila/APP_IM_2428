#include <iostream>
#include <cmath>
using namespace std;

// Ваші функції
double S0(const int K, const int N) {
    double s = 0;
    for (int i = K; i <= N; i++)
        s += ((K / static_cast<double>(i)) + (i / static_cast<double>(N)));
    return s;
}

double S1(const int K, const int N, const int i) {
    if (i > N)
        return 0;
    else
        return ((K / static_cast<double>(i)) + (i / static_cast<double>(N))) + S1(K, N, i + 1);
}

double S2(const int K, const int N, const int i) {
    if (i < K)
        return 0;
    else
        return ((K / static_cast<double>(i)) + (i / static_cast<double>(N))) + S2(K, N, i - 1);
}

double S3(const int K, const int N, const int i, double t) {
    t = t + ((K / static_cast<double>(i)) + (i / static_cast<double>(N)));
    if (i >= N)
        return t;
    else
        return S3(K, N, i + 1, t);
}

double S4(const int K, const int N, const int i, double t) {
    t = t + ((K / static_cast<double>(i)) + (i / static_cast<double>(N)));
    if (i <= K)
        return t;
    else
        return S4(K, N, i - 1, t);
}

// Функція для проведення тестів
void runTests() {
    double result = S0(1, 5);
    cout << "S0(1, 5) = " << result << " (Expected: 3.33333)" << endl;

    result = S1(1, 5, 1);
    cout << "S1(1, 5, 1) = " << result << " (Expected: 3.33333)" << endl;

    result = S2(1, 5, 5);
    cout << "S2(1, 5, 5) = " << result << " (Expected: 3.33333)" << endl;

    result = S3(1, 5, 1, 0);
    cout << "S3(1, 5, 1, 0) = " << result << " (Expected: 3.33333)" << endl;

    result = S4(1, 5, 5, 0);
    cout << "S4(1, 5, 5, 0) = " << result << " (Expected: 3.33333)" << endl;
}


int main() {
    runTests();

    return 0;
}
