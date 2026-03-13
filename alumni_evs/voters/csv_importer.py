import pandas as pd
from .models import Voter

def import_voters(csv_file):

    df = pd.read_csv(csv_file)

    voters = []

    for _, row in df.iterrows():
        voter = Voter(
            fullname=row["fullname"],
            email=row["email"],
            phone=row["phone"],
            alumni_id=row["alumni_id"]
        )
        voters.append(voter)

    Voter.objects.bulk_create(voters)

    return len(voters)