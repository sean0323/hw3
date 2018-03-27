
# coding: utf-8

# In[34]:


z=dict()
x=input("Please type anything:\n") 
for y in x :
    if y not in z:
        z[y]=1
    else:
        z[y]+=1
for y in z:
    w=z[y]
    print(y,":",w)

