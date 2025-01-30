# from ytmusicapi import YTMusic

# # インスタンスを作成
# ytmusic = YTMusic()

# # YouTube MusicのURLを指定
# video_url = "https://music.youtube.com/watch?v=dtN5DJ9Gvh4&si=QLCMnoFQh10wJIJq"

# # 動画IDを抽出（URLの "v="以降を使用）
# video_id = video_url.split("v=")[1].split("&")[0]  # "&"以降を除去

# # 曲情報を取得
# song_info = ytmusic.get_song(video_id)

# # 曲情報の解析
# if 'videoDetails' in song_info:
#     # 基本情報を取得
#     title = song_info['videoDetails']['title']  # 曲名
#     artist = song_info['videoDetails']['author']  # アーティスト名

#     # アルバム情報の取得
#     track_results = ytmusic.search(artist, filter="songs")
#     if track_results:
#         track = track_results[0]
#         album = track["album"]["name"]

#     # サムネイル画像のURLを取得
#     thumbnails = song_info['videoDetails'].get('thumbnail', {}).get('thumbnails', [])
#     thumbnail_url = thumbnails[-1]['url'] if thumbnails else 'サムネイル画像なし'

#     # 結果を表示
#     print(f"曲名: {title}")
#     print(f"アーティスト: {artist}")
#     print(f"アルバム: {album}")
#     print(f"サムネイルURL: {thumbnail_url}")
# else:
#     print("曲情報が取得できません。レスポンスを確認してください。")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotifyのクレデンシャル
CLIENT_ID = '7983b9b716644de8ad52951ebe81bbde'
CLIENT_SECRET = 'ff80e3a6c64d4d71b91c528833f4d86a'

# 認証
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Spotify楽曲URL
track_url = "https://open.spotify.com/intl-ja/track/5U4PgFWzfzY7VEg9Ck4ziF?si=cb2e6ecb8cf448eb"

# トラック情報を取得
track_info = sp.track(track_url)

# 必要な情報を取得
track_name = track_info['name']
artists = ", ".join(artist['name'] for artist in track_info['artists'])
album_name = track_info['album']['name']

# アルバム画像のURLを取得
album_images = track_info['album']['images']
album_image_url = album_images[0]['url'] if album_images else "画像なし"

# 結果を表示
print(f"曲名: {track_name}")
print(f"アーティスト: {artists}")
print(f"アルバム名: {album_name}")
print(f"アルバム画像URL: {album_image_url}")
