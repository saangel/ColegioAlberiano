import numpy as np
from numpy import random as rand
from matplotlib import pyplot as plt

lanzamientos = int(input("Ingrese número de lanzamientos del dado para sumar: "))
trials = int(input("Ingrese número de experimentos: "))
caras = int(input("Ingrese número de caras del dado: "))
norm = input("Graficar distribución normal? [Y/N]: ")
result = []

for t in range(trials):
    sum = 0
    for l in range(lanzamientos):
        sum+=1+rand.randint(caras)
    result.append(sum)

bins=np.arange(lanzamientos-0.5,caras*lanzamientos+1.5,1)
n,bins,blocks=plt.hist(result,histtype="step",bins=bins,alpha=0.7,linewidth=2)
#plt.hist(result,bins=caras*lanzamientos-(lanzamientos-1),zorder=1)
plt.title("Suma de lanzamientos de "+str(lanzamientos)+" dado(s) de "+str(caras)+" caras, "+str(trials)+" intentos")

if norm == "Y":
    sigma=np.std(result)
    mu=np.mean(result)
    x_plot=np.linspace(min(bins),max(bins),1000)
    normal =trials*(1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-(np.power(x_plot-mu,2)/(2*np.power(sigma,2)))))
    plt.plot(x_plot,normal,label=r"$\mu=$ "+str(mu)[:5]+r", $\sigma=$ "+str(sigma)[:5],linewidth=3,alpha=0.7)
    plt.legend(loc="best")

plt.xlabel("Suma")
plt.ylabel("Frecuencia")
plt.show()
