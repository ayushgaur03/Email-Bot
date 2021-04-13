import smtplib
import speech_recognition as sr
import pyttsx3 as speak
from email.message import EmailMessage
from color import colors


listener = sr.Recognizer()
engine = speak.init()

def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print(f"{colors.fg.yellow}listening....{colors.reset}")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_mail(receiver, subject, msg_body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('managingdirector1975@gmail.com', 'Director_1975')
    email = EmailMessage()
    email["From"] = "managingdirector1975@gmail.com"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(msg_body)
    server.send_message(email)


email_list = {
    # This object is like the email diectory, i.e., EmailBot will use the shortnames to refer to email addresses.
    "ayush": "ayushgaur02@gmail.com",
}


def get_email_info():
    talk("To whom you want to send the email")
    name = get_info()
    receiver = email_list[name]
    talk("What is the subject of your email?")
    subject = get_info()
    talk("What is the message?")
    msg_body = get_info()
    prGreen("Your mail has been sent successfuly!")
    print(f"{colors.fg.green}Success:Your mail has been sent successfully!!{colors.reset}")
    talk("Sent Sir!")
    send_mail(receiver, subject, msg_body)


get_email_info()
