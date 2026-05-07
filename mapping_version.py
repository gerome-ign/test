from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QTabBar,QMessageBox,QAbstractItemView,QListWidget

# QT6
try :
    Dialog = Qt.WindowType.Dialog
    WindowCloseButtonHint = Qt.WindowType.WindowCloseButtonHint
    WindowTitleHint = Qt.WindowType.WindowTitleHint
    WindowStaysOnTopHint = Qt.WindowType.WindowStaysOnTopHint
    Warning = QMessageBox.Icon.Warning
    YesRole = QMessageBox.ButtonRole.YesRole
    AcceptRole = QMessageBox.ButtonRole.AcceptRole
    WaitCursor = Qt.CursorShape.WaitCursor
    Warning = QMessageBox.Icon.Warning
    Ok = QMessageBox.StandardButton.Ok
# QT5
except :
    Dialog = Qt.Dialog
    WindowCloseButtonHint = Qt.WindowCloseButtonHint
    WindowTitleHint = Qt.WindowTitleHint
    WindowStaysOnTopHint = Qt.WindowStaysOnTopHint
    Warning = QMessageBox.Warning
    YesRole = QMessageBox.YesRole
    AcceptRole = QMessageBox.AcceptRole
    WaitCursor = Qt.WaitCursor
    Warning = QMessageBox.Warning
    Ok = QMessageBox.Ok