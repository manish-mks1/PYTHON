str=input("Enter a string to check palindrome:")
rev_str = ""
for i in str:
	rev_str = i + rev_str

if (str == rev_str):
	print("Your string is palindrome")
else:
	print("No, Your string is not palindrome ")