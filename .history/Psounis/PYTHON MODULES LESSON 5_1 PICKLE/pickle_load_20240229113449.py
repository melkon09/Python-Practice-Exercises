from pickle import dumps, load

d=[(1,3),{1,2}, dumps]

serialized=dumps(d)
print(serialized)

deserialized = load(serialized)