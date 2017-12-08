def permutations(head, tail, perms, limit):
	if len(perms) == limit:
		return
	elif len(head) == 0:
		perms.append(tail)
	else:
		for i in range(len(head)):
			permutations(head[0:i] + head[i+1:], tail + [head[i]], perms, limit)

def getPerms(digits, limit):
	perms = []
	permutations(digits, [], perms, limit)
	return perms

perms = getPerms([0,1,2,3,4,5,6,7,8,9], 1000000)
print ''.join(str(i) for i in perms[-1])
