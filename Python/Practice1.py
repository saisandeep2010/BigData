#very important:

# l = [1,2,3]

# l.append(4)

# print(l)

# print(dir(l))
# l.insert(0,0)
# print(l)

# .append - O(1)
# .insert - O(n*n) -> O(n)

# hashtable is faster than list
# print(hash('hello'))
# print(hash('hello2'))


a = [123]
b = [456, a]
a.append(b)
# print(b)

# print('----')
# for i in b:
#     print(i)


# a = 1
# b = 1

r = range(1000000)
print(r)

a = [i for i in range(10)]
b = (i for i in range(10))

print('A:', a[5])
#print(b[5])
print('R:', r[5])

