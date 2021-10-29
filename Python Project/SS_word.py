import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class SS_word(QMainWindow):
    def __init__(self):
        super(SS_word, self).__init__()
        self.editor= QTextEdit()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.editor.setFontPointSize(20)
        self.Font_size_box= QSpinBox()
        self.create_Toolbar()
        self.create_Menu_Bar()

    def create_Menu_Bar(self):
        Menu_Bar= QMenuBar()
        
        file_menu = QMenu('File', self)
        Menu_Bar.addMenu(file_menu)

        save_as_PDF_action= QAction('save as PDF', self)
        save_as_PDF_action.triggered.connect(self.save_as_PDF)
        file_menu.addAction(save_as_PDF_action)

        edit_menu = QMenu('Edit', self)
        Menu_Bar.addMenu(edit_menu)
        
        view_menu = QMenu('View', self)
        Menu_Bar.addMenu(view_menu)
        
        self.setMenuBar(Menu_Bar)

    def create_Toolbar(self):
        tool_Bar= QToolBar()

        UNDO_action= QAction('Undo', self)
        UNDO_action.triggered.connect(self.editor.undo)
        tool_Bar.addAction(UNDO_action)

        tool_Bar.addSeparator()
        tool_Bar.addSeparator()

        Redo_action= QAction('Redo', self)
        Redo_action.triggered.connect(self.editor.redo)
        tool_Bar.addAction(Redo_action)
        
        tool_Bar.addSeparator()
        tool_Bar.addSeparator()

        copy_action= QAction('Copy', self)
        copy_action.triggered.connect(self.editor.copy)
        tool_Bar.addAction(copy_action)

        tool_Bar.addSeparator()
        tool_Bar.addSeparator()

        cut_action= QAction('Cut', self)
        cut_action.triggered.connect(self.editor.cut)
        tool_Bar.addAction(cut_action)
    
        tool_Bar.addSeparator()
        tool_Bar.addSeparator()

        paste_action= QAction('Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        tool_Bar.addAction(paste_action)

        tool_Bar.addSeparator()
        tool_Bar.addSeparator()

        self.Font_size_box.setValue(20)
        self.Font_size_box.valueChanged.connect(self.set_font_size)
        tool_Bar.addWidget(self.Font_size_box)
       
        self.addToolBar(tool_Bar)

    def set_font_size(self):       
        value = self.Font_size_box.value()
        self.editor.setFontPointSize(value)

    def save_as_PDF(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'save PDF', None,'PDF file (*.pdf)')
        printter= QPrinter(QPrinter.HighResolution)
        printter.setOutputFormat(QPrinter.PdfFormat)
        printter.setOutputFileName(file_path)
        self.editor.document().print(printter)

app=QApplication(sys.argv)
window=SS_word()
window.show()
sys.exit(app.exec_())
