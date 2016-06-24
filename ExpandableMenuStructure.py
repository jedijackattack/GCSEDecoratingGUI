def TotalMenu(SelectionTable,TableHeading,InputLine):
    """Complete hassle free menu generation just follow the dictionary set up guide at the bottom"""

    INPUT = None

    print(TableHeading)

    DisplayMenu(SelectionTable)

    try:
        INPUT = int(input(InputLine))

    except Exception as e:
        print(e)

    print(INPUT)
    RunSelectedFunction(SelectionTable,INPUT)
    pass



def DisplayMenu(SelectionTable):
    """Displays the table in a numbered list for easy selection"""

    for counter,Display in enumerate(SelectionTable.keys()):
        print("{0}.".format(counter),end="")
        print(Display)
        pass
    pass



def RunSelectedFunction(SelectionTable,UserInput):
    """Runs the selected function and checks for errors."""

    A = None

    for counter,i in enumerate(SelectionTable.keys()):
            if(counter == UserInput and i in SelectionTable.keys()):
                A = i
            pass

    try:
        SelectionTable[A]()

    except Exception as e:
        print(e)

    pass


"""
Please set out your dictionary with the functions having no brackets e.g.
DisplayMenu(x) would be DisplayMenu .
If you need to pass through variables message me and I may start a project for it.
"""