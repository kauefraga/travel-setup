import click, validators, time
from rich import print
from rich.progress import Progress, track
from components.icons import Icon
from pytube import YouTube

@click.command()
@click.argument('url')
@click.option('--audio-only', '-mp3', is_flag=True, help='Install audio only')
def install(url: str, audio_only: bool):
  """Install a youtube video with the highest resolution"""
  if not validators.url(url):
    print('{} [bold red]The URL is not valid'.format(Icon.MINUS.value))
    exit(0)

  print('{} Searching...'.format(Icon.INTERROGATIVE.value))

  video = YouTube(url)

  print('[green]Found!')
  print('{} Title: [orange_red1]{}'.format(Icon.PLUS.value, video.title))
  print('{} Published at: [orange_red]{}'.format(Icon.PLUS.value, video.publish_date))
  print('{} URL: [orange_red1]https://youtube.com/watch?v={}'.format(Icon.PLUS.value, video.video_id))

  print('[bold]Downloading...')

  if audio_only:
    video_download = video.streams.get_audio_only()
  else:
    video_download = video.streams.get_highest_resolution()

  video_download.download('./downloads')
  print('[bold green]Done!')
