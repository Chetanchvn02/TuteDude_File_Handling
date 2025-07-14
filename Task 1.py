try:
    with open('sample.txt','r') as file:
        reading_file = file.read()
        print("Reading file content....")
        print(reading_file)
        file.close()
except FileNotFoundError:
    print("Error: The file sample.txt was not found.")