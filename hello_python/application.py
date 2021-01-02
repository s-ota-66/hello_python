#! env python
# -*- coding: utf-8 -*-


from hello_python.main_form import MainForm


class Application:
    """
    アプリケーションメイン
    """

    def __init__(self):
        super().__init__()

    def run(self):
        """
        ここでメインウィンドウを開く感じか
        """
        main_form = MainForm()
        main_form.show()
