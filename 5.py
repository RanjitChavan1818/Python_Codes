binary = input("Enter the Binary numbers ").split(",")
for i in binary:
    if int(i) % 5 == 0:  
        print(i)