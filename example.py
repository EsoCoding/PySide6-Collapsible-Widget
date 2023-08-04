from PySide6 import QtWidgets
from PySide6.QtGui import QPalette, QColor
from Container import Container
import sys

# Create a custom MainWindow class that inherits from QtWidgets.QMainWindow
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget for the main window
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout and assign it to the central widget
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Create an instance of the Container class and add it to the layout
        self.container = Container("Group", color_background=True)
        self.layout.addWidget(self.container)

        # Create a content layout for the Container and add a button to it
        content_layout = QtWidgets.QGridLayout(self.container.contentWidget)
        content_layout.addWidget(QtWidgets.QPushButton("Button"))

        # Create a toggle button and connect it to the container's toggle method
        self.toggle_button = QtWidgets.QPushButton("Toggle Container")
        self.toggle_button.clicked.connect(self.toggle_container)
        self.layout.addWidget(self.toggle_button)

        # Add a vertical spacer at the bottom
        self.layout.addStretch(1)

    def toggle_container(self):
        """Toggle the visibility of the container."""
        if self.container.contentWidget.isVisible():
            self.container.collapse()
        else:
            self.container.expand()


# Define a function to apply a dark theme to the application.
def apply_dark_theme(app):
    """Apply dark theme to the application."""
    # Create a QPalette object.
    palette = QPalette()

    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

    app.setPalette(palette)


if __name__ == "__main__":
    # Create a QApplication object.
    app = QtWidgets.QApplication(sys.argv)

    # Apply the dark theme to the application.
    apply_dark_theme(app)

    # Create a MainWindow object.
    main_window = MainWindow()

    # Show the main window.
    main_window.show()

    # Run the application event loop.
    sys.exit(app.exec())

