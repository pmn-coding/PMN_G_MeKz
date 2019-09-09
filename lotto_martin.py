from random import randint
#Erstellen der Liste
nums = []

for x in range(49):
    nums.append(x+1)
#Mischen
for i in range(randint(1000,50000)):
    num1 = randint(0,48)
    num2 = randint(0,48)
    nums[num1], nums[num2] = nums[num2], nums[num1]
print(nums,"\n")
#Ziehung
print("Die Gewinnzahlen sind: ",nums[0:6])
