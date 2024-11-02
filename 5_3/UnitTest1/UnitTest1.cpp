// UnitTest1.cpp
#include "pch.h"
#include "CppUnitTest.h"
#include "C:\Users\suka\source\repos\5_3\5_3\5_3.cpp" // включіть ваш основний код сюди

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
    TEST_CLASS(UnitTest1)
    {
    public:

        TEST_METHOD(TestMethod_s)
        {
            Assert::AreEqual(s(2.0), (1 + 2.0 * 2.0) / sqrt(1 + abs(sin(2.0))), 1e-6, L"Failed on s(2.0)");
            Assert::AreEqual(s(0.5), 1.64583, 1e-5, L"Failed on s(0.5)"); 
        }

        TEST_METHOD(TestMethod_CalculateResult)
        {
            double r = 2.0;
            double expected = s(sqrt(r + 1)) - s(sqrt(r - 1)) + 1;
            Assert::AreEqual(expected, s(sqrt(r + 1)) - s(sqrt(r - 1)) + 1, 1e-6, L"Failed on CalculateResult for r = 2.0");
        }
    };
}
