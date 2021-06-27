import pandas as pd
import matplotlib.pyplot as plt


class MyPlotLib:
    def histogram(self, data, features):
        data.hist(column=features)
        plt.show()

    def density(self, data, features):
        data[features].plot.density()
        plt.show()

    def pair_plot(self, data, features):
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    def box_plot(self, data, features):
        data.boxplot(column=features)
        plt.show()
