import matplotlib.pyplot as plt
import math
import numpy as np
from operator import itemgetter, attrgetter
def World_Population(pop,countries):
	tlist = []
	for i in range(43,len(pop)):
		for j in range(0,len(countries)):
			if (pop[i,2]==countries[j]):
				mlk =[pop[i,2],pop[i,-1]*1000]
				tlist.append(mlk)
	return (tlist)


def padding_function(countries,cases,deaths,cum_cases,cum_deaths,L):
	for i,c in enumerate(countries):
		P=L-len(cases[i])
		for k in range(P):
			cases.insert(0,0)
			deaths.insert(0,0)
			cum_cases.insert(0,0)
			cum_deaths.insert(0,0)
	return cases,deaths,cum_cases,cum_deaths


def moving_av(series,w):
	step=w//2
	s=[]
	for i in range(step):
		s.append(0)
	for c in range(step,len(series)-step):
		sum=0
		for i in range(c-step,c+step+1):
			sum=sum+series[i]
		s.append(sum/w)
	for i in range(step):
		s.append(0)
	return s


def plot_top10(tlist,string1,string2,f):
	sorted_list = sorted_list = sorted(tlist, key=attrgetter(string2),reverse=True)
	fig = plt.figure(figsize=(16,6))
	ax = fig.add_axes([0,0,1,1])
	plt.title("Top ten countries " +  string1,fontsize=20)
	plt.xlabel('Country', fontsize=20)
	plt.ylabel(string2,fontsize=20)
	colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan', 'yellow', 'magenta', 'green', 'orange', 'pink')
	for i in range(0,10):
		ax.bar(sorted_list[i].country_name,getattr(sorted_list[i],string2),color=colors[i], width=0.9, label=sorted_list[i].country_name)
	plt.legend(fontsize=f)
	plt.show()

def plot_WorldMR(tlist,Dates_reported,string):
	plt.figure(figsize=(50,20))
	plt.title("Worldwide {} Mortality rate of Covid-19".format(string),fontsize=50)
	plt.xlabel('Days passed since the begining', fontsize=40)
	plt.ylabel('{} mortality rate'.format(string),fontsize=30)
	plt.plot(Dates_reported, tlist, 'r', marker='o', linewidth=1.9, label='Mortaity Rate')
	plt.xticks(rotation=90)
	plt.yticks(size=20)
	plt.legend(loc='best',fontsize=40)
	plt.grid(True, linewidth=2.0)
	plt.show()

def plot_daily(cases,deaths,weekly_cases,weekly_deaths,Dates_reported,country):
	fig = plt.figure(figsize=(50,20))
	ax = fig.add_axes([0,0,1,1])
	plt.title("Daily cases and deaths {}".format(country),fontsize=50)
	plt.xlabel('Day', fontsize=40)
	plt.ylabel('New Cases/New Deaths',fontsize=40)
	ax.bar(Dates_reported,cases,color='r',width=0.9, label='New Cases')
	ax.bar(Dates_reported,deaths, color= 'm',width=0.9, label='New Deaths')
	plt.plot(Dates_reported,weekly_cases,color='b',linewidth=6,label='weekly average cases')
	plt.plot(Dates_reported,weekly_deaths,color='g',linewidth=6,label='weekly average deaths')
	plt.yticks(size=20)
	plt.xticks(rotation=90)
	plt.legend(fontsize=40)
	plt.grid(True)
	plt.show()


def plot_cumulative(cases,deaths,country,Dates_reported,scale):
	plt.figure(figsize=(50,20))
	plt.title("Cumulative cases and deaths {} ({} scale)".format(country,scale),fontsize=50)
	plt.xlabel('Days passed since the begining', fontsize=40)
	plt.ylabel('Cumulative Cases/Deaths ('+ scale + ' scale)',fontsize=30)
	plt.plot(Dates_reported, cases, 'r', marker='o', linewidth=1.9, label='Cases')
	plt.plot(Dates_reported, deaths, 'm', marker='*', linewidth=1.9, label='Deaths')
	plt.yscale(scale)
	plt.xticks(rotation=90)
	if (scale=="linear"):
		d = (cases[-1]-cases[0])/10
		plt.yticks(np.arange(cases[0], cases[-1], d))
	plt.legend(loc='best',fontsize=40)
	plt.grid(True, linewidth=2.0)
	plt.show()

