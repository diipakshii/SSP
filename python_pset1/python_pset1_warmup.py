# produce code that is able to sum the list of values
# warm-up
# 06/15/22
# Dipakshi Pal

# PART 1

def sumList(nums):
    total = 0
    n = len(nums)
    for i in range(n):
        total = total + nums[i]
    return total 

print("testing sumList")
print(sumList([]))              # expected output: 0
print(sumList([3]))             # expected output: 3
print(sumList([1., 4.5, -3.2])) # expected output: 2.3

# PART 2

def estimatePi(n):
    total = 0
    for i in range(1,n+1):
        total += (4 * (-1)**(i+1) / (2*i - 1))
    return total

print("testing estimatePi")
print(estimatePi(1))     # expected (approximate) output: 4.0
print(estimatePi(10))    # expected (approximate) output: 3.0418396189294032
print(estimatePi(100))   # expected (approximate) output: 3.1315929035585537
print(estimatePi(1000))  # expected (approximate) output: 3.140592653839794
print(estimatePi(10000)) # expected (approximate) output: 3.1414926535900345

def scaleVec(vec, scalar):
    new_vec = []
    for i in range(len(vec)):
        new_vec.append(vec[i] * scalar)
    return new_vec

print("testing scaleVec")
vec = []
print(scaleVec(vec, 5)) # expected output: []
print(vec) # expected output: []
vec = [1]
print(scaleVec(vec, 5)) # expected output: [5]
print(vec) # expected output: [1]
vec = [-2, 1.5, 0.]
print(scaleVec(vec, 6)) # expected output: [-12., 9., 0.]
print(vec) # expected output: [-2, 1.5, 0.]
