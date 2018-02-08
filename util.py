
FILENAME = "hw03.html"

print1 = print
def erase_file(filename):
    open(filename, 'w').close()

def print(*args):
    with open(FILENAME, "a") as myfile:
        myfile.write(' '.join([str(x) for x in args]) + '\n')


def currency_format(n):
    return '${:,.2f}'.format(n)

class T_table:

    all_tables = []
    def __init__(self, title):
        self.title = title
        self.debits = []
        self.credits = []
        T_table.all_tables.append(self)

    def total_debits(self):
        return sum(x[1] for x in self.debits)

    def total_credits(self):
        return sum(x[1] for x in self.credits)

    def total(self):
        return self.total_debits() - self.total_credits()

    def add_debit(self, transaction, amount):
        self.debits.append((transaction, amount))

    def add_credit(self, transaction, amount):
        self.credits.append((transaction, amount))

    def render_table(self):
        print("<table border='0' style='width:400px'>")
        print("<th style='background-color:lightgray; border-bottom: 2px solid black;'>" + self.title + "</th>")
        print("<tr>")
        print("<td>")

        print("<table border='0' style='width:100%; border-collapse: collapse'>")

        i = 0

        while i < len(self.debits) or i < len(self.credits):
            a, b, c, d = None, None, None, None
            if i < len(self.debits):
                a, b = self.debits[i][0], self.debits[i][1]
            if i < len(self.credits):
                c, d = self.credits[i][1], self.credits[i][0]
            print("<tr>")
            print("<td style='width:25%'>")
            if a:
                print('(' + str(a) + ')')
            print("</td>")
            print("<td style='width:25%; text-align:right; border-right:1px solid black'>")
            if b:
                print(currency_format(b))
            print("</td>")
            print("<td style='width:25%'>")
            if c:
                print(currency_format(c))
            print("</td>")
            print("<td style='width:25%; text-align: right'>")
            if d:
                print('(' + str(d) + ')')
            print("</td>")
            print("</tr>")
            i += 1

        total = self.total()
        print("<tr style='border-top:1px solid black'>")
        print("<td style='width:25%'>")
        print("</td>")
        print("<td style='width:25%; text-align:right; border-right:1px solid black'>")
        if total > 0:
            print("<b>" + currency_format(total) + "</b>")
        print("</td>")
        print("<td style='width:25%'>")
        if total < 0:
            print("<b>" + currency_format(total) + "</b>")
        print("</td>")
        print("<td style='width:25%; text-align: right'>")
        print("</td>")
        print("</tr>")
        print("</table>")
        print("</td>")
        print("</tr>")
        print("</table>")

