'''
Program Name: EECS 348 Assignment 1
Description: show emails based on a priority queue managed by a maxHeap
Inputs: test file labelled "Assignment1_Test_File.txt"
Outputs: next email and number of unread emails
Collaborators: 
Other Sources: stackOverflow
Author: Warren Tan
Creation Date: 27/08/2025
'''

# path for input file
filePath = "Assignment1_Test_File.txt"

def main():
    # make a max heap to hold/prioritise emails
    myMaxHeap = maxHeap()

    # "open" function obtained from stackOverflow
    # takes "fileName" and reads it line-by-line
    with open(filePath, 'r') as file:
        for line in file:
            # find which command is being sent
            # get the first word of command (ex: "EMAIL", "COUNT", "NEXT", "READ")
            match line.strip().split(" ")[0]:
                case "EMAIL": # registers information about email
                    myMaxHeap.insert(Email(line[6:]))
                case "COUNT": # returns # of unread emails
                    print(f"There are {myMaxHeap.size} emails to read.")
                case "NEXT": # find next email in priority list
                    print(f"{myMaxHeap.data[-1] if myMaxHeap.size > 0 else 'There are no emails to read'}")
                case "READ": # output email at current index
                    myMaxHeap.pop()
                case _: # no command found
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
        output += f"Next email:\n\tSender: {self.sender}\n\tSubject: {self.subject}\n\tDate: {self.date}"
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

class maxHeap:
    def __init__(self, data=None):
        if data == None:
            self.data = []
            self.size = 0
        else:
            self.data = data
            self.size = len(data)
    
    def insert(self, element):
        self.data.append(element)
        self.size += 1
        self.heapify()

    def heapify(self):
        # iterate backwards through list
        for i, _ in reversed(list(enumerate(self.data))):
            # fix heap by swapping parent and repeating until correct
            while i != 0 and self.data[i] > self.data[i // 2]:
                self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
                i //= 2

    def pop(self):
        if self.size > 0:
            self.data.pop(-1)
            self.size -= 1
        else:
            print(f"No elements in heap")

if __name__ == "__main__":
    main()