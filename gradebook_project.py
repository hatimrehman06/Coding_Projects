last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]


#Listing subjects
subjects = ["physics" , "calculus", "poetry", "history"]
#Listing grades
grades = [ 98 , 97 , 85 , 88]

#Creating a two-dimensional list to combine subjects and grades
gradebook = [["physics", 98], ["calculus" , 97], ["poetry" , 85], ["history" , 88]]

#printing gradebook
print (gradebook)

#Adding other subjects
gradebook.append(["computer science" , 100])
gradebook.append(["visual arts", 93])

#Adding 5 points to visual arts grade
gradebook[-1][1] += 5

#Switching poetry class to pass and fail instead of numerical
gradebook[2].remove(85)
gradebook[2].append("Pass")


#Cmbining last semsester gradebook with current
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
