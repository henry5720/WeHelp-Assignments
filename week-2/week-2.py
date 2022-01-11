# 要求一：函式與流程控制
print("要求一：函式與流程控制")
def calculate(min, max):
    sum=0
    for x in range(min, max+1):
        sum=sum+x
    print(sum)        
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

# 要求二：Python 字典與列表、JavaScript 物件與陣列
print("要求二：JavaScript 物件與陣列")
def avg(data):
    total = data["count"]
    ls = []
    step = 0
    dem = data["employees"]
    for i in dem:
        ls.append(dem[step]["salary"])
        step+=1
    print(sum(ls) / total)

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

# 要求三：演算法
print("要求三：演算法")
def maxProduct(nums):
    result = []
    for i in range(0, len(nums)-1):
        for j in range(1+i, len(nums)):
            # print(i, j)
            result.append(nums[i] * nums[j])
    print(max(result))
    
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到2

#要求四 ( 請閱讀英文 )：演算法
print("要求四 ( 請閱讀英文 )：演算法")
def twoSum(nums, target):
    for i in range(0, len(nums)-1):
        for j in range(1+i, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# 要求五 ( Optional )：演算法
print("要求五 ( Optional )：演算法")
def maxZeros(nums):
    mz = 0 # 存最大0出現的次數
    zero = 0 # 存當前0是第幾次出現
    last = 0 # 存上一個出現的元素
    for i in nums:
        if i == last & i == 0: 
            zero += 1
            mz = max((mz, zero))
            # print(max(mz, zero))
        else:
            last = i
            zero = 0
    print(mz)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
print()