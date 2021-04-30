from PyQt5.QtWidgets import *
from src.view.project.project_window import ProjectWindow
from src.view.project.about_window import AboutWindow
from src.view.project.project_tool_bar import ProjectToolBar
from src.view.project.docks.graph_information_dock import GraphInformationDock
from src.view.project.docks.visualize_graph_dock import VisualizeGraphDock
from src.view.project.docks.invariants_checks_dock import InvariantsCheckDock
from src.store.project_information_store import project_information_store
from src.view.project.docks.invariants_dictionary_dock import InvariantsDictionaryDock
# from src.domain.utils import match_graph_code
from PyQt5 import QtCore
# from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class ProjectController:
    def __init__(self):
        self.project_window = ProjectWindow()

        self.about_window = AboutWindow()

        self.project_tool_bar = ProjectToolBar()

        self.graph_information_dock = GraphInformationDock()
        self.invariants_check_dock = InvariantsCheckDock()
        self.visualize_graph_dock = VisualizeGraphDock()
        self.invariants_dictionary_dock = InvariantsDictionaryDock()

        self.settings = QtCore.QSettings("project", "GraphFilter")

    def show_window(self):
        self.connect_events()
        self.create_docks()

        self.project_window.addToolBar(self.project_tool_bar)

        graph = self.project_tool_bar.fill_combo_graphs(project_information_store.filtered_graphs)

        self.visualize_graph_dock.plot_graph(graph)

        # TODO: pass the correct dictionary to method
        self.invariants_check_dock.create_conditions({}, self.on_check_condition)

        self.project_window.show()

        self.settings.setValue("state", self.project_window.saveState())

    def connect_events(self):
        self.project_window.exit_action.triggered.connect(self.on_exit)

        self.project_window.visualize_action.triggered.connect(self.on_visualize)
        self.project_window.invariants_check_action.triggered.connect(self.on_invariants_check)
        self.project_window.graph_info_action.triggered.connect(self.on_graph_info)
        self.project_window.dictionary_action.triggered.connect(self.on_dictionary)

        self.project_window.restore_layout.triggered.connect(self.on_restore)

        self.project_window.about_action.triggered.connect(self.on_about)

        self.project_tool_bar.combo_graphs.activated.connect(self.on_change_graph)
        self.project_tool_bar.left_button.clicked.connect(self.on_click_button_left)
        self.project_tool_bar.right_button.clicked.connect(self.on_click_button_right)

        # self.project_window.print_action.triggered.connect(self.on_print)

    def on_exit(self):
        self.project_window.close()

    def on_print(self):
        # printer = QPrinter(QPrinter.HighResolution)
        # dialog = QPrintDialog(printer, self)
        #
        # if dialog.exec_() == QPrintDialog.Accepted:
        #     pass
        pass

    def on_visualize(self):
        self.project_window.restoreDockWidget(self.visualize_graph_dock)

    def on_invariants_check(self):
        self.project_window.restoreDockWidget(self.invariants_check_dock)

    def on_graph_info(self):
        self.project_window.restoreDockWidget(self.graph_information_dock)

    def on_dictionary(self):
        self.project_window.restoreDockWidget(self.invariants_dictionary_dock)

    def on_about(self):
        self.about_window.show()

    def on_restore(self):
        self.project_window.restoreState(self.settings.value("state"))

    def create_docks(self):
        self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.visualize_graph_dock)
        self.project_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.graph_information_dock)
        self.project_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.invariants_check_dock)
        self.project_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.invariants_dictionary_dock)

        self.project_window.tabifyDockWidget(self.invariants_dictionary_dock, self.invariants_check_dock)
        self.project_window.setTabPosition(QtCore.Qt.RightDockWidgetArea, QTabWidget.East)

    def on_change_graph(self):
        if self.project_tool_bar.combo_graphs.currentIndex() == 0:
            self.project_tool_bar.left_button.setDisabled(True)
        else:
            self.project_tool_bar.left_button.setDisabled(False)

        if self.project_tool_bar.combo_graphs.currentIndex() == self.project_tool_bar.combo_graphs.count() - 1:
            self.project_tool_bar.right_button.setDisabled(True)
        else:
            self.project_tool_bar.right_button.setDisabled(False)
        #
        # self.project_tool_bar.current_graph = match_graph_code(self.project_tool_bar.combo_graphs.currentText())
        # if self.project_tool_bar.current_graph is not None:
        #     self.visualize_graph_dock.plot_graph(self.project_tool_bar.current_graph)

        # self.graph_information_dock.update_graph_to_table()
        # self.info.update_table_inv({"test": self.combo_graphs.currentText()})

    def on_click_button_left(self):
        self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.currentIndex() - 1)
        self.on_change_graph()

    def on_click_button_right(self):
        self.project_tool_bar.combo_graphs.setCurrentIndex(self.project_tool_bar.combo_graphs.currentIndex() + 1)
        self.on_change_graph()

    def on_check_condition(self):
        check = QCheckBox().sender()
        # TODO: this logic does not belongs here
        # if self.visualize.current_graph is not None:
        #     g = nx.from_graph6_bytes(self.visualize.current_graph.encode('utf-8'))
        # else:
        #     g = None
        #
        # if check.text() not in self.visualize.invariants_selected:
        #     if g is not None:
        #         self.visualize.invariants_selected[check.text()] = \
        #             self.visualize.dic_invariants[check.text()].calculate(g)
        #     else:
        #         self.visualize.invariants_selected[check.text()] = 'None'
        # else:
        #     del self.visualize.invariants_selected[check.text()]
        #
        # self.visualize.info.update_table()
        pass
