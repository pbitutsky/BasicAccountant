from util import erase_file, Transaction, make_tables, FILENAME, print, unadjusted_trial_balance

erase_file(FILENAME)

accounts = "Cash; Accounts Receivable; Supplies; Prepaid Insurance; Trucks; Accumulated Depreciation-Trucks; " \
           "Equipment; Accumulated Depreciation-Equipment; Accounts Payable; Unearned Roofing Fees; Common Stock; " \
           "Roofing Fees Earned; Fuel Expense; Advertising Expense; Wages Expense; Insurance Expense; Supplies " \
           "Expense; Depreciation Expense-Trucks; Depreciation Expense-Equipment".split('; ')

t = Transaction("Apr.", 1)
t.cash_asset(11500)
t.contrib_capital(11500, "Common Stock")

t = Transaction("Apr.", 1)
t.cash_asset(-2880)
t.noncash_asset(2880, "Prepaid Insurance")

t = Transaction("Apr.", 2)
t.cash_asset(-6100)
t.noncash_asset(6100, "Trucks")

t = Transaction("Apr.", 2)
t.noncash_asset(3100, "Equipment")
t.cash_asset(-1000)
t.liabilities(2100, "Accounts Payable")

t = Transaction("Apr.", 5)
t.liabilities(1200, "Accounts Payable")
t.expenses(1200, "Supplies Expense")

t = Transaction("Apr.", 5)
t.cash_asset(1800)
t.expenses(1800, "Unearned Roofing Fees")

t = Transaction("Apr.", 12)
t.noncash_asset(5500, "Accounts Receivable")
t.revenues(5500, "Roofing Fees Earned")

t = Transaction("Apr.", 18)
t.cash_asset(4900)
t.noncash_asset(-4900, "Accounts Receivable")

t = Transaction("Apr.", 29)
t.cash_asset(-675)
t.expenses(675, "Fuel Expense")

t = Transaction("Apr.", 30)
t.cash_asset(-100)
t.expenses(100, "Advertising Expense")

t = Transaction("Apr.", 30)
t.cash_asset(-2500)
t.expenses(2500, "Wages Expense")

t = Transaction("Apr.", 30)
t.noncash_asset(4000, "Accounts Receivable")
t.revenues(4000, "Roofing Fees Earned")

t.print_table()
t.print_all_journal_entries()
make_tables(accounts, t.all_transactions)

# t = Transaction()
unadjusted_trial_balance(accounts, t.all_transactions)


print("<h1>Part (D)</h1>")

# Transaction.all_transactions = []

t = Transaction("Apr.", 30)
t.contra_asset(125, "Accumulated Depreciation-Trucks")
t.expenses(125, "Depreciation Expense-Trucks")
t = Transaction("Apr.", 30)
t.contra_asset(35, "Accumulated Depreciation-Equipment")
t.expenses(35, "Depreciation Expense-Equipment")
t = Transaction("Apr.", 30)
t.expenses(1375, "Insurance Expense")
t.liabilities(1375, "Accounts Payable")
t = Transaction("Apr.", 30)
t.expenses(400, "Supplies Expense")
t.liabilities(400, "Accounts Payable")

t.print_table()
t.print_all_journal_entries()
make_tables(accounts, t.all_transactions)
