# Author: Max Smith
# File Name: module2labMS.py
# Description: This app accepts student names and GPAs, checks if they qualify for the Dean's List or Honor Roll, and prints appropriate messages based on their GPA.

def main():
    while True:
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            print("Exiting the program.")
            break
        
        first_name = input("Enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not qualify for either the Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()