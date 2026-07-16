import asyncio
from plugins.truyenfull.source import TruyenFullSource


async def test():
    # 1. Khởi tạo plugin
    source = TruyenFullSource()
    print(f"--- Đã nạp thành công Plugin: {source.manifest['name']} ---")

    # 2. Thử nghiệm tìm kiếm truyện
    print("\n[Hành động] Đang tìm kiếm truyện 'trai tim cua'...")
    search_results = await source.search_novels("trai tim cua")

    if search_results:
        first_novel = search_results[0]
        print(f"Tìm thấy: {first_novel['title']} | Link: {first_novel['url']}")

        # 3. Thử nghiệm lấy chi tiết truyện từ link đầu tiên
        print(f"\n[Hành động] Đang lấy chi tiết truyện từ: {first_novel['url']}...")
        detail = await source.get_novel_details(first_novel["url"])
        print(f"Tên truyện: {detail['title']}")
        print(f"Tác giả: {detail['author']}")
        print(f"Số lượng chương lấy được ở trang 1: {len(detail['chapters'])}")

        # 4. Thử nghiệm lấy nội dung chương đầu tiên
        if detail["chapters"]:
            first_chapter_url = detail["chapters"][0]["chapter_url"]
            print(f"\n[Hành động] Đang lấy nội dung chương từ: {first_chapter_url}...")
            chapter_data = await source.get_chapter_content(first_chapter_url)
            print(f"Tiêu đề chương: {chapter_data['chapter_title']}")
            print(f"Nội dung (50 ký tự đầu): {chapter_data['content'][:50]}...")
    else:
        print("Không tìm thấy kết quả phù hợp.")


if __name__ == "__main__":
    asyncio.run(test())
