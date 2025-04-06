taskslist = ['learn python' , 'brush up angular unit testing','gitlab package registry learning',
             'gitlab sast testing job integration','learnig linux' , 'learnig docker']

# iterating through list

for task in taskslist:
    # get index of an element in list
    print(f"{taskslist.index(task)+1} ) {task}")

# slice an array 


# check existance of element in list

if 'learn python' in taskslist:
    print("you have to learn python for this week....")
else:
    print("you have not added python in your learning path...")

# return length of an list

print(f"There are {len(taskslist)} tasks to complete this week...")

for i in range(5,10):print(i)

firstweektask = taskslist[:3]
print(f"first 2 days learn {firstweektask}")

print(f"remaining days learn pending tasks {taskslist[len(firstweektask)+1:]}")

# splicing with index 

print(taskslist[2:4])


# while operations over list 
# print every 3rd elements of the list 
for i in range(10):
    while i < 10:
        print(i)
        i+=3
    break;

# add new elem to the end of the list

taskslist.append("learn springboot")
print(f"{taskslist}")

# add elem at the specific index - this will add elem at the specific index and shift 
# remaining elem to right

taskslist.insert(3,"learn spring security")
print(taskslist[3:4]) #this will return ["learn spring security"]

if 'learn python' in taskslist: print(taskslist.index('learn python'))

# remove elem from the list 

if 'learn python' in taskslist: 
    print(taskslist.remove('learn python'))
    print(taskslist)

# sort the list 

taskslist.sort()
print(taskslist)

# reverse the list 

taskslist.reverse()
print(taskslist)

# removes the elem with the index

taskslist.pop(0)
print(taskslist)

print(len(taskslist[0]))
print(taskslist[0][0] ) # return the first char of the word
searchIndex = taskslist.index('gitlab package registry learning')
print(taskslist[searchIndex:searchIndex+1])