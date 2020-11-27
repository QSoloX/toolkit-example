import os
import subprocess


def main():
    getVersion = subprocess.check_output(
        "python --version", shell=True)
    if "2" in str(getVersion):
        print("This may be python2 this program is written in python3 please use python3 to install.")
        exit()
    os.system("pip install pipenv && pipenv install && pipenv shell")
    print(
        "To Enter the virtual env use the command:[pipenv shell] this setup file does do it after finishing.")


if __name__ == "__main__":
    main()
