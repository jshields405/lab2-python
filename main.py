# Author: Jack Shields jcs6283@psu.edu
# Collaborator: Jack Scallan - jgs5472@psu.edu
# Collaborator: Danielle Alamo - dca5244@psu.edu
# Section: 10
# Breakout: 8

def getLetterGrade(grade):
  if(grade>=93.0):
    return "A"
  elif(grade<93.0 and grade>= 90.0):
    return "A-"
  elif(grade<90.0 and grade>= 87.0):
    return "B+"
  elif(grade<87.0 and grade>= 83.0):
    return "B"
  elif(grade<83.0 and grade>= 80.0):
    return "B-"
  elif(grade<80.0 and grade>= 77.0):
    return "C+"
  elif(grade<77.0 and grade>= 70.0):
    return "C"
  elif(grade<70.0 and grade>= 60.0):
    return "D"
  elif(grade<60.0):
    return "F"

def run():
  gradeNum = input("Enter your CMPSC 131 grade: ")
  gradeNum = float(gradeNum)
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(gradeNum)}.")


if __name__ == "__main__":
  run()