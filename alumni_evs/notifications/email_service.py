from django.core.mail import EmailMessage

def send_vote_email(voter, link, qr_path):

    subject = "Christ's School 1990 Alumni Election"

    message = f"""
Dear {voter.fullname},

You are eligible to vote.

Click the link below:

{link}

Or scan the attached QR code.

Regards
Election Committee
"""

    email = EmailMessage(
        subject,
        message,
        to=[voter.email]
    )

    email.attach_file(qr_path)

    email.send()