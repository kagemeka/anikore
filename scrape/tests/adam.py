import sys 
import typing


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/..')


set_globals()
sys.path.append(f'{root}/src/')

from lib.adam import add_new_animes, update_animes



if __name__ == '__main__':
  # add_new_animes()
  update_animes()