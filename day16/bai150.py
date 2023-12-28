from prettytable import PrettyTable

table = PrettyTable()
print (table.align)
table.align = "l"
print (table.align)
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

# table.field_names = ["Ho và Ten","MSSV","SDT","GioiTinh"]
# table.add_row(["Nguyen Quoc Viet","B2111908","012","Nam"])
# table.add_row(["Truong Huynh Tu Nhu","B2111893","012","Nu"])
# table.add_row(["Nguyen Quoc Viet","B2111908","012","Nam"])
print(table)

