import csv
import os

# Load csv file to work with
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Variables to solve for
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        candidate_name = row[2]
        # Total number of votes cast
        total_votes += 1
        # A complete list of candidates who received votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Total number of votes each candidate received
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    # Percentage of votes each candidate won
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
       # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

# The winner of the election based on popular vote
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        print(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
