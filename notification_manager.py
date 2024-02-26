import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, from_email, from_passw, to_email, send_message) -> None:
        self.from_email = from_email
        self.emal_provider = from_email.split("@")[1]
        self.from_passw = from_passw
        self.to_email = to_email
        self.msg = send_message

    def send_notification(self):
        connection = smtplib.SMTP(f"smtp.{self.emal_provider}", port=587)
        connection.starttls()
        connection.login(user=self.from_email, password=self.from_passw)
        connection.sendmail(
            from_addr=self.from_email,
            to_addrs=self.to_email,
            msg=f"Subject: Flight deal\n\n{self.msg}"
        )
        connection.close()