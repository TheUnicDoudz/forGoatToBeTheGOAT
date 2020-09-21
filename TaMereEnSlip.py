import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    alpha = 0.1

    data = pd.read_csv("iris.csv", sep=",")

    data = data.sample(frac=1)
    data_train = data[:int(80 * 150 / 100)]
    data_test = data[int(80 * 150 / 100):]

    Number_per_class = data.Class.value_counts()

    Class_count = len(data.Class.value_counts())

    data_count = Number_per_class.sum()
    N = data_count
    N_train = len(data_train)
    N_test = N - N_train

    Class_indices_pd = data.Class
    one_hot_indice_pd = np.zeros((N, 3))
    Class_indices_pd = pd.factorize(Class_indices_pd)
    for idx, i in enumerate(Class_indices_pd[0]):
        one_hot_indice_pd[idx][i] = 1

    Class_indices = Class_indices_pd[0]
    T_train = Class_indices[:int(80 * 150 / 100)]
    T_test = Class_indices[int(80 * 150 / 100):]

    X_train = data_train[data_train.columns.difference(["Class"])]
    X_train = X_train.to_numpy()
    Biais = np.ones((N_train, 1))
    X_train = np.concatenate((Biais, X_train), axis=1)

    X_test = data_test[data_test.columns.difference(["Class"])]
    X_test = X_test.to_numpy()
    Biais = np.ones((N_test, 1))
    X_test = np.concatenate((Biais, X_test), axis=1)

    W = np.random.rand(5, 3)
    W = W.T

    k = 0
    y_train = np.zeros((N_train, 3))

    while k < 100:
        k = k + 1
        for n in range(0, N_train):
            y = np.dot(W, X_train[n])
            y_train[n] = y
            j = np.argmax(y)
            if j != T_train[n]:
                for i in range(3) :
                    for l in range(5) :
                        W[i,l] = W[i, l] + alpha*(one_hot_indice_pd[n, i] - y[i])*X_train[n, l]

    y = (np.dot(W, X_test.T))
    y = y.T
    y_class = np.zeros(len(y))
    for i in range(len(y)):
        y_class[i] = np.argmax(y[i])

    # error_test = T_test != y_class
    # error_test = error_test.astype(int).sum()
    # error_train = T_train != y_train
    # error_train = error_train.astype(int).sum()
    # print("Pourcentage de précision test : ", (N_test - error_test) * 100 / N_test)
    # print("Pourcentage de précision train : ", (N_train - error_train) * 100 / N_train)
