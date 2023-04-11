from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def plot_attack():
    x=[]
    for i in range(27,51):
        x.append(i)
    x.append(64)    
    y=[0.001996278762817383,0.0015094280242919922,0.0029964447021484375,0.002978801727294922,0.00099945068359375,0.01000070571899414,0.0029969215393066406,0.009166955947875977,0.0034720897674560547 ,0.008999109268188477,0.009996414184570312,0.017999887466430664,0.02700018882751465,0.03399991989135742,0.03800559043884277,0.09052467346191406,0.08600139617919922,0.1249992847442627,0.3231937885284424,0.3862457275390625,0.32400059700012207,0.5685150623321533,0.800532341003418,0.8834793567657471,450.41779351234436      ]
    y=np.asarray(y)
    #y=y/3600
    plt.plot(x, y)
    plt.title("attacking analysis")
    plt.xlabel("key size in bits")
    plt.ylabel("time for attacking in sec")
    plt.show()

plot_attack()   


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