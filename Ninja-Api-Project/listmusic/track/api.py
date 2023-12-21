from django.http import JsonResponse
from ninja import NinjaAPI, ModelSchema, Schema
from typing import List, Optional
from .models import *

api = NinjaAPI()

class TrackSchema(ModelSchema):
    class Meta:
        model = Track
        fields = "__all__"

class NotFoundSchema(Schema):
    message : str


@api.get("/all-tracks", response=List[TrackSchema])
def tracks(request,title=None):
    if title:
        return Track.objects.filter(title__icontains=title)
    else:
        return Track.objects.all()


@api.get("/get-tracks/{track_id}",response={200:TrackSchema,404:NotFoundSchema})
def track(request,track_id:int):
    try:
        track = Track.objects.get(id=track_id)
        return track
    except Track.DoesNotExist:
        return 404, {"message":"Şarkı Bulunamadı."}


@api.post("/add-tracks", response={201:TrackSchema})
def create_track(request,track:TrackSchema):
    track = Track.objects.create(**track.dict())
    return track

@api.put("/update-tracks/{track_id}", response={200:TrackSchema,404:NotFoundSchema})
def update_track(request,track_id:int,data:TrackSchema):
    print("data",data)
    try:
        track = Track.objects.get(id=track_id)
        for attr,value in data.dict().items():
            setattr(track,attr,value)
        track.save()
        return 200, track
    except Track.DoesNotExist:
        return 404, {"message":"Şarkı Bulunamadı."}

@api.delete("/delete-tracks/{track_id}",response={404:NotFoundSchema})
def delete_track(request,track_id:int):
    try:
        track = Track.objects.get(id=track_id)
        track.delete()
        return JsonResponse({"success":True})
    except Track.DoesNotExist:
        return 404, {"message":"Şarkı Bulunamadı."}