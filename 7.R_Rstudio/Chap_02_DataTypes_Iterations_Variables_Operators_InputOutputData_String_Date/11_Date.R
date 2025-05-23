# date() to take the current date time data of the system (computer)
print(date())

print(Sys.Date())


# as.Date("date_string", format(....)) to convert a date_string with particular format into Date data
print(as.Date("20/10/2025", format("%d/%m/%Y")))

print(class(as.Date("20/10/2025", format("%d/%m/%Y"))))

## %d: day of month as number, [01-31]

## %a: abbreviated weekday, [Mon, Tue, ...]
## %A: long-form weekday, [Monday, Tuesday, ...]

## %m: month as number, [01-12]
## %b: month as abbreviated string, [Jan, Feb, ...]
## %B: month as long-form string, [January, February, ...]

## %Y: 4-digit year, [1998, 1999, ..., 2018, 2019, 2020, ...]
## %y: 2-digit year, [  98,   99, ...,   18,   19,   20, ...]

# format() to define a specific format to display the data
print(format(Sys.Date(), format = "%B %d %Y"))
print(format(Sys.Date(), format = "%b %d %y"))


# Calculate time distance
distance <- Sys.Date() - as.Date("2025-04-30")
print(distance)
print(as.numeric(distance)) #To return a numeric output only

# difftime() to calculate time distance with different types of unit
# units = c("auto", "secs", "mins", "hours", "days", "weeks")
diff_time <- difftime(Sys.Date(), as.Date("2023-03-25"), units = 'weeks')
print(diff_time)
print(as.numeric(diff_time))

diff_time <- difftime(Sys.Date(), as.Date("2023-03-25"), units = 'days')
print(diff_time)
print(as.numeric(diff_time))

