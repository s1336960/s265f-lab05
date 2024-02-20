a = [(1,20), (1,10), (2,10), (2,20)]
print(min(a), max(a))
print(a.index(min(a)), a.index(max(a)) )
del a[a.index(min(a))]
print(a)