# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Level 1
len(it_companies)
it_companies.add('Twitter')
it_companies.update({'Youtube','Twitch','Tiktok'})
it_companies.discard('Y')

#Level2
C=A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.symmetric_difference(B))
print(A.isdisjoint(B))


#Level3
len(A)
len(it_companies)

D='I am a teacher and I love to inspire and teach people'
E = D.split()
F = set(E)
print(F)
del C
#it_companies.remove('Y')


