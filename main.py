import ExpandableMenuStructure
import Functions

FunctionsForMainMenu = {
    "Create new tab":Functions.CreateNewTab,
    "Open tab":Functions.OpenTab,
    "Delete tab":Functions.DeleteTab,
    "Quit":Functions.Quit
}

TableTitle = " = = = = = M E N U = = = = = "
InputString = "Select the number of the function you want to run:"

print(' Jedi Painting & Decorating Co.')

while True:
    ExpandableMenuStructure.TotalMenu(FunctionsForMainMenu,TableTitle,InputString)
    pass

