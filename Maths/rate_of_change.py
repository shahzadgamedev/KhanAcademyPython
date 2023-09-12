import numpy as np
import matplotlib.pyplot as plt


# linear function of same average rate of change
def linear_distance(x):
    return np.add(np.multiply(x, 3), 1)


def linear_distance_inverse(y):
    return np.divide(np.subtract(y, 1), 3)


# quadratic function of different average rate of change
def quadratic_distance(x):
    return np.add(np.power(x, 2), 1)


def quadratic_distance_inverse(y):
    return np.sqrt(np.subtract(y, 1))


def determineSlope(algebraic_func, minimum=1, maximum=2):
    one = algebraic_func(minimum)
    two = algebraic_func(maximum)
    print(f"Rate of change is between no{minimum} and {maximum} is: ", two - one)
    return two - one


def main():
    test_data = np.arange(1, 10, 1)
    y_values = quadratic_distance(test_data)
    y_inverse = quadratic_distance_inverse(test_data)

    # show plot x-axis from 0 to 3 and y-axis from 0 to 10
    plt.plot(test_data, y_values)
    plt.plot(test_data, y_inverse)
    plt.axis([1, 10, 1, 10])
    # shop a point on the graph
    plt.show()


if __name__ == '__main__':
    main()
