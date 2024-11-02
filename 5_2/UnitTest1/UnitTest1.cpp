#include "pch.h"
#include "CppUnitTest.h"
#include "C:\Users\suka\source\repos\5_2\5_2\5_2.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
    TEST_CLASS(UnitTest1)
    {
    public:

        TEST_METHOD(TestSFunction)
        {
            // Тестові значення
            double x = 2.0;
            double eps = 1e-6;
            double s = 0.0;
            int n = 0;

            // Очікуване значення, використовуючи точне значення arctg(x)
            double expectedValue = atan(x);

            // Виклик функції S для обчислення значення ряду Тейлора
            S(x, eps, n, s);

            // Перевірка, чи значення, обчислене через ряд Тейлора, є близьким до точного значення
            Assert::AreEqual(expectedValue, s, eps, L"Результат не відповідає очікуваному значенню.");
        }
    };
}
