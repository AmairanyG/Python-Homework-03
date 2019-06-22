# Importing Modules
import os
import csv

# Setting path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Create empty lists to store data
voter_id = []
candidates = []
unique_candidates = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    header = next(csvreader)

   # store data from csv file into individual lists to run formulas on it later
    for row in csvreader:
        voter_id.append(row[0])
        candidates.append(row[2])
    
    # Count total number of votes cast from voter_id list that was appended in the for loop
    total_voters = len(voter_id)
    
    # make a unique list of candidates who recieved votes via dictionary trick
    unique_candidates = list(dict.fromkeys(candidates))
 
    # Calculate each candidates total votes and percentage of votes recieved
    Khan_Count = candidates.count("Khan")
    Khan_Percent = round((Khan_Count / total_voters) * 100, 2)
  
    Correy_Count = candidates.count("Correy")
    Correy_Percent = round((Correy_Count / total_voters) * 100, 2)
  
    Li_Count = candidates.count("Li")
    Li_Percent = round((Li_Count / total_voters) * 100, 2)
 
    OTooley_Count = candidates.count("O'Tooley")
    OTooley_Percent = round((OTooley_Count / total_voters) * 100, 2)
  
    # Calculate the candidate with the most votes and returns the name 
    Winner = max(range(len(voter_id)), key = lambda x: voter_id[x])
    WinnerName = candidates[int(Winner)]
   
# Generate Output Summary
output = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {(total_voters):,}\n"
    f"----------------------------\n"
    f"Khan: {Khan_Percent:,}% ({Khan_Count:,})\n"
    f"Correy: {Correy_Percent:,}% ({Correy_Count:,})\n"
    f"Li: {Li_Percent:,}% ({Li_Count:,})\n"
    f"O'Tooley: {OTooley_Percent:,}% ({OTooley_Count:,})\n"
    f"----------------------------\n"
    f"Winner: {str(WinnerName)}\n"
    f"----------------------------\n")
      
# Print the output to terminal
print(output)

#Export the results to text file
file = "PyPoll_Report.txt"
with open(file, "w") as f:
    f.write(output)