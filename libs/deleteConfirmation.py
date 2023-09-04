try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

from libs.utils import new_icon, trimmed

BB = QDialogButtonBox


class DeleteConfirmationDialog(QDialog):
    def __init__(self, image_name=None, parent=None):
        super(DeleteConfirmationDialog, self).__init__(parent)

        self.image_name = image_name

        self.label = QLabel(f"Are you sure you want to delete the image: {self.image_name}?")

        self.button_box = bb = BB(BB.Yes | BB.No, Qt.Horizontal, self)
        bb.button(BB.Yes).setIcon(new_icon('delete'))
        bb.button(BB.No).setIcon(new_icon('undo'))
        bb.accepted.connect(self.accept)
        bb.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_box, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)

    def pop_up(self):
        result = self.exec_()
        if result == QDialog.Accepted:
            return True
        return False
