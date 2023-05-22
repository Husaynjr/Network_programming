l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,443,20,53]
d={l1[i]:l2[i] for i in range(len(l1))}
print(d)