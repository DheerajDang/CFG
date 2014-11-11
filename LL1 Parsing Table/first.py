from collections import defaultdict
from copy import deepcopy
grammar = defaultdict(list)
first_nodes = defaultdict(list)
pro = defaultdict(list)
production = []
table = {}
terminals = []
newnode = 'P'
def follow(n):
	ans=[]
	if n == 'S':ans.append('$')
	for j in grammar:
		for k in grammar[j]:	
			for l in range(0,len(k)):
				if k[l].isupper() and k[l]==n:
					try:
						if k[l+1].isupper():
							for m in first_nodes[k[l+1]]:
								if m not in ans and m!='#':ans.append(m)
								if m == '#':
									for p in follow(k[l+1]):
										if p not in ans and p!='#':ans.append(p)
						else: 
							if k[l+1] not in ans:ans.append(k[l+1])
					except:
						if j != n:
							for o in follow(j):
								if o not in ans:ans.append(o)
	return ans
def first(n):
	count = 0
	flag = 0
	ans = []
	prod = []
	length = len(grammar[n])
	for j in range(0,length):
		f = grammar[n][j][count]
		if f.islower() or f=='#':
			ans.append(f)
			prod.append(grammar[n][j])
		else :
			for k in first(f):
				if k == '#':flag = 1
				if k not in ans and k!='#':
					ans.append(k)
					prod.append(grammar[n][j])		

		if flag == 1: 
			count = count+1
			j = j-1
		else : count = 0
	return ans,prod

def subsitution(node):
	for j in grammar[node]:
		if len(j)==1 and j.isupper():
			grammar[node].remove(j)
			for l in grammar[j]:
				grammar[node].append(l)


file = open('input.txt','r')
for line in file:
	j = line.split()
	node = j[0]
	grammar[node].append(j[1])

print "Grammar"
for k in grammar:
	print k,"->",grammar[k]

for node in grammar:
	subsitution(node)
	print node,grammar[node]


g = deepcopy(grammar)
for node in g:
	left =[]
	newnode = chr(ord(newnode)+1)
	for j in g[node]:
		if node == j[0]:
			left.append(j)
			grammar[node].remove(j)
			if '#' not in grammar[newnode]:grammar[newnode].append('#')
		if j[0].islower and len(j)==1 and len(left)>0:
			grammar[node].append(j+newnode)
			grammar[node].remove(j)
	for k in left:
		grammar[newnode].append(k[1:]+newnode)

print "New CFG GRAMMAR FOR LL1 GRAMMAR"
for k in grammar:
	for l in grammar[k]:
		print k," -> ",l

print "FIRST OF CFG"
for node in grammar:
	first_nodes[node],pro[node] = first(node)
	# print node,first_nodes[node],pro[node]

print "Follow of CFG"
for node in grammar:
	print node,follow(node)

for node in grammar:
	for j in grammar[node]:
		for k in j:
			if (k.islower() or k=='+' or k=='-' or k=='*' or k=='/' or k=='#') and k not in terminals:terminals.append(k)
print terminals
terminals.append("$")


for node in grammar:
	table[node] = {}
	for i in terminals:
		try:
			if i == '#':
				for j in follow(node):table[node][j] = pro[node][first_nodes[node].index(i)]
			else:table[node][i] = pro[node][first_nodes[node].index(i)]
		except ValueError:
			a = 1

print "\n\n\t\tLL1 Table"
print "\t\t",
for i in terminals:print i,"\t\t",
for node in grammar:
	print
	print node,"\t\t",
	for i in terminals:
		try:
			print table[node][i],"\t\t",
		except:
			print " \t\t",
print 