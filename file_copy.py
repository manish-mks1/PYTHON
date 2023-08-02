#Note: create a text file as “input.txt” and write some date in it. This will be used in the program.

with open("input.txt","r") as input:
    with open("output.txt","w") as output:
        for line in input: output.write(line)

    print("JOB DONE!!")

