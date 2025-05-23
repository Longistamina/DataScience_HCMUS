deposit <- as.numeric(readline(prompt = "Input deposit money ($): "))
annual_interest_rate <- as.numeric(readline(prompt = "Input annual interest rate (%): "))
days_of_deposit <- as.numeric(readline(prompt = "Input number of deposit days: "))

daily_interest_rate <- annual_interest_rate / 365
interest <- (deposit * days_of_deposit) * (daily_interest_rate/100)

cat("Deposit money ($): ", deposit, "\n",
    "Number of deposit days: ", days_of_deposit, "\n",
    "Daily interest rate (%): ", daily_interest_rate,"%", "\n",
    "====================================", "\n",
    "Interest money: ", interest, "\n", 
    "Total money (deposit + interest): ", deposit+interest, 
    sep = "")