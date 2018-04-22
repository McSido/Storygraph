from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QTextEdit, QPushButton, QListWidget,
    QListWidgetItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout)


class CreatorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Storygraph - Creator'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):

        # Left box

        select_box = QVBoxLayout()

        new_node_btn = QPushButton()
        new_node_btn.setText('NEW')

        node_list = QListWidget()

        select_box.addWidget(node_list)
        select_box.addWidget(new_node_btn)
        # Right box

        change_box = QVBoxLayout()

        top_box = QHBoxLayout()

        title_field = QLineEdit()

        options_box = QVBoxLayout()

        require_btn = QPushButton()
        require_btn.setText('REQUIREMENTS')

        changes_btn = QPushButton()
        changes_btn.setText('CHANGES')

        options_box.addWidget(require_btn)
        options_box.addWidget(changes_btn)

        top_box.addWidget(title_field)
        top_box.addLayout(options_box)

        text_field = QTextEdit()

        outgoing = QTableWidget()

        change_box.addLayout(top_box)
        change_box.addWidget(text_field)
        change_box.addWidget(outgoing)

        base_box = QHBoxLayout()
        base_box.addLayout(select_box)
        base_box.addLayout(change_box)

        self.setLayout(base_box)

        # Node select area
        # Changes
        # in-Requirements
        # out-options:
        # Linedit | out-changes
        """
        ############################################################
        # Node1 # TITLE                       #  [REQUIREMENTS]    #
        # Node2 #                             #     [CHANGES]      #
        # ...   ####################################################
        #       # Text                                             #
        #       #                                                  #
        #       #                                                  #
        #       #                                                  #
        #       #                                                  #
        #       #                                                  #
        #       #                                                  #
        #       #                                                  #
        #       #                                                  #
        #       #                                                  #
        #       #                                                  #
        #       ####################################################
        #       # NODE1  |  Outgoing-text   |        [CHANGES]     #
        #-------# ...    |       ...        |           ...        #
        # +NEW+ # ...    |       ...        |           ...        #
        ############################################################
        """

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
