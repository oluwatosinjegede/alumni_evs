from django.http import JsonResponse

def turnout_api(request):

    total = Voter.objects.count()
    votes = Vote.objects.count()

    turnout = (votes/total)*100 if total else 0

    return JsonResponse({
        "votes":votes,
        "total":total,
        "turnout":turnout
    })