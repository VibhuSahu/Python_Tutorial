import os

# Get the path of the current script
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)

print("Current script path:", script_path)
print("Current script directory:", script_directory)



# Get the current working directory
current_directory = os.getcwd()

# Get the parent folder path
parent_directory = os.path.dirname(current_directory)

print("Parent folder path:", parent_directory)
