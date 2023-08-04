# PySide6 Collapsible Widget/ frameLayout

Simple collapsible widget for PySide6, made to mimic Maya's native GUI.
Its Forked from https://github.com/aronamao/PySide2-Collapsible-Widget rewritten for PySide6.

![demo](https://user-images.githubusercontent.com/50831997/120691061-49667a00-c4a6-11eb-82fd-dd70270dd1a9.gif)

# How to use

Simply get the content widget via the contentWidget getter and attach your desired layout to it.

```python
layout = QtWidgets.QVBoxLayout()
container = Container("Group")
layout.addWidget(container)

content_layout = QtWidgets.QGridLayout(container.contentWidget)
content_layout.addWidget(QtWidgets.QPushButton("Button"))
```

This example is also available in the docstring of the Container class for easy access inside your IDE.

The Container class also has methods for collapsing, expanding and toggling the widget so you can hook them up to external buttons.

