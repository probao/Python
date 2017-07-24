import math
import random

#transform binary to decimal for a number
def b2d(b):		
  t=0
	for j in range(len(b)):
		t += b[j]*(math.pow(2,j))
	t=float(t*10)/1023
	return t


# transform binary to decimal for one population
def decodechrom(pop):
	temp=[]
	for i in range(len(pop)):
		t=0
		for j in range(10):
			t+=pop[i][j]*(math.pow(2,j))
		temp.append(t)
	return temp

# calculate the value according to the equation
def calobjvalue(pop):
	temp1 = []
	objvalue=[]
	temp1=decodechrom(pop)
	for i in range(len(temp1)):
		x=float(temp1[i])*10/1023
#		objvalue.append(10*math.sin(5*x)+7*math.cos(4*x))
		objvalue.append(6*x-x*x-5)
	return objvalue

# calculate the fit value if value equals to 0, then make it zero
def calfitvalue(objvalue):
	fitvalue=[]
	temp=0.0
	Cmin=0
	for i in range(len(objvalue)):
		if (objvalue[i] + Cmin) > 0:
			temp =Cmin + objvalue[i]
		else:
			temp = 0.0
		fitvalue.append(temp)
	return fitvalue

# choose the best results
def best(pop, fitvalue):
	px=len(pop)
	bestindividual=[]
	bestfit=fitvalue[0]
	for i in range(1, px):
		if (fitvalue[i] > bestfit):
			bestfit=fitvalue[i]
			bestindividual=pop[i]
	return [bestindividual, bestfit]

# selection
def sum(fitvalue):
	total=0
	for i in range(len(fitvalue)):
		total += fitvalue[i]
	return total

def cumsum(fitvalue):
	for i in range(len(fitvalue)):
		t=0
		j=0
		while j<=i:
			t += fitvalue[j]
			j += 1
		fitvalue[i] = t

def selection(pop, fitvalue):
	newfitvalue = []
	totalfit = sum(fitvalue)
	for i in range(len(fitvalue)):
		newfitvalue.append(float(fitvalue[i])/totalfit)
	cumsum(newfitvalue)
	ms=[]
	poplen=len(pop)
	for i in range(poplen):
		ms.append(random.random())
	ms.sort()
	fitin = 0
	newin = 0
	newpop = pop
	while newin < poplen:
		if ms[newin] < newfitvalue[fitin]:
			newpop[newin] = pop[fitin]
			newin = newin + 1
		else:
			fitin = fitin + 1
	pop = newpop

# crossover between two chromo	
def crossover(pop, pc):
	poplen = len(pop)
	for i in range(poplen-1):
		if random.random() < pc:
			cpoint = random.randint(0, len(pop[0]))
			temp1 = []
			temp2 = []
			temp1.extend(pop[i][0:cpoint])
			temp1.extend(pop[i+1][cpoint:len(pop[i])])
			temp2.extend(pop[i+1][0:cpoint])
			temp2.extend(pop[i][cpoint:len(pop[i])])
			pop[i] = temp1
			pop[i+1] = temp2


# mutation for some chromo
def mutation(pop, pm):
	px = len(pop)
	py = len(pop[0])
	for i in range(px):
		if random.random() < pm:
			mpoint = random.randint(0, py-1)
			if (pop[i][mpoint] == 1):
				pop[i][mpoint]=0
			else:
				pop[i][mpoint]=1


# generate original population
def pop(n):
	pop=[]
	for i in range(n):
		a=[0  for j in range(n)]
		a[i]=1
		pop.extend([a]*5)
	return pop


#initial defination	
chromlength=10
pc=0.6
pm=0.001
results=[[]]
bestindividual=[]
bestfit=0
fitvalue=[]
tempop=[[]]
pop=pop(10)
#print pop

#main loop
for i in range(100):
	objvalue=calobjvalue(pop)
	fitvalue=calfitvalue(objvalue)
	[bestindividual, bestfit]=best(pop, fitvalue)
	results.append([bestfit,b2d(bestindividual)])
	selection(pop, fitvalue)
	crossover(pop, pc)
	mutation(pop, pc)	

results.sort()
print(results[-1])
