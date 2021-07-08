import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Summary():
  total_score: float
  review_cnt: int
  shelf_cnt: int 
  rank: int



class ScrapeSummary():
  
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Summary:
    cls_ = (
      'l-animeDetailHeader_'
      'pointSummary_unit'
    )
    ls = soup.find_all(
      class_=cls_,
    )
    ls = [
      s.find('strong').text
      for s in ls
    ]
    ls[0] = float(ls[0])
    for i in range(1, 4):
      ls[i] = int(ls[i])
    return Summary(*ls)
    
