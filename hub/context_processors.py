from .models import Track

def music_player(request):
    tracks = Track.objects.all()
    return {'tracks':tracks}