"""
CP1404 - Practical 07
Estimate: 2hrs
Actual:
"""

import datetime

DEFAULT_FILENAME = "projects.txt"
MENU = """Menu:
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid Menu Choice.")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename = DEFAULT_FILENAME):
    """Loads projects into a list of lists from a txt file."""
    # project.txt format "Name	Start Date	Priority	Cost Estimate	Completion Percentage"
    projects = []
    loaded_projects = 0
    load_project_failure_count = 0
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            in_file.readline()
            for line in in_file:
                try:
                    name, start_date_string, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
                    projects.append([name, start_date, int(priority), float(cost_estimate), float(completion_percentage)])
                    loaded_projects += 1
                except ValueError:
                    load_project_failure_count += 1
    except FileNotFoundError:
        print(f"{filename} not found, check that FILENAME is correct.")

    if load_project_failure_count > 0:
        print(f"Failed to load {load_project_failure_count} projects")
    print(f"Loaded {loaded_projects} projects.")
    return projects

main()