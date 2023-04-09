from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def plot_attack():
    x=[]
    for i in range(27,35):
        x.append(i)
    y=[10.996012449264526,20.09508490562439,39.23932504653931,62.10986256599426,281.43727254867554,1043.6157057285309,1876.9959406852722,1986.2639257907867 ]
    plt.plot(x, y)
    plt.show()

plot_attack()    