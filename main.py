import time
name = input("Enter your name :-")
def helloBuddy(name):
  y = int(time.strftime('%H'))
  if(y<12):
    print("Good Morning",name)
  elif(y==12):
    print("Good noon",name)
  elif(y<=18):
    print("Good Afternoon",name)
  elif(y<=20):
    print("Good evening",name)  
  else:
    print("Good night",name)

helloBuddy(name)
questions = [
  ["Panna National Park is in which state?","Rajasthan","Maharashtra","Gujarat"," Madhya Pradesh",4],
  ["What is the capital of Turkey?","Jerusalem","Canberra","Ankara","Wellington",3], 
  ["Humayun was born in the year _____","1508","1608","1708","1808",1],
  ["Who Invented the 3-D printer?","Nick Holonyak","Elias Howe","Chuck Hull","Christiaan Huygens",3],
  ["What is the maximum number of Members in Lok Sabha?","512","552","542","532",2],
  ["Before its Independence, Bangladesh was part of______","India","China","Pakistan","United Kingdom",3],
  ["Who discovered India?","Vasco da Gama","Christopher Columbus","James Cook","Willem Janszoon",1],
  ["Who is Sachin Tendulkar?","Indian Hockey player","Indian Cricketer","Indian Kabaddi player","Indian Marathon Runner",2],
  ["What is the capital city of India?","New Delhi","Mumbai","Kolkata","Bhubaneswar",1],
  ["Who was the first Prime Minister of India?","Indira Gandhi","Narendra Modi","Jawaharlal Nehru","Rajiv Gandhi",3],
  ["Who is popularly known as the \"Iron Man\" of India?","Lal Bahadur Shastri","Sardar Vallabh Bhai Patel","Mahatma Gandhi","Dr. B.R Ambedkar",2],
  ["Which is the national sport of India?","Basket Ball","Cricket","Football","Hockey",4],
  ["Who is the current President of India?","Ram Nath Kovind","Pranab Mukherjee","Draupadi Murmu","A. P. J. Abdul Kalam",3],
  ["Which place in India is also known as the \“Land of Rising Sun\”?","Sikkim","Arunachal Pradesh","Karnataka","Gujarat",2],
  ["Where is Taj Mahal located in India?","New Delhi","Kolkata","Agra","Punjab",3],
]


levels = [1000,2000,3000,5000,10000,20000,30000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

money = 0 
for i in range(0,len(questions)):
  q = questions[i]
  print(f"\n\nQuestion for ₹ {levels[i]}/-")
  print(f"\n\n{q[0]}")
  print(f"1) {q[1]}           2) {q[2]}")
  print(f"3) {q[3]}           4) {q[4]}")
  reply = int(input("Ans:- "))
  if reply == q[-1]:
    print(f"Correct you win ₹ {levels[i]}/-")
    money = money + levels[i]
  else:
    print(f"Wrong Answer Thank you {name} for joining")
    break
print(f"Congratulations You are taking ₹ {money}/-")
