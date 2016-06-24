# Created 24/06/2016 #
# Last edited 24/06/2016 #
# Most recent changes made by: jedijackattack #

'''
------Basics for code-----

Indent size must be 4
    like this
        and this.
        
All functions must have docstrings

    def BasicTestFunction(x,y):
        """This is the docstring explain the function here if you don't it won't be merged"""
        print(x,y)
        pass
        
All variables and functions that are not 1 letter tempary vars must start with capital letters and follow the C 
variable guide. e.g. onetwothree would be OneTwoThree.
    
    def TheFunction(x):
        """multiplies two numbers"""
        BasicValue = 4
        print(x*BasicValue)
        pass

All functions must end in pass, continue, break or return.

Functions should do one task and one task only. If it can be split into 2 tasks split it. They can call other functions.

A classes __init__ function must be the first function in the class file.

We will use self as the variable to pass into argument 1 of the __init__ function.

All variables in classes will be self.[name of variable] and then will have a comment specifing data type.

Strings must use double quote marks and charaecters by them selves use single.

All projects must use a main.py file.


------Basics reporting issues, milestones and pushing, pulling and merging-----

If you report a issues please tag it correctly.

Milestones will have due dates, if you can not finish it with in that time, talk to the project manager(s)

Never directly push to master unless given express permision by the project manager, 
always make a new branch/fork and ask for review and merge.

Allways pull down the latest version before you start editing.

'''

