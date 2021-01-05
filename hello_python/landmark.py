#! env python
# -*- coding: utf-8 -*-

"""
  landmark.py
   Forest Notes

  Created by Seiji Ota on 2021/01/3.

"""

import hello_python.data


class Forest:

    __instance = None
    __landmarks = []

    def __new__(cls):
        raise NotImplementedError("Cannot initialize via Constructor")

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__landmarks = hello_python.data.load("landmarkData.json")
            cls.__instance = cls.__internal_new__()

        return cls.__instance

    def __init__(self) -> None:
        super().__init__()

    @property
    def landmarks(self):
        return self.__landmarks


class Landmark:
    def __init__(self) -> None:
        super().__init__()
        self.id = 0
        self.name = ""
        self.prefectures = ""
        self.imageName = ""
        self.coodinates = Coodinates()
        self.sounds = []
        self.description = Description()


class Coodinates:
    def __init__(self) -> None:
        super().__init__()
        self.latitude = 0.0
        self.longitude = 0.0


class Sound:
    def __init__(self) -> None:
        super().__init__()
        self.id = 0
        self.title = ""
        self.src = ""
        self.isLive = False

    @property
    def requestURL(self):
        pass

    @requestURL.getter
    def requestURL(self):
        return "https://www.forestnotes.jp/api/streamurl?id=" + self.src


class Description:
    def __init__(self) -> None:
        super().__init__()
        self.html = ""
        self.header = ""
        self.imageName = ""
        self.body = ""
        self.sections = []
        self.banners = []


class DescriptionSection:
    def __init__(self) -> None:
        super().__init__()
        self.id = 0
        self.title = ""
        self.headerImageName = ""
        self.body = ""
        self.footerImageName = ""


class Banner:
    def __init__(self) -> None:
        super().__init__()
        self.id = 0
        self.imageName = ""
        self.url = ""
        self.alt = ""
