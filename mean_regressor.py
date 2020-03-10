import pandas as pd
import numpy as np


class MeanRegressor:

    def fit(self, X, y):
        self.y_mean = np.mean(y)

    def predict(self, X):
        y_means = []
        for _ in range(len(X.iloc[:, 0])):
            y_means.append(self.y_mean)
        return y_means

    def score(self, X, y):
        y = np.array(y)
        y_pred = self.predict(X)
        rss = 0
        tss = 0
        for i in range(0, len(X.iloc[:, 0])):
            rss += (y[i] - y_pred[i])**2
            tss += (y[i] - np.mean(y))**2
            print(rss, tss)
        print(rss)
        return 1 - (rss/tss)
