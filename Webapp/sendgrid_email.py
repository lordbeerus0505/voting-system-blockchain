import sendgrid
class Email:
    def send(self,address,path="http://localhost:5000/cast_vote_overseas"):
        client = sendgrid.SendGridAPIClient("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")
        message = sendgrid.Mail(from_email="abhiramn.cs16@rvce.edu.in",
                                to_emails=address,
                                subject='Indian Elections 2019, OTP + URL',
                                html_content='OTP is <strong>kjlfa123</strong> The link to vote is: <a href=\"'+path+'\">Click here</a>')

        # message.add_to("abhiram.natarajan@gmail.com")
        # message.set_from("abhiramn.cs16@rvce.edu.in")
        # message.set_subject("Sending with SendGrid is Fun")
        # message.set_html("and easy to do anywhere, even with Python")
        # import pdb; pdb.set_trace()
        response=client.send(message)
# obj=Email()
# obj.send("abhiram.natarajan@gmail.com")