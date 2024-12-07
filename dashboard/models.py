from django.db import models
# from twilio.rest import Client  # Uncomment this if you intend to use Twilio

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Temporarily commenting out sensitive data and SMS sending logic
        # Uncomment and use environment variables for sensitive information
        account_sid = "ACa75cdbeda4a27599e8fe3c7001875ee3"
        auth_token = "e39280b050e5e037f372b29f0f6a1433"
        
        # Validate Twilio client initialization only if needed
        try:
            from twilio.rest import Client
            client = Client(account_sid, auth_token)
        except ImportError:
            client = None
            print("Twilio library is not installed. Skipping SMS logic.")

        if self.score >= 70:
            body = f"Congratulations! {self.name}, your score is {self.score}"
        else:
            body = f"Sorry! {self.name}, your score is {self.score}. Try again."
        
        # Example of logging instead of sending SMS
        print(f"Mock SMS: {body}")
        
        if client:  # Only try to send SMS if Twilio client is initialized
            try:
                message = client.messages.create(
                    from_="+17755427880",
                    body=body,
                    to="+639667200116"
                )
                print(f"Message SID: {message.sid}")
            except Exception as e:
                print(f"Failed to send SMS: {e}")

        super().save(*args, **kwargs)
