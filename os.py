import os

current_directory = os.getcwd()
print(f"Hey Canalp, this is the current_directory: {current_directory}")

new_directory = "C:/Users/canal/Desktop/os/new directory brought to you by the os module"
os.mkdir(new_directory)
print(f"Created a new directory: {new_directory}")

directory_contents = os.listdir("C:/Users/canal/Pictures/Screenshots")
print("Directory Contents:")
for item in directory_contents:
    print(item)