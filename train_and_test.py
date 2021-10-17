import json
import joblib
import sklearn
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn import preprocessing
import numpy as np
import pandas as pd
import os
import collections
from collections import Counter
#import keras
#from keras.models import load_model
def add_X_train_p():
    for i in range(len(a1)):
        X_train_host.append(repr(a1[i]['host']))
        X_train_ts.append(a1[i]['@timestamp'])
        X_train_destination.append(repr(a1[i]['destination']))
        X_train_type.append(repr(a1[i]['type']))
       # X_train_flow.append(repr(a1[i]['flow']))
        X_train_source.append(repr(a1[i]['source']))
        X_train_event.append(repr(a1[i]['event']))
        X_train_network.append(repr(a1[i]['network']))

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

def add_X_train_w():
    for i in range(len(a1)):
        X_train_ts2.append(repr(a1[i]['@timestamp']))
        X_train_winlog.append(repr(a1[i]['winlog']))
        X_train_event2.append(repr(a1[i]['event']))

def add_X_test_w():
    for i in range(len(a1)):
        X_test_ts2.append(repr(a1[i]['@timestamp']))
        X_test_winlog.append(repr(a1[i]['winlog']))
        X_test_event2.append(repr(a1[i]['event']))
#for packetbeat
X_train_host=[]
X_train_ts=[]
X_train_destination=[]
X_train_type=[]
X_train_flow=[]
X_train_source=[]
X_train_event=[]
X_train_network=[]
#for winlogbeat
X_train_ts2=[]
X_train_winlog=[]
X_train_event2=[]
#type
Y_train=[]
Y_train2=[]

num=-1000000
#FOR PACKETBEAT
#load attack 1 logs
count=0
a1=[]
for line in open('Train/Attack_1/packetbeat.json','r'):
    a1.append(json.loads(line))
    #print(lines)
    #print()
    count+=1
    if count==num:
        break
#print(len(a1))
#print(a1[0]['@timestamp'])
#a1_keys=[]
#a1_keys=a1[0].keys()
#print(a1_keys)
add_X_train_p()
count=0
for i in range(len(a1)):
    Y_train.append('attack 1')
    count+=1
    if count==num:
        break

print('attack 1')
#print(X_train_destination)
#load attack 2 logs
count=0
a1=[]
for line in open('Train/Attack_2/packetbeat.json','r'):
    a1.append(json.loads(line))
    count+=1
    if count==num:
        break
'''print(a1[0]['type'])
a1_keys=[]
a1_keys=a1[0].keys()
print(a1_keys)'''
add_X_train_p()
count=0
for i in range(len(a1)):
    Y_train.append('attack 2')
    count+=1
    if count==num:
        break
print('attack 2')


#load attack 3 logs
count=0
a1=[]
for line in open('Train/Attack_3/packetbeat.json','r'):
    a1.append(json.loads(line))
    count+=1
    if count==num:
        break
add_X_train_p()
count=0
for i in range(len(a1)):
    Y_train.append('attack 3')
    count+=1
    if count==num:
        break
print('attack 3')

#load attack 4 logs
count=0
a1=[]
for line in open('Train/Attack_4/packetbeat.json','r'):
    a1.append(json.loads(line))
    count+=1
    if count==num:
        break
add_X_train_p()
count=0
for i in range(len(a1)):
    Y_train.append('attack 4')
    count+=1
    if count==num:
       break
print('attack 4')

#load attack 5 logs
count=0
a1=[]
for line in open('Train/Attack_5/packetbeat.json','r'):
    a1.append(json.loads(line))
    count+=1
    if count==num:
        break
add_X_train_p()
count=0
for i in range(len(a1)):
    Y_train.append('attack 5')
    count+=1
    if count==num:
        break
print('attack 5')


#FOR WINLOGBEAT
#load attack 1 logs
count=0
a1=[]
for line in open('Train/Attack_1/winlogbeat.json','r'):
    a1.append(json.loads(line))
    #print(lines)
    #print()
    count+=1
    if count==num:
        break
