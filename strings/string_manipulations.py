print(','.join(['a','b','c']))

"""
the below line will throw error 
because python list doesn't have join method
but the javascript array have join method

"""
# print(['a','b','c'].join(','))

"""
spilt method will do the splitter on the called string 
return the list 

"""

print("My Cat name is chittu".split())

mail = """
spilt method will do the splitter on the called string 
return the list 

"""
print(mail.split('\n'))



"""
rjust , ljust method usage sample 
"""

def printPicnic(picnicitems:dict,leftwidth:int,rightwidth:int):
    print("PICNIC ITEM".center(30,'='))

    for k,v in picnicItems.items():
        print(k.ljust(leftwidth,'.') + str(v).rjust(rightwidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPicnic(picnicitems=picnicItems,leftwidth=20,rightwidth=10)







