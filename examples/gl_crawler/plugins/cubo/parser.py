from bs4 import BeautifulSoup
from typing import List, Dict, Any
from plugins.base import parser_utils
from plugins.base.exceptions import ParseError


class TruyenFullParser:
    def __init__(self, selectors: Dict[str, Any]):
        self.selectors = selectors

    def parse_search_results(self, html: str) -> List[Dict[str, Any]]:
        soup = BeautifulSoup(html, "html.parser")
        results = []
        items = soup.select(self.selectors["search"]["item"])

        for item in items:
            try:
                title_el = item.select_one(self.selectors["search"]["title"])
                if not title_el:
                    continue

                author_el = item.select_one(self.selectors["search"]["author"])

                results.append(
                    {
                        "title": parser_utils.clean_text(title_el.text),
                        "url": title_el.get("href", ""),
                        "author": parser_utils.clean_text(author_el.text)
                        if author_el
                        else "Ẩn danh",
                    }
                )
            except Exception as e:
                raise ParseError(f"Lỗi phân tích mục tìm kiếm: {str(e)}")
        return results

    def parse_novel_details(self, html: str) -> Dict[str, Any]:
        soup = BeautifulSoup(html, "html.parser")
        try:
            title_el = soup.select_one(self.selectors["detail"]["title"])
            author_el = soup.select_one(self.selectors["detail"]["author"])
            status_el = soup.select_one(self.selectors["detail"]["status"])
            desc_el = soup.select_one(self.selectors["detail"]["description"])

            # Lấy danh sách chương xuất hiện trên trang hiện tại
            chapters = []
            chapter_els = soup.select(self.selectors["detail"]["chapter_item"])
            for ch in chapter_els:
                chapters.append(
                    {
                        "chapter_title": parser_utils.clean_text(ch.text),
                        "chapter_url": ch.get("href", ""),
                    }
                )

            return {
                "title": parser_utils.clean_text(title_el.text)
                if title_el
                else "Không rõ",
                "author": parser_utils.clean_text(author_el.text)
                if author_el
                else "Không rõ",
                "status": parser_utils.clean_text(status_el.text)
                if status_el
                else "Không rõ",
                "description": parser_utils.clean_html_content(desc_el)
                if desc_el
                else "",
                "chapters": chapters,
            }
        except Exception as e:
            raise ParseError(f"Lỗi phân tích chi tiết truyện: {str(e)}")

    def parse_chapter_content(self, html: str) -> Dict[str, Any]:
        soup = BeautifulSoup(html, "html.parser")
        try:
            title_el = soup.select_one(self.selectors["chapter"]["title"])
            content_el = soup.select_one(self.selectors["chapter"]["content"])

            return {
                "chapter_title": parser_utils.clean_text(title_el.text)
                if title_el
                else "Không có tiêu đề",
                "content": parser_utils.clean_html_content(content_el)
                if content_el
                else "Nội dung trống",
            }
        except Exception as e:
            raise ParseError(f"Lỗi phân tích nội dung chương: {str(e)}")