def plot_pie_charts(tlist, sortby, title):
    S=0
    xlist = []
    ylist = []
    sorted_list = sorted(tlist, key=attrgetter(sortby),reverse=True)
    for i in range(0,10):
        xlist.append(getattr(sorted_list[i],sortby))
        ylist.append(sorted_list[i].country_name)
    for j in range(10,len(sorted_list)):
        S = S + getattr(sorted_list[j],sortby)
    xlist.append(S)
    ylist.append('Others')

    c = ['lightcoral', 'rosybrown', 'sandybrown', 'navajowhite', 'gold', 'khaki', 'lightskyblue', 'turquoise', 'lightslategrey', 'thistle', 'pink']
    plt.figure(figsize=(16,14))
    plt.title(title, size=16)
    plt.pie(xlist, colors=c,shadow=True, labels=xlist)
    plt.legend(ylist, loc='upper left', fontsize=11)
    plt.show()


def plot_top5(tlist,Dates_reported,string1,sortstring,string2):
    sorted_list = sorted(tlist,key=attrgetter(sortstring),reverse=True)
    plt.figure(figsize=(50,20))
    plt.title("Cumulative {} in the top 5 countries".format(string2),fontsize=45)
    plt.xlabel('Days passed since the begining', fontsize=40)
    plt.ylabel("Cumulative {}".format(string2),fontsize=30)
    for i in range(0,5):
      plt.plot(Dates_reported,getattr(sorted_list[i],string1), linewidth=3.9, label=sorted_list[i].country_name)
    plt.xticks(rotation=90)
    plt.yticks(size=20)
    plt.legend(loc='best',fontsize=30)
    plt.grid(True, linewidth=2.0)
    plt.show()


def Make_Overall(alist):
	for i in range(0,len(countries)):
		My_array = ["empty",0,0,0,0,0]
		My_array[0] = countries[i]
		My_array[1] = Cumulative_cases[i][-1]
		My_array[2] = Cumulative_deaths[i][-1]
		if (Cumulative_cases[i][-1]!=0):
			My_array[3] = (Cumulative_deaths[i][-1]/Cumulative_cases[i][-1])*100
		else:
			My_array[3] = 0.0
		for j in Population:
			if (j[0]==countries[i]):
				My_array[4] = ((Cumulative_cases[i][-1])/j[1])*1000000
				My_array[5] = ((Cumulative_deaths[i][-1])/j[1])*1000000
				break
			else:
				My_array[4] = 0.0
				My_array[5] = 0.0
		alist.append(My_array)
	return alist


class country2():
    def __init__(self,c):
        self.country_name=c
        self.population=0
        self.new_cases=None
        self.new_deaths=None
        self.cumulative_cases=None
        self.cumulative_deaths=None
        self.total_cases=None
        self.total_deaths=None
        self.cases_per_million=None
        self.deaths_per_million=None
        self.total_mr=None
        self.daily_mr=[]
        self.cumulative_mr=[]
  
    def set_new_cases(self,data):
        self.new_cases=list(data[' New_cases'].where(data[' Country']==self.country_name).dropna())
  
    def set_new_deaths(self,data):
        self.new_deaths=list(data[' New_deaths'].where(data[' Country']==self.country_name).dropna())
  
    def set_cumulative_cases(self,data):
        self.cumulative_cases=list(data[' Cumulative_cases'].where(data[' Country']==self.country_name).dropna())
  
    def set_cumulative_deaths(self,data):
        self.cumulative_deaths=list(data[' Cumulative_deaths'].where(data[' Country']==self.country_name).dropna())
  
    def set_total_cases(self):
        self.total_cases=self.cumulative_cases[-1]
  
    def set_total_deaths(self):
        self.total_deaths=self.cumulative_deaths[-1]
  
    def set_total_mr(self):
        if (self.total_cases!=0):
            self.total_mr=self.total_deaths/self.total_cases
        else:
            self.total_mr=0

    def set_daily_mr(self):
        for i,j in zip(self.new_cases,self.new_deaths):
            if (i!=0): self.daily_mr.append(j/i)
            else: self.daily_mr.append(0)

    def set_cumulative_mr(self):
        for i,j in zip(self.cumulative_cases,self.cumulative_deaths):
            if (i!=0): self.cumulative_mr.append(j/i)
            else: self.cumulative_mr.append(0)
    

    def padding(self,L):
        P=L-len(self.new_cases)
        for k in range(P):
            self.new_cases.insert(0,0)
            self.new_deaths.insert(0,0)
            self.cumulative_cases.insert(0,0)
            self.cumulative_deaths.insert(0,0)

    def set_population(self,Population):
        for p in Population:
            if (self.country_name==p[0]):
                self.population=math.floor(p[1])
                break

    def set_cases_per_million(self):
        if (self.population!=0):
            self.cases_per_million=(self.total_cases/self.population)*1000000
        else: self.cases_per_million=0
  
    def set_deaths_per_million(self):
        if (self.population!=0):
            self.deaths_per_million=(self.total_deaths/self.population)*1000000
        else: self.deaths_per_million=0

