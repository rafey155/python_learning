# Take a key from the user and check whether it exists in a dictionary.
new_dist = {
    "stu_name" : "rafey",
    "roll no" : 2200100310,
    "marks" : "89"
}
key = input("enter your key : ")
if key in new_dist:
    print("key  present in dictonery")
else:
    print(" key dose not present in dictonary")