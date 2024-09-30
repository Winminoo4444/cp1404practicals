# 1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.
FILENAME = "name.txt"
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2. In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
FILENAME = "numbers.txt"
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)