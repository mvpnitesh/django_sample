import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Song
# Create your views here.


def get_songs(request):
	if request.method=="POST":
		data = request.body
		# import ipdb; ipdb.set_trace()
		song_data = json.loads(str(data, 'utf-8'))
		new_song = Song.objects.create(**song_data)	
		song_data['id'] = new_song.id
		return JsonResponse(song_data)
	else:

		songs = [song.to_dict() for song in Song.objects.all()]
		response_dict = {'items':songs}
		return JsonResponse(response_dict)

def get_homepage(request):
	return render(request, template_name="base.html")