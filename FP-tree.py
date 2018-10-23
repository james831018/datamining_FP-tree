#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self,name,value=0,child=[],parent=None):
        self.name=name
        self.value = value
        self.child=child
        self.parent=parent


# In[ ]:


def build_tree(root,l,num,node_dict):
    #print("root.name",root.name,"(",root.value,")",l)
    if l==[]:
        return
    if root.child==[]:
        #print("not in")
        new_node=Node(l[0],num,[],root)
        if l[0] in node_dict:
            node_dict[l[0]].append(new_node)
        else:
            node_dict[l[0]]=[new_node]
        root.child.append(new_node)
        #print(root.child[0].name,":",root.child[0].value,root.child[0].parent.name,":",root.child[0].parent.value)
        build_tree(new_node,l[1:],num,node_dict)
    else:
        finded=0
        for j in range(0,len(root.child)):
            #print("不是空集合，現在的child",root.child[j].name,"j=",j)
            if l[0]==root.child[j].name:
                #print("in",l[0])
                finded=1
                root.child[j].value+=num
                build_tree(root.child[j],l[1:],num,node_dict)
        if finded==0:
            #print("創新的child",l[0])
            new_node=Node(l[0],num,[],root)
            if l[0] in node_dict:
                node_dict[l[0]].append(new_node)
            else:
                node_dict[l[0]]=[new_node]
            root.child.append(new_node)
            #for i in root.child:
                #print("child name:",i.name,"child parent:",i.parent.name)
            build_tree(new_node,l[1:],num,node_dict)
                #print("近來",node.name)
            
    #if l[0] in root
    #print(root.name,l)


# In[ ]:


f=open("data3.data",'r')
database={}
for line in f.readlines():
    n1,n2,n3=(int(s) for s in line.split())
    #print(n1,n2,n3)
    if n2 in database:
        database[n2].append(n3)
    else:
        database[n2]=[n3]
#print(database)
f.close()


# In[ ]:


#print(len(database))
database_count={}
for i in range(1,len(database)+1):
    database_count[i]=1
#print(database_count)


# In[ ]:


def FP_tree(database,database_count,now_value,min_sup):
    #----------------------------------數個數，低於min_sup砍掉，output：List
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~數個數，低於min_sup砍掉，output：List~~~~~~~~~~~~~~",now_value)
    #print("database：",database)
    #print("database_count：",database_count)
    List={}
    root=Node(-1,0,[])
    for i in range(1,len(database)+1):
        if database[i]==[] and database_count[i]>=min_sup:
            root.value=database_count[i]
            #print("database出現[],value",root.value)
        for item in database[i]:
            if item in List:
                List[item]=List[item]+database_count[i]
            else:
                List[item]=database_count[i]
            #print(item)
    #print(L1)
    remove=[]
    for key in List.keys():
        if List[key]<min_sup:
            remove.append(key)
    for i in remove:
        List.pop(i)
    #print("remove",remove)
    #print("============output:List=",List)

    #----------------------------------數個數，低於min_sup砍掉，output：List
    
    #----------------------------------把database降序排列，output：database
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~把database降序排列，output：database~~~~~~~~~~~~~~")
    import operator
    #x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    #sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    for key in database.keys():
        tmp_dict={}
        tmp_list=[]
        for item in database[key]:
            #print(item,L1[item])
            if item in List:
                tmp_dict[item]=List[item]
        sorted_x = sorted(tmp_dict.items(),reverse=True, key=operator.itemgetter(1))
        for i in range(0,len(sorted_x)):
            #print(i)
            tmp_list.append(sorted_x[i][0])
        database[key]=tmp_list
        #print(tmp_list,sorted_x,sorted_x[0],sorted_x[0][0],len(sorted_x))
    #for key in database.keys():
    #    print(database[key])
    
    #print("============output:database",database)
    #----------------------------------把database降序排列，output：database
    
    
    #----------------------------------建樹，output：node_dict
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~建樹，output：node_dict~~~~~~~~~~~~~~")   
    node_dict={}
    #root=Node(-1,0,[])
    for key in database.keys():
        #if database[key]==[]:
            #print("建樹，加在root",now_value,database_count[key])
            #root.value=database_count[key]
            #continue
        build_tree(root,database[key],database_count[key],node_dict)
        
    #print(len(node_dict[38]))
    #----------------------------------建樹，ourput：node_dict

    
    #----------------------------------從最後一個開始找，ourput：new_database，new_database_count
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~從最後一個開始找，ourput：new_database，new_database_count~~~~~~~~~~~~~~")    
    sorted_L1=sorted(List.items(), key=operator.itemgetter(1))
    #print("從最後一個開始找，根據sorted_L1:",sorted_L1)
    
    if sorted_L1==[]:#全部都低於min_sup
        return [[now_value]],[0]
    
    
    return_item=[]
    return_count=[]
    for item in sorted_L1:
        new_database={}
        new_database_count={}
        new_db_num=1
        for node in node_dict[item[0]]:
            #注意!!!!!!從不同路徑可以得到一樣的組合===>要檢查dic然後加上去
            parent=node.parent
            new_database[new_db_num]=[]
            new_database_count[new_db_num]=node.value
            while parent.name!=-1:
                new_database[new_db_num].append(parent.name)
                parent=parent.parent
            new_db_num+=1
            
        #開始遞迴
        output_item,output_count=FP_tree(new_database,new_database_count,item[0],min_sup)
        #print("從",item[0],"output回來的東西：",output_item,output_count,"now_value:",now_value)
        for i in range(0,len(output_count)):
            if output_count[i]!=0:
                return_item.append(output_item[i])
                return_count.append(output_count[i])
        return_item.append([item[0]])#我發給你，我補上你。不用回傳自己
        return_count.append(item[1])
        
    for i in range(0,len(return_item)):
        #print("output_item[i]=",output_item[i])
        if now_value!=-1:
            return_item[i].append(now_value)
    #if now_value!=-1:
        #return_item.append([now_value])
        #return_count.append(root.value)
    #print("return_item=",return_item,"return_count=",return_count,now_value,root.value)
    return return_item,return_count
        #----------------------------------從最後一個開始找，ourput：new_database，new_database_count
    
    
    #----------------------------------return：output_item，output_count
    if new_database[1]==[]:#回傳自己
        output_item=[]
        output_count=[]
        output_item.append([now_value])
        output_count.append(0)
        return output_item,output_count
    


# In[ ]:


#min_sup=5
import time
for i in range(1,21):
    min_sup=i*5
    print("min_sup",min_sup)
    tStart = time.time()
    item,count=FP_tree(database,database_count,-1,min_sup)
    tEnd = time.time()#計時結束
    print ("花了 %f 秒" % (tEnd - tStart))
    print("有 %d 筆" % len(item))
#for i in range(0,len(item)):
    #print(item[i],":",count[i])
#print(item,count)

