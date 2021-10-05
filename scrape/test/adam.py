import sys 
import typing


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/..')


set_globals()
sys.path.append(f'{root}/src/')



def scrape_unscraped_anime() -> typing.NoReturn:
  ... 



if __name__ == '__main__':
  ... 

