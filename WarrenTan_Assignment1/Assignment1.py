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

    # temp list to hold variables
    priorityList = []

    # "open" function obtained from stackOverflow
    # takes "fileName" and reads it line-by-line
    with open(filePath, 'r') as file:
        for line in file:
            # find which command is being sent
            # get the first word of command (ex: "EMAIL", "COUNT", "NEXT", "READ")
            match line.strip().split(" ")[0]:
                case "EMAIL": # registers information about email
                    priorityList.append(Email(line[6:]))
                case "COUNT": # returns # of unread emails
                    print(f"COMMAND COUNT: There are {'myMaxHeapSize'} emails to read.")
                case "NEXT": # find next email in priority list
                    print("COMMAND NEXT: Finding next email... (no output for \'NEXT\')")
                case "READ": # output email at current 
                    print("COMMAND READ: Reading current email.")
                case default: # no command found
                    print(f"There was no command found on line: {line}")

class Email:
    def __init__(self, emailString):
        # split emailString into more managable variables
        self.sender, self.subject, self.date = emailString.strip().split(',')
        self.monthNum, self.dayNum, self.yearNum = self.date.split("-")
        # set initial priority based on sender
        self.senderPrio = 0
        match self.sender.lower():
            case "boss":
                self.senderPrio = 1
            case "subordinate":
                self.senderPrio = 2
            case "peer":
                self.senderPrio = 3
            case "importantperson":
                self.senderPrio = 4
            case "otherperson":
                self.senderPrio = 5

    # information in string for output
    def __str__(self):
        output = ""
        output += f"Next Email:\n\tSender: {self.sender}\n\tSubject: {self.subject}\n\tDate: {self.date}"
        return output

    # greater than attempts to sort by sender, then whichever was sent last
    def __gt__(self, other):
        # compare senderPrio
        if self.senderPrio != other.senderPrio:
            return self.senderPrio > other.senderPrio
        # compare yearNum
        if self.yearNum != other.yearNum:
            return self.yearNum > other.yearNum
        # compare monthNum
        if self.monthNum != other.monthNum:
            return self.monthNum > other.monthNum
        # compare dayNum
        if self.dayNum != other.dayNum:
            return self.dayNum > other.dayNum
        
        # base case
        return False
    
    # greater than attempts to sort by sender, then whichever was sent last
    def __lt__(self, other):
        # compare senderPrio
        if self.senderPrio != other.senderPrio:
            return self.senderPrio < other.senderPrio
        # compare yearNum
        if self.yearNum != other.yearNum:
            return self.yearNum < other.yearNum
        # compare monthNum
        if self.monthNum != other.monthNum:
            return self.monthNum < other.monthNum
        # compare dayNum
        if self.dayNum != other.dayNum:
            return self.dayNum < other.dayNum
        
        # base case
        return False
    
    # equal if same date and sender type
    def __eq__(self, other):
        prioBool = self.senderPrio == other.senderPrio
        dateBool = self.date == other.date
        return prioBool and dateBool

if __name__ == "__main__":
    main()