import re
from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    """Xóa khoảng trắng thừa và chuẩn hóa văn bản."""
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_html_content(soup_element) -> str:
    """Xóa các thẻ quảng cáo, script và giữ lại định dạng văn bản truyện."""
    if not soup_element:
        return ""

    # Xóa các thành phần không mong muốn
    for tag in soup_element(["script", "style", "iframe", "ins", "div.ads"]):
        tag.decompose()

    # Chuyển đổi các thẻ ngắt dòng thành xuống dòng chuẩn
    for br in soup_element.find_all("br"):
        br.replace_with("\n")

    return soup_element.get_text().strip()


def extract_number(text: str) -> float:
    """Trích xuất số đầu tiên tìm thấy trong chuỗi (ví dụ: 'Chương 123' -> 123)."""
    match = re.search(r"\d+(\.\d+)?", text)
    return float(match.group()) if match else 0.0
