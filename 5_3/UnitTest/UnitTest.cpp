#include "pch.h"
#include "CppUnitTest.h"
#include <cmath>

// Include the header for 5_3.cpp or declare the function as extern
extern double s(double x);

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest_5_3
{
    TEST_CLASS(SFunctionTests)
    {
    public:

        // Test case for s(x) with |x| >= 1
        TEST_METHOD(TestHandlesGreaterOrEqualOne)
        {
            double x = 2.0;
            double expected = (1 + x * x) / sqrt(1 + fabs(sin(x)));
            Assert::AreEqual(expected, s(x), 1e-5, L"Test failed for |x| >= 1");
        }

        // Test case for s(x) with |x| < 1
        TEST_METHOD(TestHandlesLessThanOne)
        {
            double x = 0.5;
            double sum1 = 1.0 + x + x * x / 2 + pow(x, 3) / 6 + pow(x, 4) / 24 + pow(x, 5) / 120 + pow(x, 6) / 720;
            double sum2 = x + pow(x, 2) / 2 + pow(x, 3) / 6 + pow(x, 4) / 24 + pow(x, 5) / 120 + pow(x, 6) / 720;
            double expected = sum1 + sum2;
            Assert::AreEqual(expected, s(x), 1e-5, L"Test failed for |x| < 1");
        }

        // Main loop test for the range calculation (dummy values, adjust if needed)
        TEST_METHOD(TestRangeCalculation)
        {
            double r_start = 1.0, r_end = 2.0;
            int n = 4;
            double dr = (r_end - r_start) / n;
            double r = r_start;

            for (int i = 0; i <= n; ++i) {
                double result = s(sqrt(r + 1)) - s(sqrt(r - 1)) + 1;
                Assert::IsTrue(result >= 0, L"Result should be non-negative");
                r += dr;
            }
        }
    };
}
