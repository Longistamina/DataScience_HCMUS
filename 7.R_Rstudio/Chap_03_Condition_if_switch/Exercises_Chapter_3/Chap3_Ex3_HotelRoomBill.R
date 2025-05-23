options(scipen = 999) #suppress scientific notation

vip1 <- 1000000
vip2 <- 900000
vip3 <- 850000
standard1 <- 700000
standard2 <- 550000

room_type <- readline(prompt = 'Input the room type (1/2/3/4/5): ')
staying_days <- abs(as.numeric(readline(prompt = 'Input the number of staying days: ')))

unity_price <- switch(room_type,
                      "1" = vip1,
                      "2" = vip2,
                      "3" = vip3,
                      "4" = standard1,
                      "5" = standard2)

if (staying_days < 3) {
  discount <- 0
} else if (staying_days < 7) {
  discount <- 0.1
} else {
  discount <- 0.2
}

hotel_room_bill <- unity_price*staying_days*(1-discount)

cat("Roomtype: ", room_type, "\n",
    "Expense per day (VND): ", unity_price, "\n",
    "Staying days: ", staying_days, "\n",
    "Discount: ", discount, "\n",
    "===================================\n",
    "Total bill (VND) = ", unity_price," * ",staying_days," * ",(1-discount)," = ", hotel_room_bill,
    sep = "")
