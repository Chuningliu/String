# 91. Write a program to accept a string and display each word and it's length.

str = "Hello World How are you?"
str = str.split (' ')
for words in str:
	print (words),"(", len (words), ")",(len(str))

