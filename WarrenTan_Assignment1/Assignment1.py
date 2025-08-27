'''
Program Name: EECS 348 Assignment 1
Description: 
Inputs: test file labelled "Assignment1_Test_File.txt"
Outputs: Next email and number of unread emails
Collaborators: 
Other Sources: stackOverflow
Author: Warren Tan
Creation Date: 27/08/2025
'''

# path for input file
filePath = "Assignment1_Test_File.txt"

def main():
    # make a max heap to hold emails
    # myMaxHeap

    # "open" function obtained from stackOverflow
    # takes "fileName" and reads it line-by-line
    with open(filePath, 'r') as file:
        for line in file:
            # find which command is being sent
            # get the first word of command (ex: "EMAIL", "COUNT", "NEXT", "READ")
            match line.strip().split(" ")[0]:
                case "EMAIL": # registers information about email
                    print(f"COMMAND EMAIL: {line[6:].strip().split(',')}")
                case "COUNT": # returns # of unread emails
                    print(f"COMMAND COUNT: There are {'myMaxHeapSize'} emails to read.")
                case "NEXT": # find next email in priority list
                    print("COMMAND NEXT: Finding next email... (no output for \'NEXT\')")
                case "READ": # output email at current 
                    print("COMMAND READ: Reading current email.")
                case default: # no command found
                    print(f"There was no command found on line: {line}")

if __name__ == "__main__":
    main()