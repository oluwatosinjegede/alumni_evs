from django.core.mail import EmailMessage

def send_voting_email(voter, link, qr_path):

    subject = "Christ's School 1990 Alumni Election"

    message = f"""
Dear {voter.fullname},

You are eligible to vote.

Click this link to vote:

{link}

Or scan the attached QR code.

You can only vote once.
"""

    email = EmailMessage(
        subject,
        message,
        to=[voter.email]
    )

    email.attach_file(qr_path)

    email.send()