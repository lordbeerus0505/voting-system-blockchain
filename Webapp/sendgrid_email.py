import sendgrid

client = sendgrid.SendGridAPIClient("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")
message = sendgrid.Mail(from_email="abhiramn.cs16@rvce.edu.in",
                        to_emails="abhiram.natarajan@gmail.com",
                        subject='Sending with Twilio SendGrid is Fun',
                        html_content='OTP is <strong>kjlfa123</strong> The link to vote is: <a href="http://localhost:5000/cast_vote_overseas">http://localhost:5000/cast_vote_overseas </a>')

# message.add_to("abhiram.natarajan@gmail.com")
# message.set_from("abhiramn.cs16@rvce.edu.in")
# message.set_subject("Sending with SendGrid is Fun")
# message.set_html("and easy to do anywhere, even with Python")

response=client.send(message)
