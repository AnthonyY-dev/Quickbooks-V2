from replit import db
from simple_chalk import chalk
import datetime
from datetime import datetime as dt
import os

# print(chalk.red.bold('This version is now decapricated. Use the new one at antsite.xyz, Sorry :('))

clearCommand = "clear"
os.system(clearCommand)


def reset():
  db["log"] = []
  db["moneyPayed"] = 0


def sort_key(sub_arr):
  return dt.strptime(sub_arr[0], '%m/%d/%Y')


def isfloat(num):
  try:
    float(num)
    return True
  except ValueError:
    return False


def main():
  choise = ""
  while True:
    print(
      chalk.green(
        "1. View debit log | 2. Add item to log | 3. Add payed money | 4. View owed money | 5. Edit log item | 6. View price list"
      ))
    choise = input(chalk.red.bold(">"))
    if choise in ["1", "2", "3", "4", "5", "6", "RESET_ALL"]:
      break
    os.system(clearCommand)
    print(chalk.red("Invalid option"))

  if choise == "1":
    os.system(clearCommand)
    if not db["log"] == []:
      nonSortedArray = db["log"][::1]
      sorted_arr = sorted(nonSortedArray, key=sort_key)
      totalPrice = 0
      for index, item in enumerate(sorted_arr, start=1):
        price = str(item[2])
        price = chalk.green("$" + price)
        print(f"{index}. {item[0]} | '{item[1]}' | {price}")
        totalPrice += int(item[2])
      print("Total: " + chalk.green("$" + str(totalPrice)))
    else:

      os.system(clearCommand)
      print("The log is empty, check back later!")
  if choise == "2":
    os.system(clearCommand)
    name = input(chalk.blue.bold("Enter the name / reason\n") + chalk.red(">"))
    name.capitalize()
    os.system(clearCommand)
    price = None
    while True:
      price = input(chalk.blue.bold("Enter the price\n") + chalk.red(">"))
      if isfloat(price):
        break
      os.system(clearCommand)
      print(chalk.red("Invalid price, price has to be numeric."))
    price = float(price)
    db["log"].append(
      [datetime.datetime.now().strftime("%m/%d/%Y"), name, price])
    os.system(clearCommand)
  if choise == "3":
    moneyAdded = None
    while True:
      moneyAdded = input(
        chalk.blue.bold("Enter the money that has been payed\n") +
        chalk.red(">"))
      if isfloat(moneyAdded):
        break
      os.system(clearCommand)
      print(chalk.red("Invalid number, number has to be numeric."))
    db["moneyPayed"] += float(moneyAdded)
  if choise == "4":
    fullMoneyOwed = 0
    for item in db["log"]:
      fullMoneyOwed += item[2]
    os.system(clearCommand)
    print("$" + str(fullMoneyOwed - db["moneyPayed"]))
  if choise == "5":
    os.system(clearCommand)
    log = db["log"][::1]
    logLen = len(log)
    entryId = None
    while True:
      entryId = input("Enter the log entry to edit\n" + chalk.red.bold(">"))
      if entryId.isnumeric():
        entryId = int(entryId)
        if (not entryId > logLen):
          if entryId > 0:
            break
          else:
            os.system(clearCommand)
            print("Number is out of log range.")
        else:
          os.system(clearCommand)
          print("Number is out of log range.")
      else:
        os.system(clearCommand)
        print("That is not a valid number!")
    optionEntry = ""
    entryId -= 1
    os.system(clearCommand)
    while True:

      print("1. Date | 2. Name | 3. Price")
      optionEntry = input(chalk.red.bold(">"))
      os.system(clearCommand)
      if optionEntry in ["1", "2", "3"]:
        break
    if optionEntry == "1":
      log[entryId][0] = input("Enter the date. Example: 04/14/2011\n" +
                              chalk.red(">"))
    if optionEntry == "2":
      log[entryId][1] = input("Enter the name.\n" + chalk.red(">"))
    if optionEntry == "3":
      while True:
        log[entryId][2] = input("Enter the price.\n" + chalk.red(">"))
        if isfloat(log[entryId][2]):
          log[entryId][2] = float(log[entryId][2])
          break
        else:
          os.system('clear')
          print(chalk.red("Invalid price!"))
    db["log"] = log[::1]
    os.system(clearCommand)
    print(chalk.green("Success!"))
  if choise == "RESET_ALL":
    os.system(clearCommand)
    print(
      chalk.red.bold(
        "ARE YOU SURE YOU WANT TO DO THIS? ENTER YES TO CONFIRM, ANYTHING ELSE TO CANCEL. YOU CANNOT UNDO THIS"
      ))
    if input().lower() == "yes":
      reset()
      os.system(clearCommand)
      print(chalk.red.bold("Everything has been reset successfully."))
    else:
      os.system(clearCommand)
      print(chalk.green("Canceled."))
  main()


if __name__ == "__main__":
  while True:
    if input(chalk.red("Enter the password\n>")) == os.environ["PASS"]:
      os.system(clearCommand)
      main()
      break
    else:
      os.system(clearCommand)
      print(chalk.red("Incorrect password."))
