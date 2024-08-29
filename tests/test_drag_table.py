import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QMimeData, QByteArray, QDataStream, QPoint, QEvent
from PySide6.QtGui import QDrag, QPixmap, QPainter, QPen

class TableWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QTableWidget.InternalMove)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.line_position = None
        self.drag_row = None

    def startDrag(self, supportedActions):
        selected_rows = self.selectionModel().selectedRows()
        if not selected_rows:
            return

        self.drag_row = selected_rows[0].row()

        drag = QDrag(self)
        mime_data = QMimeData()
        encoded_data = QByteArray()
        stream = QDataStream(encoded_data, QDataStream.WriteOnly)

        for row in selected_rows:
            for column in range(self.columnCount()):
                item = self.item(row.row(), column)
                if item:
                    stream.writeQString(item.text())
                else:
                    stream.writeQString("")

        mime_data.setData('application/x-qabstractitemmodeldatalist', encoded_data)
        drag.setMimeData(mime_data)
        drag.exec(Qt.MoveAction)

    def dragMoveEvent(self, event):
        self.line_position = event.position().toPoint().y()
        self.viewport().update()
        event.accept()

    def dropEvent(self, event):
        if event.source() == self:
            event.setDropAction(Qt.MoveAction)
            event.accept()

            encoded_data = event.mimeData().data('application/x-qabstractitemmodeldatalist')
            stream = QDataStream(encoded_data, QDataStream.ReadOnly)

            target_row = self.rowAt(int(event.position().y()))
            if target_row == -1:
                target_row = self.rowCount()

            self.insertRow(target_row)

            for column in range(self.columnCount()):
                text = stream.readQString()
                item = QTableWidgetItem(text)
                self.setItem(target_row, column, item)

            # Remove the original row(s)
            for row in sorted(self.selectionModel().selectedRows(), reverse=True):
                self.removeRow(row.row())

            self.line_position = None
            self.drag_row = None
            self.viewport().update()
            super().dropEvent(event)
        else:
            event.ignore()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.line_position is not None:
            painter = QPainter(self.viewport())
            pen = QPen(Qt.black, 2)
            painter.setPen(pen)
            painter.drawLine(0, self.line_position, self.viewport().width(), self.line_position)
            painter.end()

    def moveRow(self, source_row, target_row):
        items = [self.takeItem(source_row, col) for col in range(self.columnCount())]
        self.insertRow(target_row)
        for col, item in enumerate(items):
            self.setItem(target_row, col, item)
        self.removeRow(source_row)

    def dragEnterEvent(self, event):
        event.accept()

    def dragLeaveEvent(self, event):
        self.line_position = None
        self.drag_row = None
        self.viewport().update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = TableWidget(10, 5)
        for row in range(10):
            for column in range(5):
                item = QTableWidgetItem(f"Item {row},{column}")
                self.table.setItem(row, column, item)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setWindowTitle("Table Drag and Drop Example")
        self.resize(600, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())