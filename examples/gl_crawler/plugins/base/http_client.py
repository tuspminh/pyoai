import httpx
from typing import Dict, Any, Optional
from plugins.base.exceptions import NetworkError


class HTTPClient:
    def __init__(self, default_headers: Optional[Dict[str, str]] = None):
        self.headers = default_headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        }

    async def fetch(self, url: str, params: Optional[Dict[str, Any]] = None) -> str:
        """Gửi yêu cầu GET và trả về nội dung HTML dạng chuỗi."""
        try:
            async with httpx.AsyncClient(
                headers=self.headers, follow_redirects=True, timeout=15.0
            ) as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                return response.text
        except httpx.HTTPStatusError as e:
            raise NetworkError(f"HTTP lỗi {e.response.status_code} khi truy cập: {url}")
        except httpx.RequestError as e:
            raise NetworkError(f"Lỗi kết nối mạng mạng: {str(e)}")
