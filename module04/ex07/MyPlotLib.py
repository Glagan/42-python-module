import pandas as pd
import matplotlib.pyplot as plt


class MyPlotLib:
    def histogram(self, data: pd.DataFrame, features: list):
        if not isinstance(data, pd.DataFrame):
            return
        if not isinstance(features, list) or len(features) == 0:
            return
        try:
            data.hist(column=features)
            plt.show()
        except BaseException as error:
            print("Failed to display histogram: {}".format(error))

    def density(self, data: pd.DataFrame, features: list):
        if not isinstance(data, pd.DataFrame):
            return
        if not isinstance(features, list) or len(features) == 0:
            return
        try:
            data[features].plot.density()
            plt.show()
        except BaseException as error:
            print("Failed to display density: {}".format(error))

    def pair_plot(self, data: pd.DataFrame, features: list):
        if not isinstance(data, pd.DataFrame):
            return
        if not isinstance(features, list) or len(features) == 0:
            return
        try:
            pd.plotting.scatter_matrix(data[features])
            plt.show()
        except BaseException as error:
            print("Failed to display pair plot: {}".format(error))

    def box_plot(self, data: pd.DataFrame, features: list):
        if not isinstance(data, pd.DataFrame):
            return
        if not isinstance(features, list) or len(features) == 0:
            return
        try:
            data.boxplot(column=features)
            plt.show()
        except BaseException as error:
            print("Failed to display box plot: {}".format(error))
