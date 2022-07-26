#a)
cap_list = ["Kohli","Dhoni","Rohit"]
team_list = ["RCB","CSK","MI"]
result = zip(cap_list, team_list)
print(result) #diplays zip object as a wrapper
#hence Converting to list
result_list = list(result)
print(result_list)
print("")
#b)
score=[("Akash",85),("Arvind",80),("Ashu",95),("Bhavana",90),("Bhavik",87)]
names_marks = list(zip(*score))
print(names_marks[0])
