from django.shortcuts import render

from django.http import JsonResponse


# Create your views here.
def add_to_gallery(request):
    if request.POST:
        if request.user.is_authenticated:
            pass

    return JsonResponse(
        {"error": "You must be logged in to add to gallery."}, status=403
    )
