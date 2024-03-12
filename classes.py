scores = []

for i in range(10):
    scores.append(input("Enter a number! "))
    print(i)
    
# print(scores)

sum = 0
length = 0

for score in scores:
    if score.isnumeric():
        score = int(score)
        sum += score
        length += 1
    else:
        print("Please input a number!! ")
        
cgpa = sum / length * 0.05

# print(round(cgpa, 2))

if cgpa <= 5 and cgpa >= 4.5:
    print(f"This {round(cgpa, 2)} is a distinction")
elif cgpa <= 4.5 and cgpa >=3.5:
    print(f"This {round(cgpa, 2)} is Upper credit")
elif cgpa < 3.5 and cgpa >= 2.5:
    print(f"This {round(cgpa, 2)} is a Lower credit")
elif cgpa < 2.5 and cgpa >= 2.0:
    print(f"This {round(cgpa, 2)} is a pass")
else:
    print(f"This {round(cgpa, 2)} is a failed") 