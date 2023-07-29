list1 = []
n=int(input("Enter number of element to be input: "))
print("Enter ",n, " odd number or even number one by one:-")
for i in range(0,n):
    print("Enter ",i+1," element:",end=" ")
    store=int(input())
    list1.append(store)
even_count, odd_count = 0, 0
for ele in list1:
	if ele % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
