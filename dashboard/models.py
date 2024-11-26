from django.db import models
from twilio.rest import Client
import os  # Use for environment variables

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Use environment variables for sensitive data
        account_sid = 'ACa75cdbeda4a27599e8fe3c7001875ee3'
        auth_token = '423fe8710da9a874ad8d5f7530cef6fc'
        client = Client(account_sid, auth_token)
        
        # Define message based on the score
        if self.score >= 70:
            body = f'Congratulations! {self.name}, your score is {self.score}'
        else:
            body = f'Sorry! {self.name}, your score is {self.score}. Try again.'

        # Send SMS
        try:
            message = client.messages.create(
                from_='+17755427880',  # Replace with your verified Twilio number
                body=body,
                to='+639667200116'    # Replace with the recipient's number
            )
            print(f"Message sent successfully. SID: {message.sid}")
        except Exception as e:
            print(f"Failed to send message: {e}")

        # Call the superclass save method
        super().save(*args, **kwargs)
