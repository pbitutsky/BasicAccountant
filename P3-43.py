from util import erase_file, Transaction, make_tables, FILENAME, print, unadjusted_trial_balance

erase_file(FILENAME)

# accounts = "Cash; Accounts Receivable; Supplies; Prepaid Insurance; Trucks; Accumulated Depreciation-Trucks; " \
#            "Equipment; Accumulated Depreciation-Equipment; Accounts Payable; Unearned Roofing Fees; Common Stock; " \
#            "Roofing Fees Earned; Fuel Expense; Advertising Expense; Wages Expense; Insurance Expense; Supplies " \
#            "Expense; Depreciation Expense-Trucks; Depreciation Expense-Equipment".split('; ')

t = Transaction("Dec.", 31)
t.expenses(1800, "Wages Expense")
t.liabilities(1800, "Accounts Payable")

t = Transaction("Dec.", 31)
t.noncash_asset(200, "Interest Expense")
t.liabilities(200, "Interest Payable")

t = Transaction("Dec.", 31)
t.noncash_asset(900, "Fees Receivable")
t.revenues(900, "Printing Revenues")

t = Transaction("Dec.", 31)
t.liabilities(2400, "Prepaid Maintenance")
t.noncash_asset(2400, "Equipment Maintenance")

t = Transaction("Dec.", 31)
t.expenses(900, "Prepaid Advertising")
t.cash_asset(-900, "Cash")

t = Transaction("Dec.", 31)
t.expenses(0.80*400*1.5, "Rent Expense")
t.liabilities(0.80*400*1.5, "Accounts Payable")

t = Transaction("Dec.", 31)
t.noncash_asset(38, "Interest Receivable")
t.revenues(38, "Interest Income")

t = Transaction("Dec.", 31)
t.contra_asset(2175, "Accumulated Depreciation-Equipment")
t.expenses(2175, "Depreciation Expense-Equipment")


t.print_table()
t.print_all_journal_entries()
# make_tables(accounts, t.all_transactions)
