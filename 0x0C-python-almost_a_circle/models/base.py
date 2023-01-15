#!/usr/bin/python3
""" Base mode 
Houses a base class eith private attributes
"""
import json
import csv
import os.path

Class Base:
    __nb_objects = 0
    def __init__(self. id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1

