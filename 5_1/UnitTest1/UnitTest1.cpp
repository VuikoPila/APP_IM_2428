// UnitTest1.cpp
#include "pch.h"
#include "CppUnitTest.h"
#include "lab5_1.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:

		TEST_METHOD(TestMethod_g)
		{
			// Тестуємо функцію g з конкретними значеннями
			Assert::AreEqual(g(2.0, 3.0), sin(2.0 * 3.0) / (pow(2.0, 2) * pow(3.0, 2)), 1e-6, L"Failed on g(2.0, 3.0)");
			Assert::AreEqual(g(1.0, 1.0), sin(1.0 * 1.0) / (pow(1.0, 2) * pow(1.0, 2)), 1e-6, L"Failed on g(1.0, 1.0)");
		}

		TEST_METHOD(TestMethod_calculate_c)
		{
			// Перевіряємо обчислення змінної c для заданих значень s та t
			double s = 2.0;
			double t = 3.0;
			double expected_c = (g(pow(s, 2), t + 1) + g(pow(t, 2), s + 1)) / (1 + pow(g(s + t, s * t), 2));

			// Виконуємо обчислення з тими ж вхідними даними
			double result_c = calculate_c(s, t);

			Assert::AreEqual(result_c, expected_c, 1e-6, L"Failed on calculate_c with s = 2.0 and t = 3.0");
		}
	};
}
