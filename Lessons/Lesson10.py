#######################################
# The Blue Marble Academy 
# File Operations in Python 
#######################################

# Creating a text file
file_name = "example.txt"

# Creating and writing to the file
# If a file with the same name does not exist it will be created, else the existing file will be opened 
# file.write will overwrite any existing infomation in example.txt. So, anything in example.txt will be deleted
def create_and_write_file():
    with open(file_name, 'w') as file:
        file.write("This is an example text file.\n")
        file.write("It contains multiple lines of text.\n")
        file.write("Python file handling is simple and powerful.\n")
    print(f"File '{file_name}' created and written successfully.")

# Reading from the file
def read_file():
    with open(file_name, 'r') as file:
        content = file.read()
        print("\nReading from file:")
        print(content)

# Appending to the file
# Appending means to add information to the end of the file!
# So, the information in example.txt is not deleted, unlike in file.write 
def append_to_file():
    with open(file_name, 'a') as file:
        file.write("Hello!!!!!!!!!!!!!!.\n")
    print(f"Data appended to '{file_name}'.")


# Demonstrate file operations
# Try just running the append_to_file() function 
# All functions in if __name__ == "__main__": will excecute whenever Lesson9 is ran
if __name__ == "__main__":
    # Create and write to the file
    create_and_write_file()

    # Read the file content
    read_file()
    
    # Append new content to the file
    append_to_file()
    
    # Closing the file is handled automatically by the 'with' statement
    print("\nAll operations completed successfully.")
