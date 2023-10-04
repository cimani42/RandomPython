f = open("DOB.txt", "r+")
# print(f) # check to make sure file exists within folder location.

contents = ""
for line in f:
    contents = contents + line
print(contents)
f.close()  # always making sure to close after opening.

# Looking at the contents of the file, the information is delimited by a comma. This can be used to split_
# the information.
# Using the contents variable, delimit using the split function to get the elements.

elements = contents.split(",")
# print(elements)  # check

# print(len(elements)) # There are 26 elements in the list

# i = 0
# # print("Names and D.O.B")
# while i < len(elements):
#     print(elements[i]+",\n")
#     i += 1


rc = contents.replace(",", " ")
elements2 = rc.split(" ")

# print(elements2) # check
# print(len(elements2))

# elements2 contains 101 indices. The information needed shows on every 3rd, 4th, 5th element. (minus one for the index)
# need to create a new list to add the day month and year back together.
# Starting from index 0, add two to get the third and four to get the fifth.
# Format of data is first name, last name, DD, MM, YYYY. I can use this as a repetition of 5 indexes for each group.

listingDOB = []
x = 5
while x < len(elements2):
    if x % 5 == 0:
        dob = elements2[x - 3], elements2[x - 2], elements2[x - 1]
        listingDOB.append(dob)
    x += 5

# Using the while loop seems to be impacting on the number of returns found in the listingDOB. Will redo as a for loop.
# The error in the while loop was I has initially entered the modulos to divide by 4 not 5. Information matches.
listingDOB2 = []
index = 5
for x in range(index, len(elements2), 5):
    if x - 3 >= 0 and x - 2 >= 0 and x - 1 >= 0:
        dob = elements2[x - 3], elements2[x - 2], elements2[x - 1]
        listingDOB2.append(dob)

format_dob = []
for dob in listingDOB:
    dob_string = " ".join(map(str, dob))  # joins with a space
    format_dob.append(dob_string)
# print("*"*100)
# print(format_dob)

# print(listingDOB)
# print("*"*100)
# print(listingDOB2)

# can utilise the comma that was/is present in the contents and work back

# testtest = contents.split(" ")
# print(testtest)
#
# new_data = []
# i = 0
# while i < len(testtest):
#     if testtest[i] == ",":
#         if i >= 3:
#             dob = testtest[i - 1], testtest[i - 2], testtest[i - 3]
#             new_data.append(dob)
#     i += 1
#
# print(new_data)

# The above does not work as the information in the list is not correct.

print("*"*100)

print("Names and Date of Birth")
# i = 0
# # print("Names and D.O.B")
# while i < len(elements):
#     print(elements[i]+",\n")
#     i += 1
for wwe in elements:
    print(wwe)

print("*"*100)

print("Date of Births")
for e in format_dob:
    print(e)

print("*"*100)
