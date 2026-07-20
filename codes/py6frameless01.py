import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class FramelessWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        # 1. Bỏ viền và thanh tiêu đề mặc định
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 2. Làm nền cửa sổ trong suốt để bo góc
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # 3. Tạo Widget trung tâm để chứa giao diện (áp dụng bo góc và đổ bóng tại đây)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Dùng QSS để bo góc và đổi màu nền cửa sổ của bạn
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #2e3440; 
                border-radius: 15px;
            }
        """)

        # Bố cục giao diện
        layout = QVBoxLayout()
        self.label = QLabel("Cửa sổ tràn viền PySide6")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 24px;")
        layout.addWidget(self.label)
        self.central_widget.setLayout(layout)

        # Biến lưu trữ vị trí chuột để kéo cửa sổ
        self.old_pos = QPoint()

    # 4. Ghi đè sự kiện nhấn chuột (lưu vị trí hiện tại)
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    # 5. Ghi đè sự kiện di chuyển chuột (tính khoảng cách và di chuyển cửa sổ)
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FramelessWindow()
    window.show()
    sys.exit(app.exec())
