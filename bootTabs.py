import clickType, time

def bootGmail():
    clickType.newTab()
    clickType.goToWebsite("https://mail.google.com/mail/u/2/#inbox")

def bootReddit():
    clickType.newTab()
    clickType.goToWebsite("reddit.com")

def bootCalCentral():
    clickType.newTab()
    clickType.goToWebsite("https://calcentral.berkeley.edu/dashboard")

def bootBcourses():
    clickType.newTab()
    clickType.goToWebsite("https://bcourses.berkeley.edu/")

clickType.newWindow()
bootGmail()
bootReddit()
bootCalCentral()
bootBcourses()