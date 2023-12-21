from django.shortcuts import render, redirect
import requests


def index(request):
    response_tracks = requests.get("http://127.0.0.1:8000/api/tracks")
    if response_tracks.status_code == 200:
        tracks = response_tracks.json()
    else:
        tracks = None

    if request.method == "POST":
        if request.POST.get("addtrack") == "trackadd":
            print("Burada")
            title = request.POST.get("title")
            artist = request.POST.get("artist")
            duration = request.POST.get("duration")
            last_play = request.POST.get("last_play")

            track = {
                "title":title,
                "artist":artist,
                "duration":duration,
                "last_play":last_play
            }

            new_track = requests.post("http://127.0.0.1:8000/api/tracks",json=track)
            return redirect("index")
        
        if request.POST.get("updatetrack") == "trackupdate":
            track_id = request.POST.get("track_id")
            title = request.POST.get("title")
            artist = request.POST.get("artist")
            duration = request.POST.get("duration")
            last_play = request.POST.get("last_play")
    
            track = {
                "id":track_id,
                "title":title,
                "artist":artist,
                "duration":duration,
                "last_play":last_play
            }

            update_track = requests.put(f"http://127.0.0.1:8000/api/tracks/{track_id}",json=track)
            return redirect("index")

    if "trackid" in request.GET and request.GET["trackid"] != "":   
        track_id = request.GET["trackid"]
        delete_track = requests.delete(f"http://127.0.0.1:8000/api/tracks/{track_id}")
        return redirect("index")
    
    context={
            "tracks":tracks
        }
    return render(request=request, template_name="index.html",context=context)
