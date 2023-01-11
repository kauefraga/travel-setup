import click
from commands.install import install

@click.version_option('1.0.0', message='%(prog)s version %(version)s')
@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
  """
    A Youtube downloader made with Python\n
      example: python src/main.py install [URL]
  """
  pass

if __name__ == '__main__':
  cli.add_command(install)
  cli()
