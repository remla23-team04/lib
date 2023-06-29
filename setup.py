import json
from distutils.core import setup

setup(
  name = 'remla_lib',         # How you named your package folder (MyLib)
  packages = ['remla_lib'],   # Chose the same as "name"
  version = json.load(open('src/remla_lib/version.json', 'r'))["version"],      # Start with a small number and increase it with every change you make
  license = 'MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Version aware lib for remla',   # Give a short description about your library
  author = 'Remla team 04',                   # Type in your name
  # author_email = 'your.email@domain.com',      # Type in your E-Mail
  url = 'https://github.com/remla23-team04/lib',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/remla23-team04/lib/archive/refs/tags/a1.tar.gz',    # I explain this later on
  keywords = ['lib'],   # Keywords that define your package best
  # install_requires=[            # I get to this in a second
  #     'validators',
  #     'beautifulsoup4',
  # ],
)
