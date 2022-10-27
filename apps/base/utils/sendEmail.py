from django.core.mail import EmailMessage


def sendEmail(subject, message, email):
    email = EmailMessage(subject, message, to=[email])
    email.send()
    return email
