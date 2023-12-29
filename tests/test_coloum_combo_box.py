from PySide2.QtWidgets import QApplication, QTableWidget, QPushButton, QComboBox, QWidget, QVBoxLayout
import sys

class CustomTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setColumnCount(2)  # 假设有两列
        self.setRowCount(3)     # 假设有三行

        # 在第二列中添加下拉选择框
        for row in range(self.rowCount()):
            combo_box = QComboBox()
            combo_box.addItems(["Option 1", "Option 2", "Option 3"])
            self.setCellWidget(row, 1, combo_box)

        # 设置表头
        self.setHorizontalHeaderLabels(["Column 1", "Column 2"])

    def get_selected_values(self):
        selected_values = []

        # 遍历行
        for row in range(self.rowCount()):
            # 获取第二列的下拉选择框控件
            combo_box = self.cellWidget(row, 1)

            # 获取选中的值
            selected_value = combo_box.currentText()
            selected_values.append(selected_value)

        return selected_values

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.table_widget = CustomTableWidget()
        layout.addWidget(self.table_widget)

        button = QPushButton("Get Selected Values")
        button.clicked.connect(self.get_values)
        layout.addWidget(button)

        self.setLayout(layout)

    def get_values(self):
        selected_values = self.table_widget.get_selected_values()
        print(selected_values)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())