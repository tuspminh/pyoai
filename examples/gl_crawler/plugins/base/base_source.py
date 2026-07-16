from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseSource(ABC):
    def __init__(
        self, manifest: Dict[str, Any], selectors: Dict[str, Any], config: Any
    ):
        self.manifest = manifest
        self.selectors = selectors
        self.config = config

    @abstractmethod
    async def search_novels(self, keyword: str, page: int = 1) -> List[Dict[str, Any]]:
        """Tìm kiếm truyện theo từ khóa."""
        pass

    @abstractmethod
    async def get_novel_details(self, novel_url: str) -> Dict[str, Any]:
        """Lấy thông tin chi tiết truyện (Tên, tác giả, trạng thái, danh sách chương)."""
        pass

    @abstractmethod
    async def get_chapter_content(self, chapter_url: str) -> Dict[str, Any]:
        """Lấy nội dung chi tiết của một chương."""
        pass
