sum = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))
for x in expenses:
    sum = sum + x

print('You spent $', sum, sep = '')
