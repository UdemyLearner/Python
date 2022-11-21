programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary)

programming_dictionary["Loop"]="Doing Something again and again"

empty_dictionary={}
print(empty_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    print()
    
    
    
    

# Coding Exercise solution 
# Q) https://app.codingrooms.com/w/7z43WTw4vL99

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="Outstanding"
    elif score>80:
        student_grades[student]="Exceeds Expectation"
    elif score>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"        
    
# 🚨 Don't change the code below 👇
print(student_grades)