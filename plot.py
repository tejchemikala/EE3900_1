#%%
import numpy as np
import matplotlib.pyplot as plt 


f= open("Ydata.txt","r")
x = []
y = []
#print(f.readlines())
#%%
l=f.readline()
for xv in l.split(" "):
    if(xv!= '\n'):
       x.append(float(xv))
l =f.readline()
for xv in l.split(" "):
    if(xv!= '\n'):
       y.append(float(xv))
print(x)
print(y)
        
    

#%%
xn = np.array(x)
yn = np.array(y)


print(xn)
print(yn)

#%%

plt.subplot(1,2,1)
plt.stem(range(0,6),xn)
plt.title('Digital Filter Input-Output')
plt.ylabel('x(n)')
plt.grid()

plt.subplot(1,2,2)
plt.stem(range(0,20),yn,)
#plt.title('Digital Filter Input-Output')
plt.ylabel('y(n)')
plt.grid()



# %%
