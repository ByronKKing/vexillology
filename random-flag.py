##this script launches an html webpage in my browser for a random flag

import os

#create html page
os.system("jupyter nbconvert --execute flag-generator.ipynb")

#open it in browser
os.system("open flag-generator.html")



##how to put embed html into body of email, or attach to email?

# #send email
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import urllib.request

# haslo = []
# with open("/Users/byronking/Desktop/haslo.txt") as file:
#     for l in file:
#         haslo.append(l.strip())

# haslo = haslo[0]

# def sendEmail(subject,body,recipients):
#     msg = MIMEMultipart("alternative")
#     msg['From']="aspidistraflyer@yahoo.com"
#     msg['To']=recipients
#     msg['Subject']=subject
#     body = MIMEText(body,'html')
#     msg.attach(body)

#     s = smtplib.SMTP(host="smtp.mail.yahoo.com", port=587)
#     s.starttls()
#     s.login("aspidistraflyer@yahoo.com", haslo)
#     s.sendmail("aspidistraflyer@yahoo.com",recipients.split(","),msg.as_string())
#     s.quit()
#     print("Email sent successfully.")

# myhtml = urllib.request.urlopen("file:///Users/byronking/vexillology/flag-generator.html")
# mystr = myhtml.read().decode("utf8")
# myhtml.close()

# #print(mystr)

# sendEmail("Your Daily Vexillology Dose",mystr,"byronkking@gmail.com")

