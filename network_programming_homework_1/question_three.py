import json
grade = 0
with open("Questions.json","r") as file:
    d = json.load(file)
    
user_name = input("please enter your name first : ")
for i in range(1,21):
    answer = input(f"{i} : {d[str(i)][0]} : ")
    if answer == d[str(i)][1]:
        grade += 1
print(f"the deserved grade is {grade}")
try :
    with open(r"grades.txt",'a') as file:
        file.write(user_name+" : "+str(grade)+"\n")
except:
    with open(r"grades.txt","w") as file:
        file.write(user_name+" : "+str(grade)+"\n")
