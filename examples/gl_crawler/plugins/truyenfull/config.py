import os
# from plugins.truyenfull import manifest


class TruyenFullConfig:
    # BASE_URL = manifest.get("base_url", "https://truyenfull.live")
    BASE_URL = "https://truyenfull.live"
    SEARCH_ENDPOINT = f"{BASE_URL}/tim-kiem/"
    # https://truyenfull.live/tim-kiem/?tukhoa=tim
    # https://truyenfull.live/tim-kiem/?tukhoa=Trai+tim+cua
    # Định cấu hình số luồng hoặc độ trễ nếu cần để tránh bị chặn IP
    RATE_LIMIT_DELAY = 1.0
