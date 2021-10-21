class BankAccount:
  def __init__(self, full_name: str, account_number: float, amount = 0):
    self.name = full_name
    self.number = account_number
    self.balance = amount
  def desposit(self):
    amount = float(input("Enter deposit amount: "))
    self.balance += amount
    print(f"Amount Deposited: ${amount} New Balance: ${self.balance}")
  def withdraw(self):
    amount = float
    if amount > self.balance:
      print("Insufficicent Funds")
      self.balance -= 10
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

PenAccount = BankAccount("Pen", "1471521", "10.93")
EraserAccount = BankAccount("Eraser", "5326165", "11.51")
BlockyAccount = BankAccount("Blocky", "8381362", "14.20")
MitchellAccount = BankAccount("Mitchell", "3141592", "400,000.00")

print(PenAccount.print_statement())
print(EraserAccount.print_statement())
print(BlockyAccount.print_statement())
print(MitchellAccount.desposit())
