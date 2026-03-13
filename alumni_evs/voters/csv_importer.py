import pandas as pd
from .models import Voter

def import_voters(file):

    df = pd.read_csv(file)

    for _,row in df.iterrows():

        Voter.objects.create(
            fullname=row['fullname'],
            email=row['email'],
            phone=row['phone'],
            alumni_id=row['alumni_id']
        )