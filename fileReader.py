import os

def readFile(file_path):
    try:
        with open(file_path, 'r') as file:
            # Split the lines and create a 2D array
            content_array = [line.strip().split() for line in file.readlines()]
        return content_array
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def print2dArray(array):
    for row in array:
        print(row)

def getTextFiles():
    files = os.listdir('.')
    # Filter out only text files (files ending with .txt)
    text_files = [file for file in files if file.endswith('.txt')]
    return text_files
