import flet as ft
import flet_audio as fta
#I'll try to put the album covers(eventually)

def main(page: ft.Page):
    page.title = "Spotify TercerMundista"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    playlist = [
        {
            "title": "Take On Me",
            "artist": "a-ha",
            "album": "Hunting High and Low",
            "audio": "ASSETS\AUDIO\A-ha - Take On Me (Official Video) [4K].mp3",
        },
        {
            "title": "Copacabana",
            "artist": "Barry Manilow",
            "album": "Dance Vault Mixes - Copacabana(At the Copa)",
            "audio": "ASSETS\AUDIO\Barry Manilow - Copacabana - 1978..mp3",
        },
        {
            "title": "I Wish You Love",
            "artist": "Laufey",
            "album": "Typical Of Me",
            "audio": "ASSETS\AUDIO\Laufey - I Wish You Love (Official Audio).mp3",
        },
        {
            "title": "Let You Break My Heart Again",
            "artist": "Laufey & Philarmonia Orchestra",
            "album": "It's a single",
            "audio": "ASSETS\AUDIO\Let You Break My Heart Again - Laufey & Philharmonia Orchestra (Official Audio).mp3",
        },
        {
            "title": "Main Menu",
            "artist": "Bell Kalengar",
            "album": "Dead Plate(Original Soundtrack)",
            "audio": "ASSETS\AUDIO\Main Menu.mp3",
        },
    ]

    current_index = 0
    is_playing = False

    audio_player = fta.Audio(
        src=playlist[current_index]["audio"],
        autoplay=False,
        volume=1,
        balance=0,
    )

    title_text = ft.Text(size=22, weight="bold")
    artist_text = ft.Text(size=16)
    album_text = ft.Text(size=14)
#Functions
    def update_song_info():
        song = playlist[current_index]
        title_text.value = f"Title: {song['title']}"
        artist_text.value = f"Artist: {song['artist']}"
        album_text.value = f"Album: {song['album']}"
        page.update()

    def set_song():
        audio_player.src = playlist[current_index]["audio"]

#Controls
    async def play_pause(e):
        nonlocal is_playing
        if is_playing:
            await audio_player.pause()
            play_btn.text = "Play"
        else:
            await audio_player.play()
            play_btn.text = "Pause"
        is_playing = not is_playing
        page.update()

    async def next_song(e):
        nonlocal current_index, is_playing
        current_index = (current_index + 1) % len(playlist)
        set_song()
        update_song_info()
        await audio_player.play()
        is_playing = True
        play_btn.text = "Pause"
        page.update()

    async def prev_song(e):
        nonlocal current_index, is_playing
        current_index = (current_index - 1) % len(playlist)
        set_song()
        update_song_info()
        await audio_player.play()
        is_playing = True
        play_btn.text = "Pause"
        page.update()

#Buttons
    previous_btn = ft.ElevatedButton("Previous", on_click=prev_song)
    play_btn = ft.ElevatedButton("Play", on_click=play_pause)
    next_btn = ft.ElevatedButton("Next", on_click=next_song)

#Final Setup
    page.add(
        ft.Column(
            [
                title_text,
                artist_text,
                album_text,
                ft.Row(
                    [previous_btn, play_btn, next_btn],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    update_song_info()

ft.run(main, assets_dir="ASSETS")
