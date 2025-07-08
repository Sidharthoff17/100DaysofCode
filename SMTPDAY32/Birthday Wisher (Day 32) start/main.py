import smtplib
import random
import datetime as dt

my_email = "sidharthrofficial1704@gmail.com"
password = "dvlaiurwepslqxgz"

#open quotes.txt
with open("quotes.txt", "r") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)



now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    #open connection
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= "sid.ssrao@gmail.com",
            msg = f"Subject: Motivational quotes\n\n {quote}"
        )
