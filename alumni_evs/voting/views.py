from django.shortcuts import render
from .models import VoteToken, Vote

def vote_page(request, token):

    token_obj = VoteToken.objects.filter(
        token=token,
        used=False
    ).first()

    if not token_obj:
        return render(request,"invalid.html")

    if request.method == "POST":

        candidate = request.POST["candidate"]

        Vote.objects.create(
            voter=token_obj.voter,
            candidate=candidate
        )

        token_obj.used = True
        token_obj.save()

        return render(request,"success.html")

    return render(request,"ballot.html")

def landing_page(request):
    return render(request, "landing.html")



def latest_votes(request):

    votes = Vote.objects.select_related("voter").order_by("-created_at")[:10]

    data = []

    for v in votes:
        data.append(v.voter.fullname)

    return JsonResponse({"votes":data})
