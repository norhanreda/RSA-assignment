from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def plot_attack():
    x=[]
    for i in range(27,36):
        x.append(i)
    #y=[10.996012449264526,20.09508490562439,39.23932504653931,62.10986256599426,281.43727254867554,1043.6157057285309,1876.9959406852722,1986.2639257907867,4889.491338253021 ]
    y=[]
    y=np.asarray(y)
    #y=y/3600
    plt.plot(x, y)
    plt.title("attacking analysis")
    plt.xlabel("numner of bits of key ")
    plt.ylabel("time for attacking in sec")
    plt.show()

plot_attack()   


def plot_encryption_insec():
    x=[]
    for i in range(27,35):
        x.append(i)
    y=[10.996012449264526,20.09508490562439,39.23932504653931,62.10986256599426,281.43727254867554,1043.6157057285309,1876.9959406852722,1986.2639257907867 ]
    plt.plot(x, y)
    plt.title("encryption analysis")
    plt.xlabel("numner of bits of key ")
    plt.ylabel("time for encryption in sec")
    plt.show()

#plot_encryption_insec()   

def plot_decryption_insec():
    x=[]
    for i in range(27,35):
        x.append(i)
    y=[10.996012449264526,20.09508490562439,39.23932504653931,62.10986256599426,281.43727254867554,1043.6157057285309,1876.9959406852722,1986.2639257907867 ]
   
    plt.plot(x, y)
    plt.title("decryption analysis")
    plt.xlabel("numner of bits of key ")
    plt.ylabel("time for decryption in sec")
    plt.show()

#plot_decryption_insec()   