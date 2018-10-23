#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time


# In[ ]:


def find_c(dic,long,min_sup):
    tmp_list=[]
    output={}
    
    #---dict變成list
    for key in dic.keys():
        tmp_list.append(key)  
    #print(tmp_list)
    
    
    #--------找candidate
    for i in range(0,len(tmp_list)):
        for j in range(i+1,len(tmp_list)):
            for k in range(0,long-1):
                #print(i,j,k,tmp_list[i],tmp_list[j])
                if tmp_list[i][k]==tmp_list[j][k] and k!=long-2:
                    #print("hihi")
                    continue
                if tmp_list[i][k]==tmp_list[j][k] and k==long-2:
                    #print("stop")
                    #print(i,j,k,tmp_list[i],tmp_list[j])
                    if tmp_list[i][k+1]>tmp_list[j][k+1]:
                        #print(list(tmp_list[j]),tmp_list[i][k+1])
                        tmp=list(tmp_list[j])
                        tmp.append(tmp_list[i][k+1])
                        output[tuple(tmp)]=0
                        #print(tmp)
                    else:
                        tmp=list(tmp_list[i])
                        tmp.append(tmp_list[j][k+1])
                        output[tuple(tmp)]=0
                        #print(tmp)                
                else:
                    break
                        
    #-------數有幾個
    for key in output.keys():
        for value in database.values():
            #print(set(key),set(value))
            if set(key).issubset(set(value)):
                #print("找到")
                output[key]+=1
    #print(output)
                
    #------刪除低於min_sup
    #print("min_sup",min_sup)
    #print("output",output)
    remove=[]
    for key in output.keys():
        if output[key]<min_sup:
            remove.append(key)
    #print("remove",remove)
    for i in remove:
        output.pop(i)
    
    #-------return
    return (output)


# In[ ]:


def find_L1(database,min_sup):    
    L1={}
    for key in database.keys():
        for item in database[key]:
            if item in L1:
                L1[item]=L1[item]+1
            else:
                L1[item]=1
            #print(item)
    #print(L1)
    remove=[]
    for key in L1.keys():
        if L1[key]<min_sup:
            remove.append(key)
    for i in remove:
        L1.pop
    return L1
    #print("remove",remove)
    #print(L1)


# In[ ]:


def find_L2(database,min_sup):    
    L2={}
    for i in L1.keys():
        for j in L1.keys():
            if j>i:
                #print(i,j)
                L2[(i,j)]=0

    #print(L2)
    for key in L2.keys():
        for value in database.values():
        #print(key)
            if set(key).issubset(set(value)):
                L2[key]+=1
                #print(key,value)
    #print(L2)
    remove=[]
    for key in L2.keys():
        if L2[key] < min_sup:
            remove.append(key)
    for i in remove:
        L2.pop(i)
    return L2
    #print(remove)
    #print(L2) 


# In[ ]:


#讀檔
f=open("data2.data",'r')
database={}
for line in f.readlines():
    n1,n2,n3=(int(s) for s in line.split())
    #print(n1,n2,n3)
    if n2 in database:
        database[n2].append(n3)
    else:
        database[n2]=[n3]
#print(database)


# In[ ]:


#min_sup=90
for i in range(10,11):
    min_sup=i*10
    print("min_sup",min_sup)
    tStart = time.time()
    L1=find_L1(database,min_sup)
    #print(L1)
    L2=find_L2(database,min_sup)
    #print(L2)
    List=L2
    for i in range(2,20):
        new_List=find_c(List,i,min_sup)
        if new_List=={}:
            break
        #print("new_list:",new_List,i)
        List=new_List
    tEnd = time.time()#計時結束
    print ("花了 %f 秒" % (tEnd - tStart))

