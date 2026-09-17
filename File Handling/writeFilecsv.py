import csv
employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "D:/PythonFromScratch/File Handling/output.txt"

try:
    with open(file_path, "w", newline = "") as file:
        writer = csv.writer(file)
        for employee in employees:
            writer.writerow(employee)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")