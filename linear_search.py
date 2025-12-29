s=[3,5,6,1,10,7]
target=10
def linear_search(s,target):
    for num in s:
        if num==target:
            return "found"
    return "not found"
print(linear_search(s,target))