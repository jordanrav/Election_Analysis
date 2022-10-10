#get total # of candidates
#seperate votes by county
#seperate votes by candidate
#add votes for each candidate
#determine who won by highest vote count
# Import the datetime class from the datetime module.
# Import the datetime class from the datetime module.
#______________________________________________________________________________________________________________________________
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

candidate_options = []
candidate_votes = {}
total_votes = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




    


    












   
