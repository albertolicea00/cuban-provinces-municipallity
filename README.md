
# cuban Provinces...

The "cuban-provinces-municipality" module is a tool that provides an updated and accurate set of data on the provinces and municipalities of Cuba.
This module allows developers to access detailed information about Cuba's territorial and administrative organization.

⌛ Their geographic locations, and other relevant data comming soon ...


## Features

- PyQt5 support
- PyQt5 examples


## Usage/Examples

- [Basic example](https://github.com/albertolicea00/cuban-provinces-municipallity/blob/main/qt.example1.py) 

- [Alligments example](https://github.com/albertolicea00/cuban-provinces-municipallity/blob/main/qt.example2.py)

```python
cb_provinces = QComboBox(root)
cb_municipality = QComboBox(root)
cb_provinces.setGeometry(0,0,200,30)
cb_municipality.setGeometry(0,32,200,30)

a = CubaProvinces_BoxGroup(provinceBox = cb_provinces , municipalityBox = cb_municipality)
a.exec()
```

