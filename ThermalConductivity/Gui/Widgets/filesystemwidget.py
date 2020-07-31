from PyQt5 import QtWidgets, QtCore

class TreeView():
    def __init__(self,treeView):
        self.tree = treeView
    def initialize_tree(self):
        model = QtWidgets.QFileSystemModel()
        model.setRootPath("")
        treeView.setModel(model)
        treeView.scrollTo(model.index(QtCore.QDir.currentPath()))
        treeView.setSortingEnabled(True)
        treeView.setIndentation(20)
        return

    def resize(self):
        treeView.setColumnWidth(0, treeView.width())
        return

    def load_file(self):
        model = treeView.model()
        filename = os.path.abspath(model.filePath(treeView.currentIndex()))
        self.filename = filename
        print("Loaded %s"%filename)
        return

