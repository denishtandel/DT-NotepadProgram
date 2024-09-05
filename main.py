import subprocess

def open_notepad():
    # Open Notepad on Windows
    subprocess.Popen(['notepad.exe'])

if __name__ == '__main__':
    open_notepad()