class country():
    def __init__(self,c):
        self.country_name=c
        self.population=0
        self.new_cases=None
        self.new_deaths=None
        self.cumulative_cases=None
        self.cumulative_deaths=None
        self.total_cases=None
        self.total_deaths=None
        self.cases_per_million=None
        self.deaths_per_million=None
        self.total_mr=None
        self.daily_mr=[]
        self.cumulative_mr=[]
  
    def set_new_cases(self,data):
        self.new_cases=list(data['New_cases'].where(data['Country']==self.country_name).dropna())
  
    def set_new_deaths(self,data):
        self.new_deaths=list(data['New_deaths'].where(data['Country']==self.country_name).dropna())
  
    def set_cumulative_cases(self,data):
        self.cumulative_cases=list(data['Cumulative_cases'].where(data['Country']==self.country_name).dropna())
  
    def set_cumulative_deaths(self,data):
        self.cumulative_deaths=list(data['Cumulative_deaths'].where(data['Country']==self.country_name).dropna())
  
    def set_total_cases(self):
        self.total_cases=self.cumulative_cases[-1]
  
    def set_total_deaths(self):
        self.total_deaths=self.cumulative_deaths[-1]
  
    def set_total_mr(self):
        if (self.total_cases!=0):
            self.total_mr=self.total_deaths/self.total_cases
        else:
            self.total_mr=0

    def set_daily_mr(self):
        for i,j in zip(self.new_cases,self.new_deaths):
            if (i!=0): self.daily_mr.append(j/i)
            else: self.daily_mr.append(0)

    def set_cumulative_mr(self):
        for i,j in zip(self.cumulative_cases,self.cumulative_deaths):
            if (i!=0): self.cumulative_mr.append(j/i)
            else: self.cumulative_mr.append(0)
    

    def padding(self,L):
        P=L-len(self.new_cases)
        for k in range(P):
            self.new_cases.insert(0,0)
            self.new_deaths.insert(0,0)
            self.cumulative_cases.insert(0,0)
            self.cumulative_deaths.insert(0,0)

    def set_population(self,Population):
        for p in Population:
            if (self.country_name==p[0]):
                self.population=math.floor(p[1])
                break

    def set_cases_per_million(self):
        if (self.population!=0):
            self.cases_per_million=(self.total_cases/self.population)*1000000
        else: self.cases_per_million=0
  
    def set_deaths_per_million(self):
        if (self.population!=0):
            self.deaths_per_million=(self.total_deaths/self.population)*1000000
        else: self.deaths_per_million=0

def world_data(countries):
    total_cases=0
    total_deaths=0
    daily_mr=[]
    cumulative_mr=[]
    new_cases=[sum(x) for x in zip(*[i.new_cases for i in countries])]
    new_deaths=[sum(x) for x in zip(*[i.new_deaths for i in countries])]
    cumulative_cases=[int(sum(x)) for x in zip(*[i.cumulative_cases for i in countries])]
    cumulative_deaths=[int(sum(x)) for x in zip(*[i.cumulative_deaths for i in countries])]
    cases_per_million=0
    deaths_per_million=0
    for c in countries:
        total_cases+=c.total_cases
        total_deaths+=c.total_deaths
        cases_per_million+=c.cases_per_million
        deaths_per_million+=c.deaths_per_million
    cases_per_million/=1000000
    deaths_per_million/=1000000
    mr=total_deaths/total_cases
    for i,j in zip(new_cases,new_deaths):
        if (i!=0): daily_mr.append(j/i)
        else: daily_mr.append(0)
  
    for i,j in zip(cumulative_cases,cumulative_deaths):
        if (i!=0): cumulative_mr.append(j/i)
        else: cumulative_mr.append(0)
    return new_cases,new_deaths,cumulative_cases,cumulative_deaths,total_cases,total_deaths,cases_per_million,deaths_per_million,mr,daily_mr,cumulative_mr