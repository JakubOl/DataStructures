# myList = [i for i in range(1, 101)]

# myList.remove(30)

# print(myList)


# def findMissing(list, n):
#     sum1 = n*(n+1)/2
#     sum2 = sum(list)
#     print(sum1-sum2)


# findMissing(myList, 100)

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            if nums[i] + nums[j] == target:
                print(i, j)


myList = [0, 1, 2, 3, 3, 4, 5, 6]
findPairs(myList, 6)
