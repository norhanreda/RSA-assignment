import rsa
import pandas as pd
import numpy as np
import decimal 
import time
# def attak(n,c,M,p1,p2):
def attack(C,M, n, e,name):
    d=0
    q=0
    p=0
    for p in range(2, int(decimal.Decimal(n).sqrt())+1): # since n is composite then one of its factors is <=sqrt(n)
        if n % p == 0:
            q = n//p
            e = e
            p = p
            break
    phi=(p-1)*(q-1)    
    e_inv=rsa.mod_inverse(e,phi)
    d = e_inv
    if(M==rsa.decrypt(C,(d,n))):
       # if(person==True):
          print(name,"is attacked hahahahahahahahahah and his private key is:",d)
        # else:
        #   print("second person attacked hahahahahahahahahah")   
    return d


person1 = np.asarray(pd.read_csv('bob.csv',header = None))
person2 =  np.asarray(pd.read_csv('alice.csv',header = None))
# print(person1)
# print(person2)
#print(attack(14,5,20204102439760114506794536222271712090921066214428891483544916759870263304826018689371332058319286973360954858579647965067146810896394940189136672351758095371704155392084170830490668403175532623010582960123535836941747647176442645202281985467206536759656125831169529593986582417358504834327734382187988710708142126938741387171884569385361333547209202935341657114264628852397340404914319273726279683965706321781647252747963762936195254262799322085926582124958095036006667089997159519871357290192258899878534539440949575878305033711339802097911922137239448191068351516669370902665593327056937333629486345436980236459379,7 ,True))
start = time.time()
print(attack(int(person1[2]),int(person1[1]),int(person2[3]),int(person2[0]), str(person2[4])))
end = time.time()
print(end - start)
#print(attack(int(person2[2]),int(person2[1]),int(person1[3]),int(person1[0]),str(person1[4])))