import os
import sys

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





def successors(test):
    max_cost = -1
    inter_teams = []

    #print 'hey', test
    for a in range (len(test)):
        
        grpThree = [test[a]] 
        #print 'hello',grpThree
        cost = total_cost(grpThree)
        #print 'two in grps:', cost,grpThree
    
        if cost >= max_cost: # and grpThree != []:
            max_cost = cost
            new_set = grpThree[:]
            team = Team()
            team.team_members = new_set
            team.cost = max_cost
            inter_teams.append(team) 

            #print 'this is',inter_teams
            for b in  range (len(test)):
                if test[a]!=test[b]:
                    grpThree=  [test[a],test[b]]
                    cost = total_cost(grpThree)
                    #print grpThree,cost
                    if max_cost >= cost :
                        min_cost1 = cost
                        new_set1 = grpThree[:]
                        team = Team()
                        team.team_members = new_set1
                        team.cost = min_cost1
                        inter_teams.append(team)
               
                        #print inter_teams[0]
                        
                        #print min_cost1,new_set1
                        for c  in  range (len(test)):
                            if test[a]!=test[b] and test[b]!=test[c] and test[c]!=test[a] :
                                grpThree=  [test[a],test[b],test[c]]
                                cost = total_cost(grpThree)
                                #print grpThree,cost
                                if min_cost1 >= cost :
                                    mincost2 =cost
                                    newset2 = grpThree[:]
                                    team = Team()
                                    team.team_members = newset2
                                    team.cost = mincost2
                                    inter_teams.append(team) 
       
        #   return inter_teams
        
#
    return inter_teams        
#    return inter_teams
r =[]
final_cost = 0

file = open ( 'ip.txt' , 'r')
l = []
l = [ line.split() for line in file]
#print l

test= []
for i in range(len(l)):
    test.append(l[i][0])
#print test


min_val =0

grpThree = []
intermediate = []
inter_teams = []
inter_teams1 = []
#final_cost =0
final_grp =[]


while test != []:
    a=[]
    minimum =100000
    final_team =[]
#test = ['D']
    a= successors(test)
    for s in a :
        #print s
        if minimum >= s.cost:
            #print s.cost,s.team_members
            minimum = s.cost
            final_team= s.team_members
    r.append(final_team)
    test = list(set(test) - set(final_team))
    final_cost= final_cost + minimum
    #print 'hey',test 
    print(" ".join(str(x) for x in final_team))
    #print 'final teams are :' ,final_team,minimum



#print r
final_cost = final_cost + len(r) * 7
print final_cost




