from collections import defaultdict
grammar = defaultdict(list)
first_nodes = defaultdict(list)
def follow(n):
	ans=[]
	if n == 'E':ans.append('$')
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
	length = len(grammar[n])
	for j in range(0,length):
		f = grammar[n][j][count]
		if f.islower() or f=='#':
			ans.append(f)
		else :
			if f!=n:
				for k in first(f):
					if k == '#':flag = 1
					if k not in ans and k!='#':ans.append(k)
		if flag == 1: 
			count = count+1
			j = j-1
		else : count = 0
	return ans

file = open('input.txt','r')
for line in file:
	j = line.split()
	node = j[0]
	grammar[node].append(j[1])

print "Grammar"
for k in grammar:
	print k,"->",grammar[k]

print "FIRST OF CFG"
for node in grammar:
	first_nodes[node] = first(node)
	print node,first_nodes[node]

print "Follow of CFG"
for node in grammar:
	print node,follow(node)


