import json

from PySide2.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, \
    QLineEdit, QLabel, QMenu, QFileDialog, QComboBox
from PySide2.QtCore import Qt
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget Example")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Age", "Gender"])
        layout.addWidget(self.table_widget)

        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age_input)

        self.gender_combobox = QComboBox()  # 新增下拉选择框
        self.gender_combobox.addItems(["man", "woman"])  # 添加选项
        layout.addWidget(QLabel("Gender:"))
        layout.addWidget(self.gender_combobox)
        self.gender_options = self.gender_combobox.model()

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove")
        self.remove_button.clicked.connect(self.remove_item)
        layout.addWidget(self.remove_button)

        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.export_data)
        layout.addWidget(self.export_button)

        self.import_button = QPushButton("Import")
        self.import_button.clicked.connect(self.import_data)
        layout.addWidget(self.import_button)

        self.setLayout(layout)

        # 添加上下文菜单
        self.context_menu = QMenu(self)
        self.copy_action = self.context_menu.addAction("Copy")
        self.paste_action = self.context_menu.addAction("Paste")
        self.copy_action.triggered.connect(self.copy_selected_row)
        self.paste_action.triggered.connect(self.paste_row)
        self.table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_widget.customContextMenuRequested.connect(self.show_context_menu)

        self.copied_row = None


    def add_item(self):
        name = self.name_input.text()
        age = self.age_input.text()

        if name is not None and age is not None:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(age))

            gender_combobox = QComboBox()  # 创建下拉选择框
            gender_combobox.setModel(self.gender_options)  # 设置选项模型
            # gender_combobox.addItems(["man", "woman"])  # 添加选项
            self.table_widget.setCellWidget(row_position, 2, gender_combobox)

            self.name_input.clear()
            self.age_input.clear()

    def remove_item(self):
        selected_rows = self.table_widget.selectionModel().selectedRows()

        if not selected_rows:
            last_row = self.table_widget.rowCount() - 1
            if last_row >= 0:
                self.table_widget.removeRow(last_row)
        else:
            for row in reversed(selected_rows):
                self.table_widget.removeRow(row.row())

    def copy_selected_row(self):
        selected_row = self.table_widget.currentRow()
        if selected_row >= 0:
            self.copied_row = []
            for col in range(self.table_widget.columnCount()):
                if col == 2:
                    item_widget = self.table_widget.cellWidget(selected_row, col)
                    if item_widget is not None:
                        self.copied_row.append(item_widget.currentText())
                else:
                    item = self.table_widget.item(selected_row, col)
                    if item is not None:
                        self.copied_row.append(item.text())

    def paste_row(self):
        if self.copied_row:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            for col, value in enumerate(self.copied_row):
                if col == 2:  # 如果是性别列
                    gender_combobox = QComboBox()
                    gender_combobox.setModel(self.gender_options)
                    gender_combobox.setCurrentText(value)
                    self.table_widget.setCellWidget(row_position, col, gender_combobox)
                else:
                    self.table_widget.setItem(row_position, col, QTableWidgetItem(value))

    def export_data(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Data to JSON", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)

        if file_name:
            selected_rows = self.table_widget.selectionModel().selectedRows()
            if not selected_rows:
                data = []
                for row in range(self.table_widget.rowCount()):
                    name = self.table_widget.item(row, 0).text()
                    age = self.table_widget.item(row, 1).text()
                    item_widget = self.table_widget.cellWidget(row, 2)
                    if item_widget is not None:
                        gender = item_widget.currentText()
                    else:
                        gender = ""
                    data.append({"Name": name, "Age": age, "Gender": gender})
            else:
                data = []
                for row in selected_rows:
                    name = self.table_widget.item(row.row(), 0).text()
                    age = self.table_widget.item(row.row(), 1).text()
                    item_widget = self.table_widget.cellWidget(row.row(), 2)
                    if item_widget is not None:
                        gender = item_widget.currentText()
                    else:
                        gender = ""
                    data.append({"Name": name, "Age": age, "Gender": gender})

            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4)

    def import_data(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Import Data from JSON", "",
                                                   "JSON Files (*.json);;All Files (*)", options=options)

        if file_name:
            with open(file_name, "r") as json_file:
                data = json.load(json_file)

                self.table_widget.setRowCount(0)  # 清空表格

                for item in data:
                    name = item.get("Name", "")
                    age = item.get("Age", "")
                    gender = item.get("Gender", "")

                    row_position = self.table_widget.rowCount()
                    self.table_widget.insertRow(row_position)
                    self.table_widget.setItem(row_position, 0, QTableWidgetItem(name))
                    self.table_widget.setItem(row_position, 1, QTableWidgetItem(age))

                    gender_combobox = QComboBox()
                    gender_combobox.setModel(self.gender_options)
                    gender_combobox.setCurrentText(gender)
                    self.table_widget.setCellWidget(row_position, 2, gender_combobox)

    def show_context_menu(self, pos):
        self.context_menu.exec_(self.table_widget.mapToGlobal(pos))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
