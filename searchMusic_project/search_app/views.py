from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Music
from .forms import CustomSignupForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def opening(request):
        return render(request, "app_system/opening.html")

class SignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'account_system/signup.html'
    success_url = reverse_lazy('main')  # 登録後のリダイレクト先

    def form_valid(self, form):
        # ユーザーを保存してログイン
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

def mainpage(request):
    music = Music.objects.order_by('-id')
    keyword = request.GET.get('keyword')

    if keyword:
        music = music.filter(
                Q(musicname__icontains=keyword) | Q(musicvocalist__icontains=keyword) | Q(albumname__icontains=keyword) | Q(category__icontains=keyword)
            )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, "app_system/main.html", {'music': music })

def Jpop(request):
    music = Music.objects.order_by('-id')
    keyword = "J-pop"

    if keyword:
        music = music.filter(
            Q(category__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, "app_system/main.html", {'music': music })

def bokaro(request):
    music = Music.objects.order_by('-id')
    keyword = "ボカロ"

    if keyword:
        music = music.filter(
            Q(category__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, "app_system/main.html", {'music': music })

def rock(request):
    music = Music.objects.order_by('-id')
    keyword = "ロック"

    if keyword:
        music = music.filter(
            Q(category__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, "app_system/main.html", {'music': music })

def hiphop(request):
    music = Music.objects.order_by('-id')
    keyword = "hiphop"

    if keyword:
        music = music.filter(
            Q(category__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, "app_system/main.html", {'music': music })

def jaz(request):
    music = Music.objects.order_by('-id')
    keyword = "jaz"

    if keyword:
        music = music.filter(
            Q(category__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, "app_system/main.html", {'music': music })

def classic(request):
    music = Music.objects.order_by('-id')
    keyword = "classic"

    if keyword:
        music = music.filter(
            Q(category__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, "app_system/main.html", {'music': music })

def profile_view(request):
    User = request.user
    return render(request, 'app_system/profile.html', {'User': User})

class detail(DetailView):
    model = Music
    template_name='app_system/detail.html'

class edit(CreateView):
    template_name = "app_system/edit.html"
    model = Music
    fields = ('musicname', 'musicvocalist', 'musicimages', 'albumname', 'musicurl', 'musicselect')
    success_url = reverse_lazy("main")

class update(UpdateView):
    template_name = "app_system/update.html"
    model = Music
    fields = ('musicname', 'musicvocalist', 'musicimages', 'albumname', 'musicurl', 'musicselect', 'category')
    def get_success_url(self):
        return reverse_lazy("main")

class delete(DeleteView):
    template_name = "app_system/delete.html"
    model = Music
    success_url = reverse_lazy("main")

ytmusic = YTMusic()

def youtubeurl(request):
    if request.method == 'POST':
        video_url = request.POST.get("youtubeurl")
        try:
            video_id = video_url.split("v=")[1].split("&")[0]  # "&"以降を除去

            # 曲情報を取得
            song_info = ytmusic.get_song(video_id)

            # 曲情報の解析
            if 'videoDetails' in song_info:
                # 基本情報を取得
                title = song_info['videoDetails']['title']  # 曲名
                artist = song_info['videoDetails']['author']  # アーティスト名

                # アルバム情報の取得
                track_results = ytmusic.search(artist, filter="songs")
                if track_results:
                    track = track_results[0]
                    album = track["album"]["name"]

                # サムネイル画像のURLを取得
                thumbnails = song_info['videoDetails'].get('thumbnail', {}).get('thumbnails', [])
                thumbnail_url = thumbnails[-1]['url'] if thumbnails else 'サムネイル画像なし'

                Music.objects.create(
                    musicname=title,
                    musicvocalist=artist,
                    musicimages=thumbnail_url,
                    albumname=album,
                    musicurl=video_url,
                    musicselect="YouTubeMusic"
                )
                return redirect("main")
        except IndexError as e:
            return redirect("error")

def spotifyurl(request):
    if request.method == 'POST':
        video_url = request.POST.get("spotifyurl")
        CLIENT_ID = '7983b9b716644de8ad52951ebe81bbde'
        CLIENT_SECRET = 'ff80e3a6c64d4d71b91c528833f4d86a'
        # 認証
        auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        # Spotify楽曲URL
        track_url = video_url

        # トラック情報を取得
        track_info = sp.track(track_url)

        # 必要な情報を取得
        track_name = track_info['name']
        artists = ", ".join(artist['name'] for artist in track_info['artists'])
        album_name = track_info['album']['name']

        # アルバム画像のURLを取得
        album_images = track_info['album']['images']
        album_image_url = album_images[0]['url'] if album_images else "画像なし"

        Music.objects.create(
                    musicname=track_name,
                    musicvocalist=artists,
                    musicimages=album_image_url,
                    albumname=album_name,
                    musicurl=track_url,
                    musicselect="Spotify",
        )
    return redirect("main")


def errorpage(request):
        return render(request, "app_system/error.html")


