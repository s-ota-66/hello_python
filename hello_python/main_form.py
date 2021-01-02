#! env python
# -*- coding: utf-8 -*-
import PySimpleGUI as sg


class MainForm:
    """
    docstring
    """

    def __init__(self) -> None:
        super().__init__()
        sg.theme("Dark Brown")

    def show(self):
        """
        docstring
        """
        layout = [
            [sg.Text("これは PySimpleGUI を使ったサンプルプログラムです.")],
            [sg.Button("Quit", size=(15, 1)), sg.Button("OK", size=(15, 1))],
        ]

        window = sg.Window("Hello Python", layout)  # イベントループ

        while True:
            event, values = window.read()  # イベントの読み取り(イベント待ち)
            print("イベント：", event, "、値：", values)  # 確認表示
            if event in (None, "Quit"):
                print("終了します")
                break
        # 終了処理
        window.close()
