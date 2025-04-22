import matplotlib.pyplot as plt
import os

fake_var = True
while fake_var:
    print ("""1. Student grade
2. Assignment statistics
3. Assignment graph""")
    print()

    select = input("Enter your selection: ")
    if select == "1":
        final_grade = 0
        name = input("What is the student's name: ")
        with open("data/students.txt", "r") as file1:
            for line1 in file1:
                if name in line1:
                    with open("data/assignments.txt", "r") as file2:
                        for i, line2 in enumerate(file2, start=1):
                            if (i - 2) % 3 == 0:
                                assignment_code = line2[:-1]
                            if i % 3 == 0:
                                for filepath in os.listdir("data/submissions"):
                                    with open("submissions/" + filepath, "r") as file3:
                                        for line3 in file3:
                                            if assignment_code in line3:
                                                if line1[:3] in line3:
                                                    grade = int(line3[-2::1])
                                                    final_grade += (grade/100) * int(line2)
                    print(f"{int(round((final_grade/1000)*100, 0))}%")
                    print()
                    break
            else:
                print("Student not found")
                print()
        file1.close()
        file2.close()
        file3.close()

    elif select == "2":
        min_grade = 0
        max_grade = 0
        avg_grade = 0
        assignment = input("What is the assignment name: ")
        with open("data/assignments.txt", "r") as file1:
            lines = list(file1)
            for i, line1 in enumerate(lines):
                if assignment == line1[:-1]:
                    assignment_code = lines[i+1][:-1]
                    for filepath in os.listdir("data/submissions"):
                        with open("submissions/" + filepath, "r") as file2:
                            for line2 in file2:
                                if assignment_code in line2:
                                    grade = int(line2[-2::1])
                                    avg_grade += grade
                                    if grade > max_grade:
                                        max_grade = grade
                                    if (grade < min_grade) or (min_grade == 0):
                                        min_grade = grade
                    print(f"Min: {min_grade}%\nAvg: {int(round(avg_grade/30, 0))}%\nMax: {max_grade}%")
                    print()
                    break
            else:
                print("Assignment not found")
                print()
        file1.close()
        file2.close()

    elif select == "3":
        grade_list = []
        assignment = input("What is the assignment name: ")
        with open("data/assignments.txt", "r") as file1:
            lines = list(file1)
            for i, line1 in enumerate(lines):
                if assignment == line1[:-1]:
                    assignment_code = lines[i + 1][:-1]
                    for filepath in os.listdir("submissions"):
                        with open("submissions/" + filepath, "r") as file2:
                            for line2 in file2:
                                if assignment_code in line2:
                                    grade = int(line2[-2::1])
                                    grade_list.append(grade)
                    grade_list.sort()
                    plt.hist(grade_list, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
                    plt.show()
                    print()
                    break
            else:
                print("Assignment not found")
                print()
        file1.close()
        file2.close()
