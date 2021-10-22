class BankAccount:
  def __init__(self, full_name, account_number: float, amount: 0):
    self.name = full_name
    self.number = account_number
    self.balance = amount
  def desposit(self, amount):
    self.balance += amount
    print(f"Amount Deposited: ${amount} New Balance: ${self.balance}")
  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficicent Funds")
    else:
      self.balance -= amount
      print(f"Amount Withdrawn: ${amount} New Balance: ${self.balance}")
  def get_balance(self) -> float:
    print(f"Current Balance of Account: ${self.balance}")
    return self.balance
  def add_interest(self):
    interest = self.balance * 0.0083
    self.balance +- interest
  def print_statement(self):
    return str(f"{self.name}\nAccount Number: ****{str(self.number)[-4:]}\nBalance: ${self.balance}")

PenAccount = BankAccount("Pen", 14715215, 1093)
PenAccount.desposit(2426)
print(PenAccount.print_statement())
PenAccount.add_interest()
print(PenAccount.print_statement())
PenAccount.withdraw(285)
print(PenAccount.print_statement())

EraserAccount = BankAccount("Eraser", 53261659, 1151)
EraserAccount.desposit(209)
print(EraserAccount.print_statement())
EraserAccount.add_interest()
print(EraserAccount.print_statement())
PenAccount.withdraw(185)
print(PenAccount.print_statement())

BlockyAccount = BankAccount("Blocky", 83813628, 1420)
BlockyAccount.desposit(11229)
print(BlockyAccount.print_statement())
BlockyAccount.add_interest()
print(BlockyAccount.print_statement())
BlockyAccount.withdraw(239)
print(BlockyAccount.print_statement())

MitchellAccount = BankAccount("Mitchell", 03141592, 0)
MitchellAccount.desposit(400000)
print(MitchellAccount.print_statement())
MitchellAccount.add_interest()
print(MitchellAccount.print_statement())
MitchellAccount.withdraw(150)
print(MitchellAccount.print_statement())

  
