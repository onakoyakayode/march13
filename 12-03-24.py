import random as rd


# To print a random number between 2 numbers, use the following function:
a = rd.randint(1, 20)

# print(a)

# To print a random number between 2 numbers and also take a step

b = rd.randrange(5, 30)

l = ["Ade", "bayo", "Charles", "Dayo", "Emma"]

d = rd.choice(l)

print("The chosen name is ", d)

fruits = ["Apple", "Banana", "Cherry"]
weights=[90, 76, 56] #sum 90 + 76 +  56
total_weight = sum(weights)

normalized_weight = [weight / total_weight for weight in weights]

e = rd.choices(fruits, weights = normalized_weight, k=5)

print("Print choices for me:", e)


f = rd.seed(1, 30)

print(f)

# print(b)

# print([l for l in b])
# print(d)


# for i in rd.randint(1, 20):
#     po = []

#     if i == 0:
#         print("Oops!")
#     else:
#         po.append(i)
#         print(po)


# for i in range(1, 21):
#     rd.seed(1)
#     print(rd.randint(1, 21))
#     # print(rd.randrange(1, 40, 2))
    

random_num = [] 
    
for ran in range(1, 101):
    num = rd.randint(1, 100)
    random_num.append(num)
    

print(random_num)