import sys
import json
import numpy as np
import pandas as pd
import os
import collections
from collections import Counter
import joblib
import sklearn 
from sklearn import utils
def add_X_test_p():
    for i in range(len(a1)):
        X_test_host.append(repr(a1[i]['host']))
        X_test_ts.append(repr(a1[i]['@timestamp']))
        X_test_destination.append(repr(a1[i]['destination']))
        X_test_type.append(repr(a1[i]['type']))
       # X_test_flow.append(repr(a1[i]['flow']))
        X_test_source.append(repr(a1[i]['source']))
        X_test_event.append(repr(a1[i]['event']))
        X_test_network.append(repr(a1[i]['network']))
def add_X_test_w():
    for i in range(len(a1)):
        X_test_ts2.append(repr(a1[i]['@timestamp']))
        X_test_winlog.append(repr(a1[i]['winlog']))
        X_test_event2.append(repr(a1[i]['event']))
#print("path: ")
#folder=input()
folder=sys.argv[1]
num=-1000000
model1 = joblib.load('my_model1')
model2 = joblib.load('my_model2')
model3 = joblib.load('my_model3')
model4 = joblib.load('my_model4')
model5 = joblib.load('my_model5')
model6 = joblib.load('my_model6')
model7 = joblib.load('my_model7')
#TEST
cases=os.listdir(folder)
cases.sort()
#count2=0
for c in cases:
    a1=[]
    X_test_host=[]
    X_test_ts=[]
    X_test_destination=[]
    X_test_type=[]
    X_test_flow=[]
    X_test_source=[]
    X_test_event=[]
    X_test_network=[]
    X_test_ts2=[]
    X_test_winlog=[]
    X_test_event2=[]
    #count2+=1
    #if count2==3:
    #    continue
    count=0
    #print(c)
    for line in open(folder+'/'+c+'/packetbeat.json','r'):
         a1.append(json.loads(line))
         count+=1
         if count==num:
            break
    
    #a1_keys=[]
    #a1_keys=a1[0].keys()
    #print(a1_keys)
    add_X_test_p()
    count=0
    a1=[]
    for line2 in open(folder+'/'+c+'/winlogbeat.json','r'):
         a1.append(json.loads(line2))
         count+=1
         if count==num:
            break
  #  a1_keys=[]
  #  a1_keys=a1[0].keys()
  #  print(a1_keys)
    add_X_test_w()
    #for s in X_test_host:
        #s=float(s)
    #X_test_host2d=np.reshape(X_test_host,(-1,1))
    #X_test_host2d = [[len(x[0]), len(x[0].split())] for x in X_test_host2d]
    #enc=preprocessing.LabelEncoder()
    #model=MultinomialNB()
    
    p1=model1.predict(X_test_destination)
    p2=model2.predict(X_test_type)
    p3=model3.predict(X_test_event)
    p4=model4.predict(X_test_source)
    p5=model5.predict(X_test_network)
    p6=model6.predict(X_test_winlog)
    p7=model7.predict(X_test_event2)

    psum=np.concatenate((p1,p2,p3,p4,p5,p6,p7),axis=0)
    #print(psum)
    id=c.split("Test_")[1]
    print('testcase '+id+': '+Counter(psum).most_common(1)[0][0])
