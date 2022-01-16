# 104. Accept a string and display the entire string with the first 
# and last character in uppercase.
str = input("Enter any String")
print(str[0].upper() + str[1:-1] + str[-1].upper())