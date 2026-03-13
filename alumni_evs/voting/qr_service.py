import qrcode
from .models import VoteToken

BASE_URL = "https://90set2026election.up.railway.app/"

def generate_qr_for_voter(voter,election):

    token = VoteToken.objects.create(
        voter=voter,
        election=election
    )

    url = f"{BASE_URL}/vote/{token.token}"

    img = qrcode.make(url)

    file_path = f"media/qr/{token.token}.png"

    img.save(file_path)

    return url, file_path