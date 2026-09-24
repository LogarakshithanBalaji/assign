import os

def generate_report():
    student_count = os.getenv("STUDENT_COUNT", "45")
    course_name = "Cloud Architecture"
    
    file_name = "build_report.txt"
    
    with open(file_name, "w") as f:
        f.write(f"Course Name: {course_name}\n")
        f.write(f"Students Enrolled: {student_count}\n")
    
    print(f"Successfully generated {file_name} with {student_count} students.")

if __name__ == "__main__":
    generate_report()
