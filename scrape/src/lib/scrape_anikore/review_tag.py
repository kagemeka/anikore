import dataclasses
import typing



@dataclasses.dataclass
class ReviewTag():
  anime_id: int
  tag: str
  cnt: int



class ScrapeReviewTag():

  def __call__(
    self,
    anime_id: int
  ) -> ReviewTag:
    self.__id = anime_id
    ...
    


  def __init__(
    self,
  ) -> typing.NoReturn:
    ...

  
