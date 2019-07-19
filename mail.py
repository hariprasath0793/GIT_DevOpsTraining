import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('programmingtesting12@gmail.com ', 'Testmyprogram@12')
smtpObj.sendmail('programmingtesting12@gmail.com ', 'hariprasath0793@gmail.com','Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely,Bob')
