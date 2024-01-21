import fileReader
import operations
tableNumber=0
tableFileNames=fileReader.getTextFiles()
tables=[]
tableNames=[]

def loadTables():
    print("""\nWelcome to the relational algebra query processor. 
You will need to load some tables into the processor. Tables 
are stored in .txt files using spaces and newlines.""")
    print("\nPlease choose a textfile to load as a table:")
    for i in range(len(tableFileNames)):
        print("",i,tableFileNames[i])
    selection=int(input("Which table would you like to load: "))
    tables.append(fileReader.readFile(tableFileNames[selection]))
    tableNames.append(tableFileNames[selection])

    print("\nPlease choose another textfile to load as a table:")
    for i in range(len(tableFileNames)):
        print("",i,tableFileNames[i])
    selection=int(input("Which table would you like to load: "))
    tables.append(fileReader.readFile(tableFileNames[selection]))
    tableNames.append(tableFileNames[selection])

    while selection !=-1:
        print("\nWould you like to load another file? choose a file number or -1 to exit:")
        for i in range(len(tableFileNames)):
            print("",i,tableFileNames[i])
        selection=int(input("Which table would you like to load or -1 to exit: "))
        if selection!=-1:
            tables.append(fileReader.readFile(tableFileNames[selection]))
            tableNames.append(tableFileNames[selection])

def autoloadTables():
    tables.append(fileReader.readFile(tableFileNames[0]))
    tables.append(fileReader.readFile(tableFileNames[1]))
    tables.append(fileReader.readFile(tableFileNames[2]))
    tableNames.append(tableFileNames[0])
    tableNames.append(tableFileNames[1])
    tableNames.append(tableFileNames[2])

def main():
    select=0
    autoloadTables()
    while select !="-1":
        select=input("""\nWhat would you like to do?
    1 Selection
    2 Projection
    3 Join
    4 Set
    5 Print a loaded table
Please input a number or a -1 to exit: """)
        match select:
            case "-1":
                print("Goodbye")
            case "1":
                print("\nPlease select a table to perform this operation on:")
                selectedTable=selectTable()
                condition=selectCondition().split()
                result=operations.selection(selectedTable,condition)
                displayResults(result)
            case "2":
                print("\nPlease select a table to perform this operation on:")
                selectedTable=selectTable()   
                columnTitles=input("Please enter the names of the columns you'd like to select, separated by spaces: ").split()
                result=operations.projection(selectedTable,columnTitles)
                displayResults(result)
            case "3":
                result=chooseJoin()
                displayResults(result)
            case "4":
                print("case 4")
            case "5":
                printaTable()
            case _:
                print("Please print a valid input.")



def selectTable():
    for i in range(len(tables)):
        print("",i,tableNames[i])
    choice=int(input("Please enter the number of the table you'd like to select: "))
    return tables[choice]

def selectTwoTables():
        print("\nPlease the left table to perform this operation on:")
        table1=selectTable()
        print("\nPlease the right table to perform this operation on:")
        table2=selectTable()
        return [table1,table2]

def selectTwoColumns():
    leftColumn=input("Please input a column from the left relation to compare through the opperator: ")
    rightColumn=input("Please input a column from the right relation to compare through the opperator: ")
    return [leftColumn,rightColumn]

def selectCondition():
    print("Type in the condition to apply to the selection. The string should be 3 values separated by spaces; a column name, an opporator (=, !=, <, >), and a value. \nEx: fname != zoltan")
    return(input("What is your condition: "))

def displayResults(result):
    print("\nThis is the resulting table: ")
    fileReader.print2dArray(result)
    choice=input("Would you like to save this relation (y/n)? ")
    if choice=="y":
        tableNames.append(input("Please name this new relation: "))
        tables.append(result)

def printaTable():
    print("\nPlease select a table to view:")
    table1=selectTable()
    fileReader.print2dArray(table1)

def chooseJoin():
    print("""Which type of join would you like to do?
1 Cartesian Product
2 Inner Join
3 Left Outer Join
4 Right Outer Join
5 Full Outer Join""")
    choice=input("Which join would you like to perform? ")
    if choice=="1":
        chosenTables=selectTwoTables()
        return operations.cartesianProduct(chosenTables[0],chosenTables[1])
    elif choice=="2":
        chosenTables=selectTwoTables()
        chosenColumns=selectTwoColumns()
        return operations.innerJoin(chosenTables[0],chosenTables[1],chosenColumns[0],chosenColumns[1])
    elif choice=="3":
        chosenTables=selectTwoTables()
        chosenColumns=selectTwoColumns()
        return operations.leftOuterJoin(chosenTables[0],chosenTables[1],chosenColumns[0],chosenColumns[1])    
    elif choice=="4":
        chosenTables=selectTwoTables()
        chosenColumns=selectTwoColumns()
        return operations.rightOuterJoin(chosenTables[0],chosenTables[1],chosenColumns[0],chosenColumns[1])    
    elif choice=="5":
        chosenTables=selectTwoTables()
        chosenColumns=selectTwoColumns()
        return operations.fullOuterJoin(chosenTables[0],chosenTables[1],chosenColumns[0],chosenColumns[1])  
main()