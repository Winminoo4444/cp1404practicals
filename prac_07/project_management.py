import datetime
from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
class_projects = []
project_dictionary = {}

def main():
    with open("projects.txt", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
        extract_data(data)
    choice = get_choice()
    while choice != "Q":
        if choice == "L":
            try:
                filename = input("Filename: ")
                input_file = open(f"{filename}.txt", "r")
                in_file = input_file.readlines()
                extract_data(in_file)
                input_file.close()
            except FileNotFoundError:
                print("Error no file of such name found")
        elif choice == "S":
            filename = input("Filename: ")
            output_file = open(f"{filename}.txt", "w")
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)
            for project in class_projects:
                print(
                    f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                    file=output_file)
            output_file.close()
        elif choice == "D":
            class_projects.sort()
            print("Incomplete Project: ")
            for project in class_projects:
                if not project.is_completed():
                    print(project)
            print("Completed Projects: ")
            for project in class_projects:
                if project.is_completed():
                    print(project)
        elif choice == "F":
            date_string = str(validate_date())
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            sorted_filtered_projects = []
            sort_project_by_date(date, sorted_filtered_projects)
            for project in sorted_filtered_projects:
                print(project)
            restore_datetime()
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = validate_date()
            priority = validate_priority("Priority: ")
            cost_estimate = validate_cost_estimate()
            completion_percentage = validate_percentage("Percent Complete: ")
            class_projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            for i, project in enumerate(class_projects, 0):
                print(
                    f"{i} {project.name}, start:{project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate}, completion: {project.completion_percentage}% ")
                project_dictionary[i] = project
            project_choice = validate_project_choice()
            print(project_dictionary[project_choice])
            new_percentage = validate_percentage("New Percentage: ")
            new_priority = validate_priority("New Priority: ")
            update_project(new_percentage, new_priority, project_choice)
        else:
            print("Invalid Choice")
        choice = get_choice()
    autosave()
    print("Thank you for using custom-built project management software.")

