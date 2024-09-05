import subprocess
import os
import time

from datetime import datetime
# Get the current date and time
now = datetime.now()
# Extract the date part
current_date = now.strftime('%A, %d %B %Y %H:%M:%S')


def create_or_update_file(file_path, content):
    # Open the file in append mode to update the file without overwriting existing content
    try:
        with open(file_path, 'a') as file:
            file.write(content + '\n')
            file.close()
        print(f"File updated: {file_path}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_notepad(file_path):
    # Open the file in Notepad
    subprocess.Popen(['notepad.exe', file_path])
    # Close the file

if __name__ == '__main__':
    # Define the file path and initial content
    user_home = os.path.expanduser("~")
    file_path = os.path.join(user_home, 'example.txt')

    content = f'File open on {current_date}'

    # Create or update the file
    create_or_update_file(file_path, content)

    # Open the file in Notepad
    open_notepad(file_path)




