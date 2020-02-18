#!/usr/bin/python3
import os
import sys
import zipfile

userinput = sys.argv[1]


def main() -> str:
    if userinput + ".zip" in os.listdir():
        with zipfile.ZipFile(userinput + ".zip", 'r') as zip_ref:
            zip_ref.extractall(userinput)
        os.remove(userinput + ".zip")
        return "Successful!"
    else:
        return "Manual-exception-handling : Invalid name !"


if __name__ == "__main__":
    main()
