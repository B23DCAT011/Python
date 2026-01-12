from cProfile import label

import numpy as np
import pandas as pd
from pkg_resources import non_empty_lines
from pyexpat.errors import XML_ERROR_INCORRECT_ENCODING


class DecisionTree:
    def __init__(self,depth=5,min_leaf_size=5):
        self.depth = depth
        self.min_leaf_size = min_leaf_size #so mau toi thieu o moi la
        self.decision_boundary = None
        self.left = None
        self.right = None
        self.predict = None

    def mean_squared_error(self,labels,prediction):
        return np.mean((labels-prediction)**2)

    def train(self,x,y):
        if x.ndim != 1:
            raise ValueError("Input data x must be one-dimensional")

        if y.ndim != 1:
            raise  ValueError("Input date y must be one=dimensional")

        if len(x)!=len(y):
            raise ValueError("x and y must have the same length")


        if len(x) < self.min_leaf_size*2:
            self.predict = np.mean(y)
            return

        if self.depth <= 1:
            self.predict = np.mean(y)
            return


        best_split = None
        min_error = self.mean_squared_error(y,np.mean(y))*2

        for i in range(len(x)):
            if len(x[:i]) < self.min_leaf_size:
                continue
            if len(x[i:]) < self.min_leaf_size:
                continue

            error_left = self.mean_squared_error(y[:i],np.mean(y))
            error_right = self.mean_squared_error(y[i:],np.mean(y))
            error = error_left + error_right

            if error < min_error:
                min_error = error
                best_split = i

        if best_split:
            left_x = x[:best_split]
            left_y = y[:best_split]
            right_x = x[best_split:]
            right_y = y[best_split:]

            self.decision_boundary = x[best_split]
            self.left = DecisionTree(depth=self.depth-1,min_leaf_size=self.min_leaf_size)
            self.right = DecisionTree(depth=self.depth-1,min_leaf_size=self.min_leaf_size)

            self.left.train(left_x,left_y)
            self.left.train(right_x,right_y)
        else:
            self.predict = np.mean(y)

        return

    def prediction(self,x):
        if self.predict is not None:
            return self.predict
        elif self.left is not None and self.right is not None:
            if x >= self.decision_boundary:
                return self.left.prediction(x)
            else:
                return self.left.prediction(x)
        else:
            raise ValueError("Decision tree not yet trained")







def main():
    x = np.arange(-1.0, 1.0, 0.005)
    y = np.sin(x)

    tree = DecisionTree(depth=10, min_leaf_size=10)
    tree.train(x, y)

    rng = np.random.default_rng()
    test_cases = (rng.random(10) * 2) - 1
    predictions = np.array([tree.prediction(x) for x in test_cases])
    avg_error = np.mean((predictions - test_cases) ** 2)

    print("Test values: " + str(test_cases))
    print("Predictions: " + str(predictions))
    print("Average error: " + str(avg_error))


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod(name="mean_squared_error", verbose=True)