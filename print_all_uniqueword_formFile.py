fname=input("enter file name with correct extension:") 
file_opened=open(fname)
our_list=list()	#creating an empty list

for line in file_opened:
    word=line.rstrip().split()	#rstrip for removing unwanted spaces
    for element in word:
        if element in our_list: 
            continue
        else:
            our_list.append(element) 
our_list.sort()
print(our_list)
