voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
{"county":"Denver", "registered_voters": 463353}, 
{"county":"Jefferson", "registered_voters": 432438}]

for i in voting_data :
    name =i.get("county")
    voters =i.get("registered_voters")
    print(f"{name} county has {voters:,} registered voters")

print("END OF PROGRAM")
