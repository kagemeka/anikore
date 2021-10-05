import typing
from .make_df import MakeDFs
from .store import Store



class Adam():
  def __call__(self) -> typing.NoReturn:
    df = MakeDFs()()
    print(df)
    if df is None: return
    Store()(df)