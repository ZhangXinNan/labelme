from qtpy.QtCore import Qt
from qtpy import QtWidgets


class EscapableQListWidget(QtWidgets.QListWidget):
<<<<<<< HEAD

    def keyPressEvent(self, event):
=======
    def keyPressEvent(self, event):
        super(EscapableQListWidget, self).keyPressEvent(event)
>>>>>>> upstream/master
        if event.key() == Qt.Key_Escape:
            self.clearSelection()
