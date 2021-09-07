import random

#These were some candidates in Mexico
candidates = ["AMLO", "Peña","Bronco","Calderon","Fox"]
school_1 = []
school_2 = []
school_3 = []
school_4 = []
school_5 = []
votes = []


#Inserting the votes in the lists of the schools
for vote in range(5):
  num = random.randint(20, 100)
  school_1.append(num)

for vote in range(5):
  num = random.randint(20, 100)
  school_2.append(num)

for vote in range(5):
  num = random.randint(20, 100)
  school_3.append(num)

for vote in range(5):
  num = random.randint(20, 100)
  school_4.append(num)

for vote in range(5):
  num = random.randint(20, 100)
  school_5.append(num)

#Summing the votes for every candidate
for vote in range(5):
    if vote == 0:
      vote1 = school_1[vote] + school_2[vote] + school_3[vote] + school_4[vote] + school_5[vote]
    elif vote == 1:
      vote2 = school_1[vote] + school_2[vote] + school_3[vote] + school_4[vote] + school_5[vote]
    elif vote == 2:
      vote3 = school_1[vote] + school_2[vote] + school_3[vote] + school_4[vote] + school_5[vote]
    elif vote == 3:
      vote4 = school_1[vote] + school_2[vote] + school_3[vote] + school_4[vote] + school_5[vote]
    elif vote == 4:
      vote5 = school_1[vote] + school_2[vote] + school_3[vote] + school_4[vote] + school_5[vote]


#Inserting the sum of votes per candidate en the list of votes
votes.append(vote1)
votes.append(vote2)
votes.append(vote3)
votes.append(vote4)
votes.append(vote5)

# Adding all the votes to the variable total
total = 0
for voto in votes:
  total += voto


for vote in range(5):
  print(candidates[vote] + " Number of votes:", end="")
  print(votes[vote])
  print(f"Respective porcentage: {round((votes[vote] / total)*100, 2)}%")
  print()
