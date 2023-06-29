import os
import csv

#CSV file path with related dataset
csv_path = '/Users/katieloosararian/Class_Requirements/Module 3/Starter_Code/PyPoll/Resources/election_data.csv'

# variables 
total_votes= 0
candidate_votes= {}
winner= " "
winner_votes = 0

#read csv file 
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter= ',')
    header = next(csv_reader)

    # iteration over the rows
    for row in csv_reader: 
        # count total # of votes
        total_votes += 1

        #Candidates names
        candidate =  row[2]


        # add in the candidate to dict if not already presented
        if candidate not in candidate_votes: 
            candidate_votes[candidate] = 0

        # incerement the candidate vote count
        candidate_votes[candidate] += 1

# calculate the % of votes each candidate win and find the winner
results = []
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

#show results
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
for candidates, votes, percentage in results:
    print(f"{candidates}: {percentage: .3f}% ({votes}])")
print("---------------------------------")
print(f"Winner: {winner}")
print("---------------------------------")
