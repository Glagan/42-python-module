import pandas as pd
import matplotlib.pyplot as plt


class Komparator:
    def __init__(self, df: pd.DataFrame):
        self.data = df

    def compare_box_plots(self, categorical_var: str, numerical_vars):
        if not isinstance(self.data, pd.DataFrame):
            print("data is not a DataFrame")
            return
        if not isinstance(numerical_vars, list):
            numerical_vars = [numerical_vars]
        try:
            self.data.boxplot(column=numerical_vars,
                              by=categorical_var,
                              grid=False)
            plt.show()
        except BaseException:
            return

    def density(self, categorical_var: str, numerical_var):
        if not isinstance(self.data, pd.DataFrame):
            print("data is not a DataFrame")
            return
        if not isinstance(numerical_var, str):
            print("numerical var needs to be a string")
            return
        try:
            self.data.groupby(categorical_var)[numerical_var].plot.density(legend=True,
                                                                           xlabel=numerical_var,
                                                                           title='{} density by {}'.format(numerical_var, categorical_var),)
            plt.show()
        except BaseException:
            return

    def compare_histograms(self, categorical_var: str, numerical_var):
        if not isinstance(self.data, pd.DataFrame):
            print("data is not a DataFrame")
            return
        if not isinstance(numerical_var, str):
            print("numerical var needs to be a string")
            return
        try:
            self.data.groupby(categorical_var)[numerical_var].plot.hist(legend=True,
                                                                        xlabel=numerical_var,
                                                                        title='{} density by {}'.format(numerical_var, categorical_var),
                                                                        grid=False,
                                                                        stacked=True,
                                                                        alpha=0.5)
            plt.show()
        except BaseException:
            return
