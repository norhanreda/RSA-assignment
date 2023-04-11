from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def plot_attack():
    x=[]
    for i in range(27,36):
        x.append(i)
    y=[]
    y=np.asarray(y)
    #y=y/3600
    plt.plot(x, y)
    plt.title("attacking analysis")
    plt.xlabel("key size in bits")
    plt.ylabel("time for attacking in sec")
    plt.show()

# plot_attack()   


def plot_encryption():
    x=[32,64,128,256,512,1024]
   
    y=[0.0,0.0009999275207519531,0.0009937286376953125,0.0009791851043701172,0.002000570297241211,0.007999420166015625]
    plt.plot(x, y)
    plt.title("encryption analysis")
    plt.xlabel("key size in bits ")
    plt.ylabel("time for encryption in sec")
    plt.show()

plot_encryption()   

def plot_decryption():
    x=[32,64,128,256,512,1024]
   
    y=[0.0,0.0,0.0,0.0009984970092773438,0.001375436782836914,0.007000446319580078]
   
    plt.plot(x, y)
    plt.title("decryption analysis")
    plt.xlabel("key size in bits")
    plt.ylabel("time for decryption in sec")
    plt.show()

plot_decryption()   