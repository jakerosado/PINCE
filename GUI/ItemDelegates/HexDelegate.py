"""
Copyright (C) Korcan Karaokçu <korcankaraokcu@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from PyQt6.QtWidgets import QItemDelegate, QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression


class QHexDelegate(QItemDelegate):
    def __init__(self, max_length=2, regexp="[0-9a-fA-F]+", parent=None):
        super().__init__(parent)
        self.max_length = max_length
        self.regexp = regexp

    def createEditor(self, parent, option, index):
        self.editor = QLineEdit(parent)
        self.editor.setMaxLength(self.max_length)
        hex_validator = QRegularExpressionValidator(QRegularExpression(self.regexp), self.editor)
        self.editor.setValidator(hex_validator)
        self.editor.setText(index.model().data(index, Qt.ItemDataRole.DisplayRole))
        self.editor.textChanged.connect(self.check_text)
        return self.editor

    def setEditorData(self, editor, index):
        # Initial text was set in createEditor, this is a trick to dodge the textChanged signal
        return

    def check_text(self):
        if len(self.editor.text()) >= self.max_length:
            self.closeEditor.emit(self.editor, QItemDelegate.EndEditHint.EditNextItem)
