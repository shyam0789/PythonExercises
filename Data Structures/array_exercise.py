expense_list = [2200,2350,2600,2130,2000]
# 1. In Feb, how many dollars you spent extra compare to January?
addnl_amt = expense_list[1]-expense_list[0]
print(f"Addnl. Amt spent in Feb is ${addnl_amt}")
# 2. Find out your total expense in first quarter (first three months) of the year.
quarter_result = sum(expense_list[0:2])
print(f"Quarterly Result: ${quarter_result}")
# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spend $2000 in any month ? ", 2000 in expense_list)
for i in expense_list:
    if i == 2000:
        print(f"You have spent $2000 in the index [{expense_list.index(2000)}]")
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense_list.append(1980)
print(expense_list)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
refund = expense_list[3]-200
expense_list[3] = refund
print(f"Amount Spent on April: ${expense_list[3]}")
