s1 = {2,3,1}
s2 = {"c","o","v"}
s3 = list(zip(s1,s2))
print(s3)
l1 = ["Rinmolu", "Mathhew", "John"]
l2 = [9,4,2]
l3 = {l1:l2 for l1,l2 in zip(l1,l2)}
print(l3)


