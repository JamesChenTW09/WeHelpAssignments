# # 要求一：函式與流程控制
def calculate(min, max):
    print(((min + max) * (max - min + 1)) / 2)

    # sum = 0
    # for i in range(min, max+1):
    #     sum+=i
    # print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30
print("--------------------------------------")

# 要求二：Python 字典與列表、JavaScript 物件與陣列
def avg(data):
    avg = 0
    for x in range(data["count"]):
        avg+=data["employees"][x]["salary"]
    print(avg / data["count"])
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

print("--------------------------------------")

# 要求三：演算法

def maxProduct(nums):
    max = nums[0]*nums[1]
    for x in nums:
        for y in nums:
            if x!=y and x*y>max:
                max = x*y
    print(max)
                

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

print("--------------------------------------")
# 要求四 ( 請閱讀英文 )：演算法
def twoSum(nums, target):
    answer = []
    for x in range(len(nums)):
        for y in range(x+1,len(nums)): 
            if  nums[x] != nums[y] and nums[x] + nums[y] == target:
                answer.append(x)
                answer.append(y)
                break

    return answer
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
print("--------------------------------------")

# 要求五 ( Optional )：演算法
def maxZeros(nums):
    count = 0
    longestLength = 0
    for x in nums:
        if x == 0:
            count+=1
        elif count > longestLength:
            longestLength = count
            count = 0
    if count > longestLength:
        longestLength = count
    print(longestLength)


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
