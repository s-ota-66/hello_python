#! env python
# -*- coding: utf-8 -*-

"""
  main_form.py
   Forest Notes

  Created by Seiji Ota on 2021/01/3.

"""

from typing import Sized
import PySimpleGUI as sg
import os

from PySimpleGUI.PySimpleGUI import VerticalSeparator, pin

WIN_W: int = 90
WIN_H: int = 25


class MainForm:
    """
    docstring
    """

    __list_box_style = {
        "values": ["aa", "bb", "cc", "dd", "ee"],
        "select_mode": "LISTBOX_SELECT_MODE_SINGLE",
        "enable_events": True,
        "size": (30, 10),
        "key": "-NameList-",
    }

    def __init__(self) -> None:
        super().__init__()
        sg.theme("DarkGreen1")

    def show(self):
        """
        docstring
        """
        image_path = os.path.join(os.getcwd(), "assets/mai.png")
        print(os.getcwd())
        layout = [
            [sg.Text("これは PySimpleGUI を使ったサンプルプログラムです.")],
            [sg.Image(filename=image_path, key="-IMAGE-")],
            [
                sg.Listbox(**self.__list_box_style),
                sg.VerticalSeparator(),
                sg.MLine(default_text="A second multi-line", size=(35, 3)),
            ],
            [sg.Button("Quit", size=(15, 1)), sg.Button("OK", size=(15, 1))],
        ]
        window = sg.Window("Hello Python", layout)  # イベントループ
        window.Resizable = True
        window.read(timeout=1)
        window["-NameList-"].expand(expand_x=True, expand_y=True)
        window["-IMAGE-"].expand(expand_x=True, expand_y=True)

        while True:
            event, values = window.read()  # イベントの読み取り(イベント待ち)
            print("イベント：", event, "、値：", values)  # 確認表示
            if event in (None, "Quit"):
                print("終了します")
                break
        # 終了処理
        window.close()
