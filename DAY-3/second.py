# WAP TO CHECK IF THE LIST CONTAIN PALENDROME OR NOT 
# SOL-Reverse the string and compare it to the original.
list = [input("Enter the list :  ")]
copy_list = list.copy()
copy_list.reverse()
if(list == copy_list):
    print("palendrome")
else:
    print("not palendrome ")


