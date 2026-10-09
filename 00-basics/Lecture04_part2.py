collection=set()

collection.add(1)
collection.add(2)
collection.add(3)

collection.remove(1)

print(collection)


## union & intersection using set

set1={1,2,3}
set2={2,3,4}

print(set1.union(set2)) # both set value  return unique value
print(set1.intersection(set2))# both set common value return