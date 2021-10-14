import os
import csv

# filepath = "/Users/gurbindesidhu/Desktop/Pythonhomework/pythonchallenges/Pypoll.py/Resources/election_data.csv"
filepath = "./Resources/election_data.csv"
filepathout = "./analysis/Election_Results.txt"
count = 0
candidate_list = []
popular_candidate = []
candidate_choice = []
vote_count = {}
vote_percent = []
total_votes = 0
candidate_name=0
winning_count=0
#voter_output=[]


#def vote_percent(candidate_name):

with open(filepath,newline='') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        count = count + 1
        candidate_name=row[2]
        #total_number += 1
        #print('candidate name', candidate_name)
    
        #candidate_list.append(candidate_name)
        

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            vote_count[candidate_name] = 1
        else:
            vote_count[candidate_name] = vote_count[candidate_name] + 1
    # print(vote_count)

with open(filepathout,"w") as txt_file:
    for candidate in vote_count:
        votes=vote_count.get(candidate)
        vote_percent= (float(votes)/float(count))*100
        if(votes>winning_count):
            winning_count=votes
            winning_candidate= candidate
        voter_output= f"{candidate}:{vote_percent:3f}% ({votes})\n"
        txt_file.write(voter_output)
        print(voter_output)             
   
    Election_Results = (

       f"----------------------------------\n"
        f"Election_Results\n"

        f"Total votes:{count}\n"
        f"----------------------------------"
    )

    print(Election_Results,end="")

    winning_candidate_summary =(
    f"-------------------------\n"
    f"Winner:{winning_candidate}\n" 
    # f"---------------------------\n"
    # f"Each Candidate vote:{}"
    )

    # print(voter_output)
    

    print(winning_candidate_summary)

 #Creating output file:
# with open(filepathout,"w") as txt_file:


    
    txt_file.write(Election_Results)


    # txt_file.write(vote_count)
    
   
    txt_file.write(winning_candidate_summary)
    







    
   