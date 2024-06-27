from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QItemDelegate

from qfluentwidgets import LineEdit

class JointOneDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = LineEdit(parent)
        only_float_regx = QRegularExpression(r'^(-?((1[0-2][0-9]|1[0-2][0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])(\.\d{1,3})?|130(\.0{1,3})?|13[0-4](\.\d{1,3})?|135(\.0{1,3})?))$')
        only_float_validator = QRegularExpressionValidator(only_float_regx)
        editor.setValidator(only_float_validator)
        return editor
    
class JointTwoDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = LineEdit(parent)
        only_float_regx = QRegularExpression(r'^-?(\d{1,2}(\.\d{1,3})?|8[0-6](\.\d{1,3})?|9[0-6](\.\d{1,3})?)$')
        only_float_validator = QRegularExpressionValidator(only_float_regx)
        editor.setValidator(only_float_validator)
        return editor
    
class JointThreeDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = LineEdit(parent)
        only_float_regx = QRegularExpression(r'^-?(\d{1,2}(\.\d{1,3})?|4[0-6](\.\d{1,3})?|9[0-0](\.\d{1,3})?)$')
        only_float_validator = QRegularExpressionValidator(only_float_regx)
        editor.setValidator(only_float_validator)
        return editor

class JointFourDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = LineEdit(parent)
        only_float_regx = QRegularExpression(r'^-?(1[0-3][0-9](\.\d{1,3})?|14[0-3](\.\d{1,3})?|\d{1,2}(\.\d{1,3})?|1[0-7][0-9](\.\d{1,3})?|18[0-4](\.\d{1,3})?)$')
        only_float_validator = QRegularExpressionValidator(only_float_regx)
        editor.setValidator(only_float_validator)
        return editor
    
class JointFiveDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = LineEdit(parent)
        only_float_regx = QRegularExpression(r'^-?(1[0-9][0-9](\.\d{1,3})?|2[0-1][0-9](\.\d{1,3})?|\d{1,2}(\.\d{1,3})?|3[0-6](\.\d{1,3})?)$')
        only_float_validator = QRegularExpressionValidator(only_float_regx)
        editor.setValidator(only_float_validator)
        return editor
    
class JointSixDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = LineEdit(parent)
        only_float_regx = QRegularExpression(r'^-?(3[0-5][0-9](\.\d{1,3})?|360(\.0{1,3})?|\d{1,2}(\.\d{1,3})?|[1-2]\d{2}(\.\d{1,3})?)$')
        only_float_validator = QRegularExpressionValidator(only_float_regx)
        editor.setValidator(only_float_validator)
        return editor
    
class JointSpeedDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = LineEdit(parent)
        only_float_regx = QRegularExpression(r'^([1-9][0-9]?|100)$')
        only_float_validator = QRegularExpressionValidator(only_float_regx)
        editor.setValidator(only_float_validator)
        return editor
    
class JointDelayTimeDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = LineEdit(parent)
        only_float_regx = QRegularExpression(r'^(30|[1-2]?[0-9]|0)$')
        only_float_validator = QRegularExpressionValidator(only_float_regx)
        editor.setValidator(only_float_validator)
        return editor