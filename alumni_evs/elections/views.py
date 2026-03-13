
from alumni_evs.voting.models import Vote
from alumni_evs.voters.models import Voter

def dashboard(request):

    total_voters = Voter.objects.count()

    votes_cast = Vote.objects.count()

    turnout = round((votes_cast / total_voters) * 100,2)

    return render(request,"admin/dashboard.html",{
        "total_voters":total_voters,
        "votes_cast":votes_cast,
        "turnout":turnout
    })