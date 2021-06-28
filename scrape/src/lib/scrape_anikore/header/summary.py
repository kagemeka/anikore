import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Summary():
  total_score: int
  review_cnt: int
  shelf_cnt: int 
  rank: int



class ScrapeSummary():
  
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Summary:
    summary_base = (
      'l-animeDetailHeader_pointSummary_unit'
    )
    summaries = soup.find_all(
      'div',
      {
        'class': summary_base,
      },
    )
    return Summary(*(
      s.find('strong').text
      for s in summaries
    ))
    
