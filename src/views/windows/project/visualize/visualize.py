from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from src.views.windows.project.visualize.docks.info import Info
from src.views.windows.project.visualize.docks.graph import Graph
import re


def match_graph_code(text):
    pattern = re.compile(r'(Graph \d* - )(.*)')
    match = pattern.match(text)
    print(match.group(2))
    return match.group(2)


class Visualize(QWidget):

    def __init__(self, project_window):
        super().__init__()

        self.graph = None
        self.info = None

        self.tool_bar = None

        self.project_window = project_window

        self.combo_graphs = QComboBox()
        self.combo_graphs.adjustSize()
        self.combo_graphs.setMaximumWidth(200)
        self.combo_graphs.activated.connect(self.change_graph)

        self.current_graph = 'L??????????^~@'

        self.create_tool_bar()
        self.create_docks()

    def create_tool_bar(self):
        if self.tool_bar is None:
            self.tool_bar = QToolBar("Tool Bar")
            self.tool_bar.layout().setSpacing(30)
            self.tool_bar.layout().setContentsMargins(15, 10, 20, 20)
            self.tool_bar.setMovable(False)
            self.tool_bar.addWidget(QLabel("List of graphs filtered"))

            self.tool_bar.addWidget(self.combo_graphs)
            self.tool_bar.addSeparator()
            self.tool_bar.addAction(self.project_window.zoom_in_action)
            self.tool_bar.addAction(self.project_window.zoom_out_action)
            self.tool_bar.addAction(self.project_window.zoom_fit_action)
            self.tool_bar.addAction(self.project_window.print_action)
            self.project_window.addToolBar(self.tool_bar)

    def create_docks(self):
        if (self.graph and self.info) is None:
            self.graph = Graph(self)
            self.info = Info(self)
            self.project_window.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.graph)
            self.project_window.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.info)

    def remove_docks(self):
        if self.graph and self.info is not None:
            self.project_window.removeDockWidget(self.graph)
            self.project_window.removeDockWidget(self.info)

            self.graph = None
            self.info = None

    def fill_combo(self, file_out_path):
        for file in file_out_path:
            lines = open(file, 'r').read().splitlines()
            for i, line in enumerate(lines):
                self.combo_graphs.addItem(f'Graph {i} - {line}')
        self.graph.plot_graph(match_graph_code(self.combo_graphs.currentText()))

    def change_graph(self):
        match_graph_code(self.combo_graphs.currentText())
        self.graph.plot_graph(self.current_graph)
