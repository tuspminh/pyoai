class PluginError(Exception):
    """Lỗi cơ bản của hệ thống plugin."""

    pass


class NetworkError(PluginError):
    """Lỗi liên quan đến kết nối mạng hoặc HTTP."""

    pass


class ParseError(PluginError):
    """Lỗi xảy ra khi phân tích cú pháp HTML (DOM thay đổi, v.v.)."""

    pass


class ConfigError(PluginError):
    """Lỗi cấu hình plugin thiếu hoặc sai định dạng."""

    pass
