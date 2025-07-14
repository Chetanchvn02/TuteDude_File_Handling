txt = input("Enter the text to write to the file: ")
file = open('output.txt','w')
writing_file = file.write(txt)
print("Data successfully written to output.txt")
file.close()

txt = input("\nEnter the additional text to write to the file: ")
file = open('output.txt','a')
append_file = file.write(txt)
print("Data successfully appended")
file.close()

file = open('output.txt','r')
read_file = file.read()
print("\nFinal content of output.txt")
print(read_file)
file.close()

