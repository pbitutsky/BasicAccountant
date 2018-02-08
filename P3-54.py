from util import erase_file, Transaction, make_tables, FILENAME, print, unadjusted_trial_balance

erase_file(FILENAME)

accounts = "Cash; Accounts Receivable; Supplies; Prepaid Insurance; Trucks; Accumulated Depreciation-Trucks; " \
           "Equipment; Accumulated Depreciation-Equipment; Accounts Payable; Unearned Roofing Fees; Common Stock; " \
           "Roofing Fees Earned; Fuel Expense; Advertising Expense; Wages Expense; Insurance Expense; Supplies " \
           "Expense; Depreciation Expense-Trucks; Depreciation Expense-Equipment".split('; ')

t = Transaction("Dec.", 1)
t.cash_asset(20000)
t.contrib_capital(20000, "Common Stock")

t = Transaction("Dec.", 2)
t.cash_asset(-1200)
t.expenses(1200, "Rent Expense")

t = Transaction("Dec.", 2)
t.liabilities(1080, "Accounts Payable")
t.noncash_asset(1080, "Supplies")

t = Transaction("Dec.", 3)
t.cash_asset(-4700)
t.liabilities(4800, "Accounts Payable")
t.noncash_asset(9500, "Office Equipment")

t = Transaction("Dec.", 8)
t.cash_asset(-1080)
t.liabilities(-1080, "Accounts Payable")

t = Transaction("Dec.", 14)
t.expenses(900, "Wages Expense")
t.cash_asset(-900)

t = Transaction("Dec.", 20)
t.cash_asset(3000)
t.revenues(3000, "Consulting Revenue")

t = Transaction("Dec.", 28)
t.cash_asset(-900)
t.expenses(900, "Wages Expense")

t = Transaction("Dec.", 30)
t.noncash_asset(7200, "Fees Receivable")
t.revenues(7200, "Consulting Revenue")

t = Transaction("Dec.", 31)
t.cash_asset(-1800)
t.earned_capital(-1800, "Retained Earnings")

t = Transaction("Dec.", 31)
t.noncash_asset(-370, "Supplies")
t.expenses(370, "Supplies Expense")

t = Transaction("Dec.", 31)
t.liabilities(270, "Wages Payable")
t.expenses(270, "Wages Expense")

t = Transaction("Dec.", 31)
t.contra_asset(120, "Accumulated Depreciation")
t.expenses(120, "Depreciation Expense")

t = Transaction("Dec.", 31)
t.noncash_asset(2250, "Fees Receivable")
t.revenues(2250, "Consulting Revenue")

accounts = []
for t in Transaction.all_transactions:
    for col in Transaction.columns:
        if col in t.row and t.row[col][1] not in accounts:
            accounts.append(t.row[col][1])

t.print_table()
t.print_all_journal_entries()
make_tables(accounts, t.all_transactions)

# t = Transaction()
unadjusted_trial_balance(accounts, t.all_transactions)







