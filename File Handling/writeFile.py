# Python writing files (.txt, .json, .csv)

# txt_data = "I like pizza!"
# txt_data2 = "Meow!"

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]




file_path = "D:/PythonFromScratch/File Handling/output.txt"

# with open(file = file_path, mode = "w") as file:
# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")

# with mode = "x" it will give file exists error

# try:
#     with open(file_path, "x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

# with open(file_path, "a") as file:
#     file.write("\n" + txt_data2)
#     print(f"txt file '{file_path}' was created")

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
