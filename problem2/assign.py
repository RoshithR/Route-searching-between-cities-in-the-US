
#import numpy as np
import os

class Team:
    team_members = []
    cost = -1

    def __repr__(self):
        return str("{Team Members : " + str(self.team_members) + ", Cost : " + str(self.cost) + "}")

def preffered_partner_cost (result) :
    cost_n = 0 
    for i in range (len(l)) :
        
        sentence = l[i][2]
        #print 'sent',sentence
        for j in range (len(result)) :
            if  result[j]== l[i][0] :
    
                if (sentence != '_') :
                    sentence = sentence.split (',')
                    #print 'hey', sentence
                    s1 = set(sentence)
                    s2 = set(result)
                    if len(s1.intersection(s2)) != len(sentence) :

                        cost_n = cost_n + (len(sentence) - len(s1.intersection(s2)))
                    
                    else :
                    
                        cost_n = cost_n + 0

    return cost_n

def team_cost (result) :
    cost_i = 0
    for i in range (len(l)) :
        for j in range (len(result)) :
            if(result[j] == l[i][0] ) :
                
                if ((len(result) != int(l[i][1])) and int(l[i][1]) != 0):
                    cost_i = cost_i + 1
                else:
                    cost_i = cost_i + 0
    return cost_i

def Nonpreffred_cost (result) :
    cost_m = 0
    for i in range (len(l)) :
        sentence = l[i][3]
        for j in range (len(result)) :

            if  result[j]== l[i][0] :
            
                if (sentence != '_') :
                    sentence = sentence.split (',')
                    s1 = set(sentence)
                    s2 = set(result)
                    #print len(s1.intersection(s2))
                    if len(s1.intersection(s2))!= 0 :
                        cost_m = cost_m +  len(s1.intersection(s2))
                    else :
                        cost_m = cost_m + 0
    return  cost_m

def total_cost(result):   
    p = team_cost(result)

    n = preffered_partner_cost (result)
    m = Nonpreffred_cost(result)
    
    plus = p * 1 + n * 3 + m * 5
    #print plus
    return plus



file = open ( 'Input_file.txt' , 'r')
l = []
l = [ line.split() for line in file]
##print l

test= []
for i in range(len(l)):
    test.append(l[i][0])
#print test

min_val =0
max_cost = 0
grpThree = []
intermediate = []
inter_teams = []
#min_cost1=0
#min_cost2 =0
min =100000
for a in range (len(test)):
    grpThree = [test[a]]
    cost = total_cost(grpThree)
    #print cost,grpThree
    if cost >= max_cost:
         max_cost = cost
         new_set = grpThree[:]
         team = Team()
         team.team_members = new_set
         team.cost = max_cost
         inter_teams.append(team)
         #for i in range (len(inter_teams)) :
         print inter_teams[0]
         
         for b in  range (len(test)):
            if test[a]!=test[b]:
                grpThree=  [test[a],test[b]]
                
                cost = total_cost(grpThree)
                #print grpThree,cost
                if max_cost > cost :
                    min_cost1 = cost
                    new_set1 = grpThree[:]
                    #print min_cost1,new_set1
                    for c  in  range (len(test)):
                        if test[a]!=test[b] and test[b]!=test[c] and test[c]!=test[a] :
                            grpThree=  [test[a],test[b],test[c]]
                            cost = total_cost(grpThree)
                            
                            #print cost,grpThree
                            if min_cost1 > cost and min_val < cost:
                                mincost2 =cost
                                #min_val = cost
                                newset2 = grpThree[:]

                                #print mincost2,newset2
#test.remove(newset2)



import os

class Team:
    team_members = []
    cost = -1

    def __repr__(self):
        return str("{Team Members : " + str(self.team_members) + ", Cost : " + str(self.cost) + "}")

def preffered_partner_cost (result) :
    cost_n = 0 
    for i in range (len(l)) :
        
        sentence = l[i][2]
        #print 'sent',sentence
        for j in range (len(result)) :
            if  result[j]== l[i][0] :
    
                if (sentence != '_') :
                    sentence = sentence.split (',')
                    #print 'hey', sentence
                    s1 = set(sentence)
                    s2 = set(result)
                    if len(s1.intersection(s2)) != len(sentence) :

                        cost_n = cost_n + (len(sentence) - len(s1.intersection(s2)))
                    
                    else :
                    
                        cost_n = cost_n + 0

    return cost_n

def team_cost (result) :
    cost_i = 0
    for i in range (len(l)) :
        for j in range (len(result)) :
            if(result[j] == l[i][0] ) :
                
                if ((len(result) != int(l[i][1])) and int(l[i][1]) != 0):
                    cost_i = cost_i + 1
                else:
                    cost_i = cost_i + 0
    return cost_i

def Nonpreffred_cost (result) :
    cost_m = 0
    for i in range (len(l)) :
        sentence = l[i][3]
        for j in range (len(result)) :

            if  result[j]== l[i][0] :
            
                if (sentence != '_') :
                    sentence = sentence.split (',')
                    s1 = set(sentence)
                    s2 = set(result)
                    #print len(s1.intersection(s2))
                    if len(s1.intersection(s2))!= 0 :
                        cost_m = cost_m +  len(s1.intersection(s2))
                    else :
                        cost_m = cost_m + 0
    return  cost_m

def total_cost(result):   
    p = team_cost(result)

    n = preffered_partner_cost (result)
    m = Nonpreffred_cost(result)
    
    plus = p * 1 + n * 3 + m * 5
    #print plus
    return plus



file = open ( 'Input_file.txt' , 'r')
l = []
l = [ line.split() for line in file]
##print l

test= []
for i in range(len(l)):
    test.append(l[i][0])
#print test

min_val =0
max_cost = 0
grpThree = []
intermediate = []
inter_teams = []
#min_cost1=0
#min_cost2 =0
min =100000
for a in range (len(test)):
    grpThree = [test[a]]
    cost = total_cost(grpThree)
    #print cost,grpThree
    if cost >= max_cost:
         max_cost = cost
         new_set = grpThree[:]
         team = Team()
         team.team_members = new_set
         team.cost = max_cost
         inter_teams.append(team)
         #for i in range (len(inter_teams)) :
       	 #print inter_teams[0].cost
         
         for b in  range (len(test)):
            if test[a]!=test[b]:
                grpThree=  [test[a],test[b]]
                
                cost = total_cost(grpThree)
                #print grpThree,cost
                if inter_teams[0].cost > cost :
                    min_cost1 = cost
                    new_set1 = grpThree[:]
                    print min_cost1,new_set1
                    for c  in  range (len(test)):
                        if test[a]!=test[b] and test[b]!=test[c] and test[c]!=test[a] :
                            grpThree=  [test[a],test[b],test[c]]
                            cost = total_cost(grpThree)
                            
                            #print cost,grpThree
                            if min_cost1 > cost and min_val < cost:
                                mincost2 =cost
                                #min_val = cost
                                newset2 = grpThree[:]

         