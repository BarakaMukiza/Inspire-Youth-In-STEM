#Make a table to solve quadratic equation
from prettytable import PrettyTable

#specify the column names while initializing the table
myTable = PrettyTable(["Variable","Value of x","Equation","Result"])

#add rows
myTable.add-row(["x","0","5x^3 +2 x^2 + 8x + 9  ","9"])
myTable.add_row(["x","1","5x^3 +2 x^2 + 8x + 9 ","26"])
myTable.add_row(["x","2","5x^3 +2 x^2 + 8x + 9 ","73"])
myTable.add_row(["x","3","5x^3 +2 x^2 + 8x + 9 ","180"])
myTable.add_row(["x","4","5x^3 +2 x^2 + 8x + 9 ","377"])
myTable.add_row(["x","5","5x^3 +2 x^2 + 8x + 9 ","694"])
myTable.add_row(["x","6","5x^3 +2 x^2 + 8x + 9 ","1161"])
myTable.add_row(["x","7","5x^3 +2 x^2 + 8x + 9 ","1808"])
myTable.add_row(["x","8","5x^3 +2 x^2 + 8x + 9 ","2665"])
myTable.add_row(["x","9","5x^3 +2 x^2 + 8x + 9 ","3762"])

print(myTable)