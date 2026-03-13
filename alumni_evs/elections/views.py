from django.shortcuts import render
from voters.models import Voter
from voting.models import Vote
from django.http import JsonResponse

def dashboard(request):

    total_voters = Voter.objects.count()

    votes_cast = Vote.objects.count()

    turnout = 0

    if total_voters > 0:
        turnout = round((votes_cast / total_voters) * 100,2)

    latest_votes = Vote.objects.select_related("voter").order_by("-created_at")[:10]

    context = {
        "total_voters": total_voters,
        "votes_cast": votes_cast,
        "turnout": turnout,
        "latest_votes": latest_votes
    }

    return render(request,"admin/dashboard.html",context)




def dashboard_stats(request):

    total = Voter.objects.count()

    votes = Vote.objects.count()

    turnout = (votes/total)*100 if total else 0

    return JsonResponse({
        "total": total,
        "votes": votes,
        "turnout": round(turnout,2)
    })