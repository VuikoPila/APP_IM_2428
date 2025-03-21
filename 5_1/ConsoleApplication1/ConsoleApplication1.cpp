﻿// Lab 5_1
#include <iostream>
#include <cmath>
using namespace std;

double g(const double a, const double b);

int main()
{
	double s, t;

	cout << "s = "; cin >> s;
	cout << "t = "; cin >> t;
	double c = (g(pow(s, 2), t + 1) + g(pow(t, 2), s + 1)) / (1 + pow(g(s + t, s * t), 2));
	cout << "c = " << c << endl;
	return 0;
}
double g(const double a, const double b) 
{
	return sin(a*b)/(pow(a, 2) * pow(b, 2));
}