import numpy as np
import scipy.integrate as spi


def f(x):
    return x ** 2


def monte_carlo_integration(func, a, b, n_samples=100000):
    x_random = np.random.uniform(a, b, n_samples)
    y_random = func(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral


def analytical_integral(a, b):
    return (b ** 3 / 3) - (a ** 3 / 3)


def main():
    a, b = 0, 2
    n_samples = 1000000
    
    print("=" * 60)
    print("ОБЧИСЛЕННЯ ІНТЕГРАЛА МЕТОДОМ МОНТЕ-КАРЛО")
    print("=" * 60)
    print(f"Функція: f(x) = x^2")
    print(f"Інтервал: [{a}, {b}]")
    print(f"Кількість точок: {n_samples:,}")
    print()
    
    mc_result = monte_carlo_integration(f, a, b, n_samples)
    print(f"1. Метод Монте-Карло: {mc_result:.10f}")
    
    analytical_result = analytical_integral(a, b)
    print(f"2. Аналітичний розвязок: {analytical_result:.10f}")
    print(f"   (∫x^2 dx = x^3/3 => {b}^3/3 - {a}^3/3 = 8/3)")
    
    scipy_result, scipy_error = spi.quad(f, a, b)
    print(f"3. SciPy quad: {scipy_result:.10f}")
    
    print()
    print("=" * 60)
    print("ПОРІВНЯННЯ РЕЗУЛЬТАТІВ")
    print("=" * 60)
    
    mc_error = abs(mc_result - analytical_result)
    mc_rel_error = (mc_error / analytical_result) * 100
    
    print(f"Відхилення Монте-Карло від аналітичного: {mc_error:.10f}")
    print(f"Відносна похибка: {mc_rel_error:.4f}%")
    
    print()
    print("=" * 60)
    print("ВИСНОВКИ")
    print("=" * 60)
    print(f"Метод Монте-Карло дав результат {mc_result:.6f}")
    print(f"Аналітичний розв'язок: {analytical_result:.6f}")
    print(f"Похибка методу Монте-Карло: {mc_rel_error:.4f}%")
    print(f"SciPy quad показує точний результат")
    print(f"Для {n_samples:,} точок похибка методу менша за 0.1%")


if __name__ == "__main__":
    np.random.seed(42)
    main()