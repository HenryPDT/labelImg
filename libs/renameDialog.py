try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

from libs.utils import new_icon, label_validator, trimmed

BB = QDialogButtonBox


class RenameDialog(QDialog):
    def __init__(self, old_name=None, parent=None):
        super(RenameDialog, self).__init__(parent)

        self.edit = QLineEdit()
        self.edit.setText(old_name)

        self.button_box = bb = BB(BB.Ok | BB.Cancel, Qt.Horizontal, self)
        bb.button(BB.Ok).setIcon(new_icon('done'))
        bb.button(BB.Cancel).setIcon(new_icon('undo'))
        bb.accepted.connect(self.validate)
        bb.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.button_box, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.edit)

        self.setLayout(layout)

    def validate(self):
        if trimmed(self.edit.text()):
            self.accept()

    def pop_up(self):
        result = self.exec_()
        if result == QDialog.Accepted:
            return self.edit.text()
        return None
    
    

