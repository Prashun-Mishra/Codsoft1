# try:
#     print("Raising an exception")
#     raise ZeroDivisionError
# except ZeroDivisionError:
#    print ("can,t divide by zero")





# a=int(input("Enter a no.:"))
# b=int(input("Enter a no.:"))

# try:
#     print("Checking for exception") 
#     c=a/b
# except ZeroDivisionError:
#      print("An exception occured")   
# else:
#      print("No exception occured")  
# finally:
#      print("It will always execute")         
def count_letter_occurrences(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

# Example usage:
input_string = input("Enter a string: ")
input_letter = input("Enter a letter to count: ")

occurrences = count_letter_occurrences(input_string, input_letter)
print(f"The letter '{input_letter}' occurs {occurrences} times in the string.")


