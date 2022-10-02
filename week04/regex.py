# regex.py
# Christine Marra
# CSCI 77800 Fall 2022
# Collaborator: Sarah McCoy
# REFERENCED: https://regexr.com/3f8cm


import re



def find_names(line):
    pattern = r"([A-Za-z][-,A-Za-z. ']+[ ]*)+"
    result = re.findall(pattern, line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_names(line)
    if (len(result) > 0):
        print(result)


# def find_name(line):
#     #pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
#     #result = re.findall(pattern,line)

#     pattern=[A-Z]([a-z]+|\.)(?:\s+[A-Z]([a-z]+|\.))*(?:\s+[a-z][a-z\-]+){0,2}\s+[A-Z]([a-z]+|\.)
#     result = result + re.findall(pattern,line)
#     return result


# f = open("names.txt")
# for line in f.readlines():
#     #print(line)
#     result = find_name(line)
#     if (len(result)>0):
#         print(result)
