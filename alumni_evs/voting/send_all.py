from voters.models import Voter
from .qr_service import generate_qr_for_voter
from alumni_evs.notifications.email_service import send_vote_email

def send_all_voting_links(election):

    voters = Voter.objects.all()

    for voter in voters:

        link, qr = generate_qr_for_voter(voter,election)

        send_vote_email(voter,link,qr)