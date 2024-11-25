#4

def search_list(user_list,name):
    index=0
    for i in user_list:
        if(i.upper()==name.upper()):
            return index
        index=index+1
    return -1



values=input("Enter values:")
user_list=values.split()
name=input("Enter the name to be search:")
answer=search_list(user_list,name)
print(answer)