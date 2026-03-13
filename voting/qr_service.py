import qrcode
from .models import VoteToken

BASE_URL = "https://90set2026election.up.railway.app"

def generate_qr(voter):

    token_obj = VoteToken.objects.create(voter=voter)

    vote_url = f"{BASE_URL}/vote/{token_obj.token}"

    qr = qrcode.make(vote_url)

    filename = f"media/qr/{token_obj.token}.png"

    qr.save(filename)

    return vote_url, filename