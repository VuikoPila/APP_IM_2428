#include "pch.h"
#include "CppUnitTest.h"
#include <cmath>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

double S0(const int K, const int N);
double S1(const int K, const int N, const int i);
double S2(const int K, const int N, const int i);
double S3(const int K, const int N, const int i, double t);
double S4(const int K, const int N, const int i, double t);

namespace UnitTest
{
    TEST_CLASS(UnitTest1)
    {
    public:

        TEST_METHOD(TestS0)
        {
            Assert::AreEqual(5.0, S0(1, 5), 1e-6);
            Assert::AreEqual(4.25, S0(2, 4), 1e-6);
        }

        TEST_METHOD(TestS1)
        {
            Assert::AreEqual(5.0, S1(1, 5, 1), 1e-6);
            Assert::AreEqual(4.25, S1(2, 4, 2), 1e-6);
        }

        TEST_METHOD(TestS2)
        {
            Assert::AreEqual(5.0, S2(1, 5, 5), 1e-6);
            Assert::AreEqual(4.25, S2(2, 4, 4), 1e-6);
        }

        TEST_METHOD(TestS3)
        {
            Assert::AreEqual(5.0, S3(1, 5, 1, 0), 1e-6);
            Assert::AreEqual(4.25, S3(2, 4, 2, 0), 1e-6);
        }

        TEST_METHOD(TestS4)
        {
            Assert::AreEqual(5.0, S4(1, 5, 5, 0), 1e-6);
            Assert::AreEqual(4.25, S4(2, 4, 4, 0), 1e-6);
        }
    };
}
