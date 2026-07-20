import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QToolButton,
    QRadioButton,
    QCheckBox,
    QCommandLinkButton,
    QButtonGroup,
    QLabel,
)
from qt_material import apply_stylesheet


class ButtonShowcase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Các loại nút bấm trong PySide6")
        self.resize(500, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # 1. QPushButton tiêu chuẩn
        layout.addWidget(QLabel("<b>1. QPushButton (Nút thông thường):</b>"))
        btn_normal = QPushButton("Nút bấm thường")
        layout.addWidget(btn_normal)

        # 2. QToolButton (Nút công cụ)
        layout.addWidget(QLabel("<b>2. QToolButton (Nút công cụ / Icon):</b>"))
        tool_btn = QToolButton()
        tool_btn.setText("Cài đặt")
        # Thử set icon mặc định của hệ thống để hiển thị
        tool_btn.setIcon(
            self.style().standardIcon(self.style().StandardPixmap.SP_ComputerIcon)
        )
        tool_btn.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )  # Hiện cả chữ và icon
        layout.addWidget(tool_btn)

        # 3. QRadioButton (Chọn 1 trong nhiều)
        layout.addWidget(QLabel("<b>3. QRadioButton (Chọn duy nhất 1):</b>"))
        radio_layout = QHBoxLayout()
        radio1 = QRadioButton("Lựa chọn A")
        radio2 = QRadioButton("Lựa chọn B")
        radio1.setChecked(True)  # Mặc định chọn trước một nút
        radio_layout.addWidget(radio1)
        radio_layout.addWidget(radio2)
        layout.addLayout(radio_layout)

        # 4. QCheckBox (Chọn nhiều hoặc Bật/Tắt)
        layout.addWidget(QLabel("<b>4. QCheckBox (Hộp kiểm bật/tắt):</b>"))
        check_layout = QHBoxLayout()
        chk1 = QCheckBox("Tính năng 1")
        chk2 = QCheckBox("Tính năng 2")
        check_layout.addWidget(chk1)
        check_layout.addWidget(chk2)
        layout.addLayout(check_layout)

        # 5. QCommandLinkButton (Nút hướng dẫn / Điều hướng)
        layout.addWidget(QLabel("<b>5. QCommandLinkButton (Nút kèm mô tả):</b>"))
        cmd_btn = QCommandLinkButton(
            "Tiến hành nâng cấp hệ thống",
            "Tự động tải gói cài đặt mới nhất và khởi động lại ứng dụng.",
        )
        layout.addWidget(cmd_btn)

        layout.addStretch()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonShowcase()
    apply_stylesheet(app, theme="dark_teal.xml")
    window.show()
    sys.exit(app.exec())
