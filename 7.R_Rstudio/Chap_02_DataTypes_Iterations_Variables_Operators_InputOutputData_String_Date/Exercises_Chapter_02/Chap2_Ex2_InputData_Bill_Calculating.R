food_drink <- as.numeric(readline(prompt = "Input food and drink total price ($): "))
tax_rate <- as.numeric(readline(prompt = "Input tax rate (10-20%): ")) / 100
tip_rate <- as.numeric(readline(prompt = "Input tip rate (5-10%): ")) / 100


cat("Total food and drink original price ($): ", food_drink, "\n",
    "Tax ($): ", food_drink*tax_rate, "\n",
    "Tip ($): ", food_drink*tip_rate, "\n",
    "====================================", "\n",
    "Final Bill (original + tax + tip): ", food_drink*(1+tax_rate+tip_rate), 
    sep = "")
