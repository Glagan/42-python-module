import pandas as pd
import matplotlib.pyplot as plt


class Komparator:
    def __init__(self, df):
        self.data = df

    def compare_box_plots(self, categorical_var, numerical_vars):
        if not isinstance(numerical_vars, list):
            numerical_vars = [numerical_vars]
        self.data.boxplot(column=numerical_vars,
                          by=categorical_var, grid=False)
        plt.show()

    def density(self, categorical_var, numerical_var):
        self.data[numerical_var].plot.density()
        plt.legend()
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        self.data.hist(column=numerical_var, by=categorical_var, grid=False)
        plt.show()