class Transaction:

    all_transactions = []
    columns = ["Cash Asset", "Noncash Asset", "Contra Assets", "Liabilities", "Contrib. Capital", "Earned Capital", "Revenues", "Expenses", "Net Income"]

    # def __init__(self, month, day, amt, asset_account, asset_col, liability_account, liability_col):
    def __init__(self, month, day):
        self.month = month
        self.day = day
        self.row = {}
        self.debits = []
        self.credits = []
        self.transaction_id = len(Transaction.all_transactions)+1
        Transaction.all_transactions.append(self)
        # self.asset_account = asset_account
        # self.asset_col = {1: "Cash Asset", 2: "Noncash Asset"}[asset_col]
        # self.amt = amt
        # self.liability_account = liability_account
        # self.liability_col = {1: "Liabilities", 2: "Contrib. Capital", 3: "Earned Capital", 4: "Revenues", 5: "Expenses"}[liability_col]

    def debit_or_credit(self, cond, amt, acct): #if cond is true, debit, else credit
        amt = abs(amt)
        if cond:
            self.debits.append((amt, acct))
        else:
            self.credits.append((amt, acct))
    def cash_asset(self, amt, acct="Cash"):
        self.row["Cash Asset"] = (amt, acct)
        self.debit_or_credit(amt > 0, amt, acct)

    def noncash_asset(self, amt, acct):
        self.row["Noncash Asset"] = (amt, acct)
        self.debit_or_credit(amt > 0, amt, acct)

    def contra_asset(self, amt, acct):
        self.row["Contra Assets"] = (amt, acct)
        self.debit_or_credit(amt < 0, amt, acct)

    def liabilities(self, amt, acct):
        self.row["Liabilities"] = (amt, acct)
        self.debit_or_credit(amt < 0, amt, acct)

    def contrib_capital(self, amt, acct):
        self.row["Contrib. Capital"] = (amt, acct)
        self.debit_or_credit(amt < 0, amt, acct)

    def earned_capital(self, amt, acct):
        self.row["Earned Capital"] = (amt, acct)
        self.debit_or_credit(amt < 0, amt, acct)

    def revenues(self, amt, acct):
        self.row["Revenues"] = (amt, acct)
        self.row["Net Income"] = (amt, "")
        self.row["Earned Capital"] = (amt, "Retained Earnings")
        self.debit_or_credit(amt < 0, amt, acct)

    def expenses(self, amt, acct):
        self.row["Expenses"] = (amt, acct)
        self.row["Net Income"] = (-amt, "")
        self.row["Earned Capital"] = (-amt, "Retained Earnings")
        self.debit_or_credit(amt > 0, amt, acct)

    def print_journal_entry(self):
        print("<table>")
        i = 0
        dots = ''.join(['.' for x in range(0, 1000)])
        for debit in self.debits:
            print("<tr>")
            print("<td>")
            if i == 0:
                print(self.month, self.day)
            print("</td>")
            print("<td style='max-width:300px; overflow:hidden; white-space: nowrap''>")
            print(debit[1]+dots)
            print("</td>")
            print("<td>")
            print(currency_format(debit[0]))
            print("</td>")
            print("<td>")
            print("</td>")
            print("</tr>")
            i += 1

        for credit in self.credits:
            print("<tr>")
            print("<td>")
            print("</td>")
            print("<td style='max-width:300px; overflow:hidden; white-space: nowrap; padding-left:30px;'>")
            print(credit[1]+dots)
            print("</td>")
            print("<td>")
            print("</td>")
            print("<td>")
            print(currency_format(credit[0]))
            print("</td>")
            print("</tr>")
        print("</table>")

    def print_all_journal_entries(self):
        for t in Transaction.all_transactions:
            t.print_journal_entry()

    def print_table_row(self):
        print("<tr>")
        for col in Transaction.columns:
            print("<td style='border:1px solid black'>")
            if col in self.row:
                cell_value_tup = self.row[col]
                print(currency_format(cell_value_tup[0]) + "<br/>" + cell_value_tup[1])
            print("</td>")
        print("</tr>")

    def print_table(self):
        print("<table style='border-collapse:collapse; text-align:center'>")
        print("<tr>")
        for header in Transaction.columns:
            print("<th style='border:1px solid black; background-color:lightgray'>")
            print(header)
            print("</th>")
        print("</tr>")
        for transaction in Transaction.all_transactions:
            transaction.print_table_row()
        print("</table>")


def make_tables(accounts, transactions):
    # Create the tables
    tables = {}
    for account in accounts:
        tables[account] = T_table(account)

    # bulk import transactions into them
    for transaction in transactions:
        for d in transaction.debits:
            amt, acct, trans_id = d[0], d[1], transaction.transaction_id
            for table in tables:
                if tables[table].title == acct:
                    tables[table].add_debit(trans_id, amt)
        for c in transaction.credits:
            amt, acct, trans_id = c[0], c[1], transaction.transaction_id
            for table in tables:
                if tables[table].title == acct:
                    tables[table].add_credit(trans_id, amt)

    # render/display them
    for table in tables:
        tables[table].render_table()

def unadjusted_trial_balance(accounts, transactions):
    # Create the tables
    tables = {}
    for account in accounts:
        tables[account] = T_table(account)

    # bulk import transactions into them
    for transaction in transactions:
        for d in transaction.debits:
            amt, acct, trans_id = d[0], d[1], transaction.transaction_id
            for table in tables:
                if tables[table].title == acct:
                    tables[table].add_debit(trans_id, amt)
        for c in transaction.credits:
            amt, acct, trans_id = c[0], c[1], transaction.transaction_id
            for table in tables:
                if tables[table].title == acct:
                    tables[table].add_credit(trans_id, amt)

    print("<table style='border-collapse:collapse; border: 1px solid black'>")
    print("<tr><th></th><th>Debit</th><th>Credit</th></tr>")
    total_debit = 0
    total_credit = 0
    for table in tables:
        balance = tables[table].total()
        print("<tr>")
        print("<td style='border: 1px solid black'>" + table + "</td>")
        print("<td style='border: 1px solid black'>")
        if balance >= 0:
            total_debit += balance
            print(currency_format(balance))
        print("</td>")
        print("<td style='border: 1px solid black'>")
        if balance < 0:
            total_credit -= balance
            print(currency_format(-balance))
        print("</td>")
        print("</tr>")
    print("<tr><th style='border: 1px solid black'>Total</th><th style='border: 1px solid black'>" + currency_format(total_debit) + "</th>")
    print("<th style='border: 1px solid black'>"+currency_format(total_credit)+"</th></tr>")
    print("</table>")


