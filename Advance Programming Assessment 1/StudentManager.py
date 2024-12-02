#Exercise3: Student Manager

import tkinter as tk
from tkinter import messagebox

#This list is used to hold the students' data.
students_data = []

#This function is used to load student data from the studentMarks.txt file.
def load_student_data():
    global students_data
    students_data = []
    try:
        with open("studentMarks.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                student_id, name, coursework1, coursework2, coursework3, exam_score = parts
                student_id, coursework1, coursework2, coursework3, exam_score = int(student_id), int(coursework1), int(coursework2), int(coursework3), int(exam_score)
               
                coursework_total = coursework1 + coursework2 + coursework3
                overall_percentage = (coursework_total + exam_score) / 160 * 100  
               
                #This will calculate the total marks.
                total_marks = coursework_total + exam_score
               
                #This is a student dictionary, append it to the list.
                student = {
                    "id": student_id,
                    "name": name,
                    "coursework1": coursework1,
                    "coursework2": coursework2,
                    "coursework3": coursework3,
                    "exam": exam_score,
                    "coursework_total": coursework_total,
                    "overall_percentage": overall_percentage,
                    "total": total_marks,
                    "grade": ""  
                }
                students_data.append(student)
               
        calculate_grades(students_data)
    except FileNotFoundError:
        messagebox.showerror("Error", "The 'studentMarks.txt' file is missing. Please check the file location.")

#This is a function used to calculate grades based on overall percentage.
def calculate_grades(students):
    for student in students:
        overall_percentage = student["overall_percentage"]
        if overall_percentage >= 70:
            student["grade"] = "A"
        elif overall_percentage >= 60:
            student["grade"] = "B"
        elif overall_percentage >= 50:
            student["grade"] = "C"
        elif overall_percentage >= 40:
            student["grade"] = "D"
        else:
            student["grade"] = "F"

#This function is used to display all the student records.
def display_all_students():
    output = ""
    total_percentage = 0  
    total_students = len(students_data)
   
    for student in students_data:
        output += (f"Name: {student['name']}\n"
                   f"Number: {student['id']}\n"  
                   f"Coursework Total: {student['coursework_total']}\n"
                   f"Exam Marks: {student['exam']}\n"
                   f"Overall Percentage: {student['overall_percentage']:.2f}%\n"
                   f"Grade: {student['grade']}\n\n")
        total_percentage += student["overall_percentage"]  
       
    if total_students > 0:
        average_percentage = total_percentage / total_students
    else:
        average_percentage = 0
       
    output += f"Total Students: {total_students}\n"
    output += f"Average Percentage: {average_percentage:.2f}%"
   
    display_output(output)

#This function is used to display the highest score.
def display_highest_score():
    highest_score = max(students_data, key=lambda x: x['overall_percentage'])
    output = f"Name: {highest_score['name']}\n"
    output += f"Number: {highest_score['id']}\n"  
    output += f"Coursework Total: {highest_score['coursework_total']}\n"
    output += f"Exam Marks: {highest_score['exam']}\n"
    output += f"Overall Percentage: {highest_score['overall_percentage']:.2f}%\n"
    output += f"Grade: {highest_score['grade']}\n"
    display_output(output)

#This function is used to display the lowest score.
def display_lowest_score():
    lowest_score = min(students_data, key=lambda x: x['overall_percentage'])
    output = f"Name: {lowest_score['name']}\n"
    output += f"Number: {lowest_score['id']}\n"  
    output += f"Coursework Total: {lowest_score['coursework_total']}\n"
    output += f"Exam Marks: {lowest_score['exam']}\n"
    output += f"Overall Percentage: {lowest_score['overall_percentage']:.2f}%\n"
    output += f"Grade: {lowest_score['grade']}\n"
    display_output(output)

#This function is used to display the individual student record based on dropdown selection.
def view_individual_student_record():
    selected_student_name = dropdown_var.get()
    
    #This will find the student record based on name.
    selected_student = next((student for student in students_data if student["name"] == selected_student_name), None)
    
    if selected_student:
        output = (f"Name: {selected_student['name']}\n"
                  f"Number: {selected_student['id']}\n"  
                  f"Coursework Total: {selected_student['coursework_total']}\n"
                  f"Exam Marks: {selected_student['exam']}\n"
                  f"Overall Percentage: {selected_student['overall_percentage']:.2f}%\n"
                  f"Grade: {selected_student['grade']}\n")
    else:
        output = "Student not found."

    display_output(output)

#This function is used to display the output in the text box.
def display_output(output):
    output_box.delete(1.0, tk.END)  
    output_box.insert(tk.END, output) 

def main():
    global dropdown_var, output_box
    load_student_data()
   
    root = tk.Tk()
    root.title("Student Records Manager")
   
    #Set a background color.
    root.configure(bg="#F5F5DC")  
   
    #This will create the main window frame.
    frame = tk.Frame(root, bg="#F5F5DC")  
    frame.pack(padx=20, pady=20)
   
    title_label = tk.Label(frame, text="Student Manager", font=("Arial", 30, "bold"), bg="#F5F5DC", fg="black")  
    title_label.grid(row=0, column=0, columnspan=3, pady=30)
   
    btn_all = tk.Button(frame, text="View All Student Records", width=30, height=2, font=("Arial", 16), command=display_all_students, bd=3, relief="raised", highlightbackground="black", bg="#F4B7B1")
    btn_all.grid(row=1, column=0, padx=15, pady=10)

    btn_highest = tk.Button(frame, text="Show Highest Score", width=30, height=2, font=("Arial", 16), command=display_highest_score, bd=3, relief="raised", highlightbackground="black", bg="#F4B7B1")
    btn_highest.grid(row=1, column=1, padx=15, pady=10)

    btn_lowest = tk.Button(frame, text="Show Lowest Score", width=30, height=2, font=("Arial", 16), command=display_lowest_score, bd=3, relief="raised", highlightbackground="black", bg="#F4B7B1")
    btn_lowest.grid(row=1, column=2, padx=15, pady=10)

    label_id = tk.Label(frame, text="View Individual Student Record:", font=("Arial", 18), bg="#F5F5DC", fg="black")
    label_id.grid(row=2, column=0, padx=15, pady=10)

    dropdown_var = tk.StringVar()
    dropdown_menu = tk.OptionMenu(frame, dropdown_var, *[student['name'] for student in students_data])
    dropdown_menu.config(width=20, font=("Arial", 18))  
    dropdown_menu.grid(row=2, column=1, padx=15, pady=10)

    btn_view_record = tk.Button(frame, text="View Record", width=20, height=2, font=("Arial", 16), command=view_individual_student_record, bd=3, relief="raised", highlightbackground="black", bg="#F4B7B1")
    btn_view_record.grid(row=2, column=2, padx=15, pady=10)

    #A box to display results.
    output_box = tk.Text(frame, height=12, width=80, wrap=tk.WORD, font=("Arial", 14), 
                         bd=3, relief="solid", highlightbackground="black", highlightcolor="black")
    output_box.grid(row=3, column=0, columnspan=3, pady=20)
   
    root.mainloop()

if __name__ == "__main__":
    main()
