# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("System Online")

from django.shortcuts import render

def home(request):
    # All images
    images = ["1","2","3","4","5","6","7","8","9","10","11","13","14","15","16","17","18","20","21","22","23","24","25","27"]
    # Videos
    videos = ["12","19","26","28","29","30"]

    # Combine images + videos into one list for rotation
    media_items = []

    for img in images:
        media_items.append({
            "type": "image",
            "src": img
        })
    for vid in videos:
        media_items.append({
            "type": "video",
            "src": vid
        })

    total = len(media_items)
    for idx, item in enumerate(media_items):
        angle = (360 / total) * idx
        item["angle"] = angle  # precompute rotation angle for CSS

    context = {
        "media_items": media_items
    }

    return render(request, 'core/home.html', context)
