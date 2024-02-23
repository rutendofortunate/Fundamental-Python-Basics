#r is read, l only want to read the information in the file
employee_file = open("employees .txt", "r")

#print(employee_file.readable())
print(employee_file.readlines())

employee_file.close()

#w is write, l want to write and change some information
#open("employees.docx", "w")

#a is append, append information onto the file, add more information only to the end of the file
#open("employees.docx", "a")

# r+ , you can read and write
#open("employees.docx", "r+")