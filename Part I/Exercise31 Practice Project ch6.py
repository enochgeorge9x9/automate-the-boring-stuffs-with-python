#Table Printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
                     ['Alice', 'Bob', 'Carol', 'David'],
                     ['dogs', 'cats', 'moose', 'goose']]

#TODO: List all the items in the list
def printTable(tableData):
    tablemax = []
    for i in range(len(tableData)):
        m = len(max(tableData[i], key = len))
        tablemax.append(m)
    maximum = max(tablemax)

    for i in range(len(tableData[0])):
        print (tableData[0][i].ljust(maximum) + tableData[1][i].center(maximum) + tableData[2][i].rjust(maximum))
   
printTable(tableData)
