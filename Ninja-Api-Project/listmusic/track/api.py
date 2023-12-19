from ninja import NinjaAPI, ModelSchema, Schema
from typing import List
from .models import *

api = NinjaAPI()

class TrackSchema(ModelSchema):
    class Meta:
        model = Track
        fields = "__all__"

class NotFoundSchema(Schema):
    message : str


@api.get("/tracks", response=List[TrackSchema])
def tracks(request):
    return Track.objects.all()


@api.get("/tracks/{track_id}",response={200:TrackSchema,404:NotFoundSchema})
def track(request,track_id:int):
    try:
        track = Track.objects.get(id=track_id)
        return track
    except Track.DoesNotExist:
        return 404, {"message":"Şarkı Bulunamadı."}


@api.post("/tracks", response={201:TrackSchema})
def create_track(request,track:TrackSchema):
    track = Track.objects.create(**track.dict())
    return track