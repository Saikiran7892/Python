


#set operations
#1.union
#2.intersection
#3.difference
#4.sysmetric_difference



s1={10,20,'vcube',True}
 
s2={20,'python',1}
 
'''print(id(s1))
print(id(s2))'''
#output=s1.union(s2)
output=s1 | s2
print(output)
#output=s1.intersection(s2)
output=s1 & s2
print(output)
#output=s1.difference(s2)
output=s1-s2
print(output)
#output=s1.symmetric_difference(s2)
output=s1^s2
print(output)