#print(len(a1))
#print(a1[0]['@timestamp'])
#print(a1)
#a1_keys=[]
#a1_keys=a1[0].keys()
#print(a1_keys)
add_X_train_w()
count=0
for i in range(len(a1)):
    Y_train2.append('attack 1')
    count+=1
    if count==num:
        break
print('attack 1')
#print(X_train_host)
#load attack 2 logs
count=0
a1=[]
for line in open('Train/Attack_2/winlogbeat.json','r'):
    a1.append(json.loads(line))
    count+=1
    if count==num:
        break

add_X_train_w()
count=0
for i in range(len(a1)):
    Y_train2.append('attack 2')
    count+=1
    if count==num:
        break
print('attack 2')


#load attack 3 logs
count=0
a1=[]
for line in open('Train/Attack_3/winlogbeat.json','r'):
    a1.append(json.loads(line))
    count+=1
    if count==num:
       break
add_X_train_w()
count=0
for i in range(len(a1)):
    Y_train2.append('attack 3')
    count+=1
    if count==num:
        break
print('attack 3')

#load attack 4 logs
count=0
a1=[]
for line in open('Train/Attack_4/winlogbeat.json','r'):
    a1.append(json.loads(line))
    count+=1
    if count==num:
       break
add_X_train_w()
count=0
for i in range(len(a1)):
    Y_train2.append('attack 4')
    count+=1
    if count==num:
        break
print('attack 4')

#load attack 5 logs
count=0
a1=[]
for line in open('Train/Attack_5/winlogbeat.json','r'):
    a1.append(json.loads(line))
    count+=1
    if count==num:
        break
add_X_train_w()
count=0
for i in range(len(a1)):
    Y_train2.append('attack 5')
    count+=1
    if count==num:
        break
print('attack 5')

#for s in X_train_host:
    #s=float(s)
X_train_host2d=np.reshape(X_train_host,(-1,1))
#X_train_host2d = [[len(x[0]), len(x[0].split())] for x in X_train_host2d]
#print(X_train_host2d)
#print(Y_train)

#TRAIN
model1 = make_pipeline(TfidfVectorizer(), DecisionTreeClassifier())
model1.fit(X_train_destination, Y_train)
#model1.save('my_model1.h5') 
joblib.dump(model1, 'my_model1')
model2 = make_pipeline(TfidfVectorizer(), DecisionTreeClassifier())
model2.fit(X_train_type, Y_train)
#model2.save('my_model2.h5') 
joblib.dump(model2, 'my_model2')
model3 = make_pipeline(TfidfVectorizer(), DecisionTreeClassifier())
model3.fit(X_train_event, Y_train)
#model3.save('my_model3.h5')
joblib.dump(model3, 'my_model3')
model4 = make_pipeline(TfidfVectorizer(), DecisionTreeClassifier())
model4.fit(X_train_source, Y_train)
#model4.save('my_model4.h5') 
joblib.dump(model4, 'my_model4')
model5 = make_pipeline(TfidfVectorizer(), DecisionTreeClassifier())
model5.fit(X_train_network, Y_train)
#model5.save('my_model5.h5') 
joblib.dump(model5, 'my_model5')
model6 = make_pipeline(TfidfVectorizer(), DecisionTreeClassifier())
model6.fit(X_train_winlog, Y_train2)
#model6.save('my_model6.h5') 
joblib.dump(model6, 'my_model6')
model7 = make_pipeline(TfidfVectorizer(), DecisionTreeClassifier())
model7.fit(X_train_event2, Y_train2)
#model7.save('my_model7.h5') 
joblib.dump(model7, 'my_model7')

#TEST
print("path: ")
folder=input()
cases=os.listdir(folder)
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
    print(c)
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
    print(Counter(psum).most_common(1)[0][0])


