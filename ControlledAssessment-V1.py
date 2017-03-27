def enterNotes():
        usrNote1 = input("Enter the Student firstname: ")
        usrNote2 = input("Enter the Student Lastname: ")
        usrNote3 = input("Enter the Student Date of Birth: ")
        usrNote4 = input("Enter the Student Address: ")
        usrNote5 = input("Enter the Student Phone Number: ")
        usrNote6 = input("Enter the Student Gender: ")
        usrNote7 = input("Enter the Student Tutor Group: ")
        usrNote8 = input("Enter the Student email address: ")
        pos = (len(notebook)+1)
        entry = (pos, usrNote1, usrNote2, usrNote3, usrNote4, usrNote5, usrNote6, usrNote7, usrNote8)
        notebook.append(entry)

def printNotes():
    for counter in range(0,len(notebook)):
        print(notebook[counter])

def chgNote():
    chgeNote = int(input("Enter the index of the Student to replace: "))
    chgeNoteTxt = input("Enter the text to replace in the note: ")
    chgeNoteTxtNum = (chgeNote, chgeNoteTxt)
    notebook.insert(chgeNote -1,chgeNoteTxtNum)
    notebook.pop(chgeNote)
    
def main():
# This isn't working yet, fix reading into the array
        noteFile = open("studentsControlledY10.txt", "r")
        for line in noteFile:
                notebook.append(line)
        print("Options:")
        print("Choose 1 to enter Students")
        print("Choose 2 to display Students")
        print("Choose 3 to change a Student")
        print("Choose 4 to save students")
        print("Choose 5 to exit without saving")
        usrOptn = int(input("Enter option: "))
        if usrOptn == 1:
                enterNotes()
                main()
        elif usrOptn == 2:
                printNotes()
                main()
        elif usrOptn == 3:
                chgNote()
                printNotes()
                main()
        elif usrOptn == 4:
                noteFile = open("studentsControlledY10.txt", "a")
                for count in range(0, len(notebook)):
                        tempLine = str(notebook[count])
                        print(tempLine)
                        noteFile.write(tempLine)
                        noteFile.write("\n")
                noteFile.close()
                main()
        elif usrOptn == 5:
                exit()
        else:
                print("Not a valid option, try again")
                main()

notebook = []
main()
