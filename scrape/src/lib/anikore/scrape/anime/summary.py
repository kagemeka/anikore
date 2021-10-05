import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Summary():
  total_score: typing.Optional[float]
  review_cnt: int
  shelf_cnt: int 
  rank: int


class ScrapeSummary():
  def __call__(self, soup: bs4.BeautifulSoup) -> Summary:
    ls = soup.find_all(
      class_='l-animeDetailHeader_pointSummary_unit',
    )
    ls = [s.find('strong').text for s in ls]
    ls[0] = None if ls[0] == '計測不能' else float(ls[0])
    for i in range(1, 4): ls[i] = int(ls[i])
    return Summary(*ls)
    
