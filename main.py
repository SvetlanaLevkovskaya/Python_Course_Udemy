for i, j in enumerate(['foo', 'bar', 'baz']):
    if j == 'bar':
        print(i)

mylist = ["foo", "bar", "baz", "bar"]
newlist = enumerate(mylist)
for index, item in newlist:
    if item == "bar":
        print(index, item)
