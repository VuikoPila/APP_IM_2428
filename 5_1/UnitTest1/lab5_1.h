// lab5_1.h
#pragma once
#include <cmath>

double g(const double a, const double b) {
    return sin(a * b) / (pow(a, 2) * pow(b, 2));
}

double calculate_c(double s, double t) {
    return (g(pow(s, 2), t + 1) + g(pow(t, 2), s + 1)) / (1 + pow(g(s + t, s * t), 2));
}
