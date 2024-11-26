from django.db import models
# from twilio.rest import Client  # Commenting Twilio library temporarily

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Temporarily commenting out sensitive data and SMS sending logic
        # account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        # auth_token = "your_auth_token"
        # client = Client(account_sid, auth_token)

        if self.score >= 70:
            body = f"Congratulations! {self.name}, your score is {self.score}"
        else:
            body = f"Sorry! {self.name}, your score is {self.score}. Try again."
        
        # Example of logging instead of sending SMS
        print(f"Mock SMS: {body}")
        
        # Commented out Twilio SMS code
        # message = client.messages.create(
        #     from_="+17755427880",
        #     body=body,
        #     to="+639667200116"
        # )
        # print(f"Message SID: {message.sid}")

        super().save(*args, **kwargs)
