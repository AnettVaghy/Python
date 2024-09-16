
import random
print("Tasteaza numarul de intrebari pentru acest test:")
final = int(input())
sum =0
count =0


t1 = {"A time of 1300 UTC is transmitted as: \n 1.Thirteen hundred UTC \n 2.One three zero zero \n 3.One three hundred UT\n" :"2",
      "Semnalul emis de un NDB este afectat de:\n1.zone de litoral \n2.interferente electronice\n3.semnal GSM" :"1"}
while count <final:
  count+=1
  question = random.choice(list(t1.keys()))
  print(question)
  response = input()
  if response == t1[question]:
    sum+=1

print("Ai răspuns corect la ", sum, "intrebari din ", final)

f = open("rezultate.txt", "x")
f.write("Rezultatul tau este " )
f.write(str(sum))

f.close()
