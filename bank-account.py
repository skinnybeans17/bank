class BankAccount:
  def __init__(self, full_name: str, account_number: int, balance = 0) -> None:
    self.name = full_name
    self.number = account_number
    self.amount = balance
  def desposit(self, amount: float) -> None:
    self.amount += amount
    print(f"Amount Deposited: ${amount} New Balance: ${self.balance}")
  def withdraw(self, amount: float) -> None:
    if amount > self.amount:
      print("Insufficicent Funds")
      self.amount -= 10
    else:
      self.amount -= amount
      print(f"Amount Withdrawn: ${amount} New Balance: ${self.amount}")
  def get_balance(self) -> float:
    print(f"Current Balance of Account: ${self.amount}")
    return self.amount
  def add_interest(self) -> None:
    interest = self.amount * 0.0083
    self.amount +- interest
  def print_statement(self) -> None:
    return str(f"{self.name}\nAccount Number: ****{str(self.number)[-4:]}\nBalance: ${self.amount}")

PenAccount = BankAccount("Pen", "1471521", "10.93")
EraserAccount = BankAccount("Eraser", "5326165", "11.51")
BlockyAccount = BankAccount("Blocky", "8381362", "14.20")

print(PenAccount.print_statement())
print(EraserAccount.print_statement())
print(BlockyAccount.print_statement())
