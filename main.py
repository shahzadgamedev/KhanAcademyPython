import numpy
import matplotlib.pyplot as plt

economyData = numpy.array([5, 4, 3, 2, 1, 0])
economyDataObjectives = numpy.array([0, 100, 180, 240, 280, 300])


def createEconomyGraph(input_economy_data, input_economyDataObjectives):
    plt.plot(input_economy_data, input_economyDataObjectives)

    # get area under curve and fill it with transparent pink
    plt.fill_between(input_economy_data, input_economyDataObjectives, color='pink', alpha=0.5)

    # label the area under curve
    plt.text(1.5, 150, 'Possible \n (but not efficient)', horizontalalignment='center', fontsize=10)

    # get area over curve and fill it with transparent blue
    plt.fill_between(input_economy_data, input_economyDataObjectives.max(), input_economyDataObjectives, color='blue',
                     alpha=0.5)

    # label the area over curve
    plt.text(3.5, 250, 'Impossible', horizontalalignment='center', fontsize=10)

    plt.scatter(input_economy_data, input_economyDataObjectives, color='black')

    y_offset = 0.2
    x_offset = 0.2

    # label the points
    plt.text(0 + x_offset, 300 + y_offset, 'A', horizontalalignment='center', fontsize=10)
    plt.text(1 + x_offset, 280 + y_offset, 'B', horizontalalignment='center', fontsize=10)
    plt.text(2 + x_offset, 240 + y_offset, 'C', horizontalalignment='center', fontsize=10)
    plt.text(3 + x_offset, 180 + y_offset, 'D', horizontalalignment='center', fontsize=10)
    plt.text(4 + x_offset, 100 + y_offset, 'E', horizontalalignment='center', fontsize=10)
    plt.text(5 + x_offset, 0 + y_offset, 'F', horizontalalignment='center', fontsize=10)

    plt.xlabel('Rabbits Hunting')
    plt.ylabel('Berries Gathering')


def find_Slope(x1, y1, x2, y2):
    inner_slope = (y2 - y1) / (x2 - x1)
    # mark the horizontal and vertical line of slope
    plt.plot([x1, x2], [y1, y1], color='red', linestyle='--', linewidth=1)
    plt.plot([x2, x2], [y1, y2], color='red', linestyle='-.', linewidth=1)

    return inner_slope


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createEconomyGraph(economyData, economyDataObjectives)
    slope = find_Slope(2, 240, 1, 280)
    plt.show()
    print(slope)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
