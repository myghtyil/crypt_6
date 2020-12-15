import random as rnd
import math
import time
from progress.bar import ChargingBar



def prost(a):
    for i in range(int(math.sqrt(a))):
        if  i > 1:
            if a % i == 0:
                return False
    return True

def vz_prost(a, b):
    if a >= b:
        if prost(a):
            return True
        for i in range(b):
            if i > 1:
                if a % i == 0 and b % i == 0:
                    return False
        return True
    else:
        if prost(b):
            return True
        for i in range(a):
            if i > 1:
                if a % i == 0 and b % i == 0:
                    return False
        return True

def step_po_mod(e,stepen,mod):
    sum_steps = 0
    ost = {}
    ost[0] = e % mod
    est_li_st = {}
    otv = 1
    max_st = int(math.log(stepen,2))
    for i in range(max_st,-1,-1):
        if (sum_steps + 2**i <= stepen):
            est_li_st[i] = 1 
            sum_steps += 2**i
        else:
            est_li_st[i] = 0
            
    for i in range(1,max_st + 1):
        ost[i] = (ost[i-1]**2) % mod
        
    for i in range(0,max_st + 1):
        if est_li_st[i] == 1 :
            otv = (otv * ost[i]) % mod
        #print (2**i,"  -  ",est_li_st[i],"  -  ",ost[i])
        
    return otv



def key_gen(): # shared - n, open_key - e,secret_key - d
    global shared_key
    global open_key
    global secret_key

    bar = ChargingBar('Генерация ключей', max = 3)
    while True:
        p = rnd.randint(50,1000)
        if prost(p) == True:
            break
    bar.next()
    time.sleep(1)
    while True:
        q = rnd.randint(50,1000)
        if prost(q) == True:
            break     
    shared_key = p * q                      # общая часть ключа
    pq = (p-1)*(q-1)
    bar.next()
    time.sleep(1)
    while True:                  
        d = rnd.randint(50,10000)
        if vz_prost(d,pq) == True:
            break
    secret_key = d                          # часть секретного ключа
    
    sootv_usl = [e for e in range(50,10000000) if (e * d) % pq == 1]
    open_key = rnd.choice(sootv_usl)     # часть открытого ключа
    bar.next()
    time.sleep(1)
    bar.finish()
    print ("Открытый ключ: {",open_key,",",shared_key,"}")
    print ("Секретный ключ: {",secret_key,",",shared_key,"}")
    
def zash(in_string,key,shared):
    shifr = {}
    for i in range(len(in_string)):
        shifr[i] = step_po_mod(ord(in_string[i]),key,shared)
    return shifr

def rassh(signature,key,shared):
    desh = ''
    for i in range(len(signature)):
        desh += chr(step_po_mod(signature[i],key,shared))
    return desh
    
shared_key = 0
open_key = 0 
secret_key = 0
