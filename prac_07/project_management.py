"""
CP1404 - Practical 07
Estimate: 2hrs
Timer Recorded: 29hrs
Actual Estimate: like 3hrs? spread out over 2 days
"""

import datetime
from project import Project

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
    projects = load_projects()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects  = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            try:
                # Code stolen from prac
                date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
                date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
                print(f"That day is/was {date.strftime('%A')}")
                print(date.strftime("%d/%m/%Y"))
                # End of code stolen from prac
                filter_by_date(projects, date)
            except ValueError:
                print("That wasn't a date. Try Again :)")
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid Menu Choice.")
        print(MENU)
        choice = input(">>> ").upper()


def save_projects(projects, filename = DEFAULT_FILENAME):
    """Save a list of projects to a tab-delimited txt file."""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for project in projects:
            project_string = "\t".join([
                project.name,
                project.start_date.strftime("%d/%m/%Y"),
                str(project.priority),
                str(project.cost_estimate),
                str(project.completion_percentage)
            ])
            out_file.write(project_string + "\n")

    print(f"Projects saved to {filename}")


# Ran out of time to do error checking due to some unexpected home events :(
def add_project(projects):
    """Append a project to the current list of projects."""
    name = input("Enter project name: ")
    start_date_string = input("Enter start date: ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Enter priority: "))
    cost_estimate = float(input("Enter cost estimate: "))
    completion_percentage = float(input("Enter completion percentage: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print(f"Added {new_project}")



def update_project(projects):
    """Update priority/completion percentage for a project."""
    for project_index, project in enumerate(projects):
        print(f"{project_index + 1}. {project}")

    try:
        project_to_update = int(input("Choose a project to update: "))
        project = projects[project_to_update - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    # Get new values from user
    new_priority_input = input("Enter a new priority (or leave blank): ")
    new_completion_input = input("Enter a new completion percentage (or leave blank): ")

    if new_priority_input.strip():
        try:
            project.priority = int(new_priority_input)
        except ValueError:
            print("Invalid priority — keeping previous value.")

    if new_completion_input.strip():
        try:
            project.completion_percentage = float(new_completion_input)
        except ValueError:
            print("Invalid completion % — keeping previous value.")

    print(f"Updated project: {project}")


def filter_by_date(projects, filter_date = datetime.date.today()):
    """Display projects starting on or after a chosen date."""
    Project.comparison_field = "start_date"
    filtered_projects = [project for project in projects if project.start_date >= filter_date]

    if not filtered_projects:
        print(f"No projects starting on or after {filter_date:%d/%m/%Y}.")
        return
    else:
        print(f"Projects starting on or after {filter_date:%d/%m/%Y}:")
        for project in filtered_projects:
            print(project)


def display_projects(projects):
    """Displays projects separated by complete/incomplete and sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]
    incomplete_projects.sort()
    complete_projects.sort()
    if incomplete_projects:
        print("Incomplete Projects:")
        for project in incomplete_projects:
            print(project)
    if complete_projects:
        print("Complete Projects:")
        for project in complete_projects:
            print(project)


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
                    #projects.append([name, start_date, int(priority), float(cost_estimate), float(completion_percentage)])
                    projects.append(Project(name, start_date, int(priority), float(cost_estimate), float(completion_percentage)))
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