# Hanlin Zhang
# Nov. 19, 2024
import os
from assignment import Assignment
import matplotlib.pyplot as plt

directory: str = os.path.dirname(os.path.realpath(__file__))

def main():
    print("""1. Student grade
2. Assignment statistics
3. Assignment graph
""")
    match input("Enter your selection: "):
        case "1":
            print(f"{getGrade(findStudent(input("What is the student's name: "))):0.00f}%")
        case "2":
            mi, ma, avg = getStats(findAssignment(input("What is the assignment name: ")))
            print(f"""Min: {mi:0.00f}%
Avg: {avg:0.00f}%
Max: {ma:0.00f}%""")
        case "3":
            l = getScores(findAssignment(input("What is the assignment name: ")))
            plt.hist(l, bins=10)
            plt.show()


def findStudent(name: str):
    first, last = name.split(" ")

    studentsFile: str = os.path.join(directory, "data", "students.txt")
    with open(studentsFile, "r") as file:
        for line in file:
            f, l = line.split(" ")
            l = l[:-1]
            if last == l:
                if f[3:] == first:
                    return f[:3]


def findAssignment(name: str) -> str:
    assignmentsFile: str = os.path.join(directory, "data", "assignments.txt")
    with open(assignmentsFile, "r") as file:
        for line in file:
            if line[:-1] == name:
                return file.readline()[:-1]
def loadAssignments() -> list[Assignment]:
    assignments: list[Assignment] = []
    assignmentsFile: str = os.path.join(directory, "data", "assignments.txt")
    i: int = 0
    with open(assignmentsFile, "r") as file:
        for line in file:
            match i % 3:
                case 0:
                    assignments.append(Assignment(name=line[:-1]))
                case 1:
                    assignments[-1].code = line[:-1]
                case 2:
                    assignments[-1].points = line[:-1]
            i += 1
    return assignments

def getGrade(student: int) -> int:
    grade: float = 0
    total: int = 0
    assignments: list[Assignment] = loadAssignments()
    files: list[str] = [f for f in os.listdir(os.path.join(directory, "data", "submissions"))]
    for path in files:
        with open(os.path.join(directory, "data", "submissions", path), "r") as file:
            fStudent, fAssignment, fScore = file.readline().split("|")
            if fStudent == student:
                for assignment in assignments:
                    if assignment.code == fAssignment:
                        grade += int(assignment.points) * int(fScore)
                        break
    for assignment in assignments:
        total += int(assignment.points)

    return grade / total

def getStats(assignment: str):
    mi: int = 999
    ma: int = -1
    total: int = 0
    count: int = 0
    files: list[str] = [f for f in os.listdir(os.path.join(directory, "data", "submissions"))]
    for path in files:
        with open(os.path.join(directory, "data", "submissions", path), "r") as file:
            fStudent, fAssignment, fScore = file.readline().split("|")
            fScore = int(fScore)
            if fAssignment == assignment:
                total += fScore
                count += 1
                if fScore < mi:
                    mi = fScore
                elif fScore > ma:
                    ma = fScore
    return mi, ma, total / count

def getScores(assignment: str):
    l = []
    files: list[str] = [f for f in os.listdir(os.path.join(directory, "data", "submissions"))]
    for path in files:
        with open(os.path.join(directory, "data", "submissions", path), "r") as file:
            fStudent, fAssignment, fScore = file.readline().split("|")
            if fAssignment == assignment:
                l.append(fScore)
    return l

if __name__ == '__main__':
    main()