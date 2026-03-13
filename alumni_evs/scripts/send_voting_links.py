from voters.models import Voter
from voting.qr_service import generate_qr
from notifications.email_service import send_voting_email

def run():

    voters = Voter.objects.all()

    for voter in voters:

        link, qr = generate_qr(voter)

        send_voting_email(voter, link, qr)