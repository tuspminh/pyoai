import json
import os
from typing import List, Dict, Any
from plugins.base.base_source import BaseSource
from plugins.base.http_client import HTTPClient
from plugins.truyenfull.parser import TruyenFullParser
from plugins.truyenfull.config import TruyenFullConfig


class TruyenFullSource(BaseSource):
    def __init__(self):
        # Đọc dữ liệu từ manifest.json và selectors.json nằm cùng thư mục
        current_dir = os.path.dirname(__file__)

        with open(
            os.path.join(current_dir, "manifest.json"), "r", encoding="utf-8"
        ) as f:
            manifest = json.load(f)

        with open(
            os.path.join(current_dir, "selectors.json"), "r", encoding="utf-8"
        ) as f:
            selectors = json.load(f)

        super().__init__(
            manifest=manifest, selectors=selectors, config=TruyenFullConfig
        )

        self.http_client = HTTPClient()
        self.parser = TruyenFullParser(self.selectors)

    async def search_novels(self, keyword: str, page: int = 1) -> List[Dict[str, Any]]:
        params = {"tukhoa": keyword, "page": page}
        html = await self.http_client.fetch(self.config.SEARCH_ENDPOINT, params=params)
        return self.parser.parse_search_results(html)

    async def get_novel_details(self, novel_url: str) -> Dict[str, Any]:
        html = await self.http_client.fetch(novel_url)
        return self.parser.parse_novel_details(html)

    async def get_chapter_content(self, chapter_url: str) -> Dict[str, Any]:
        html = await self.http_client.fetch(chapter_url)
        return self.parser.parse_chapter_content(html)
