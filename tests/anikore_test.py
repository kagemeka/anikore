import asyncio
import logging
import random
import unittest

import aiohttp

import anikore

_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(pathname)s %(message)s"
logging.basicConfig(
    format=_LOGGING_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S%z",
    handlers=[logging.StreamHandler()],
    level=logging.DEBUG,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        async def wrap() -> None:
            async with aiohttp.ClientSession() as session:
                anime_ids = await anikore.fetch_anime_ids(session)
                print(len(anime_ids))
                animes = await anikore.fetch_animes(
                    session,
                    random.sample(anime_ids, 1 << 4),
                )
                print(len(animes))

        asyncio.run(wrap())


if __name__ == "__main__":
    unittest.main()
