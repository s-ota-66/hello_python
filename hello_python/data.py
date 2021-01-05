#! env python
# -*- coding: utf-8 -*-

"""
  data.py
   

  Created by Seiji Ota on 2021/01/3.

"""
import hello_python.landmark
import json
import os

"""
jsonパーサー
"""


def load(filename):

    landmarks = []

    # jsonファイルの読み込み
    json_open = open(os.path.join(os.getcwd(), "assets", filename), "r")
    json_load = json.load(json_open)

    count = len(json_load)
    for landmark_json in json_load:
        # Landmark
        landmark = hello_python.landmark.Landmark()
        landmark.id = landmark_json["id"]
        landmark.name = landmark_json["name"]
        landmark.prefectures = landmark_json["prefectures"]
        landmark.imageName = landmark_json["imageName"]
        print(landmark.id)
        print(landmark.name)
        print(landmark.prefectures)
        print(landmark.imageName)

        # coordinates
        coordinates = hello_python.landmark.Coodinates()
        coordinates.longitude = landmark_json["coordinates"]["longitude"]
        coordinates.latitude = landmark_json["coordinates"]["latitude"]
        landmark.coodinates = coordinates

        # sounds
        landmark.sounds = []
        sounds_json = landmark_json["sounds"]
        for sound_json in sounds_json:
            sound = hello_python.landmark.Sound()
            sound.id = sound_json["id"]
            sound.title = sound_json["title"]
            sound.src = sound_json["src"]
            sound.isLive = sound_json["isLive"]
            landmark.sounds.append(sound)

        # description
        description = hello_python.landmark.Description()
        desc_json = landmark_json["description"]
        description.html = desc_json["html"]
        print(description.html)
        description.header = desc_json["header"]
        description.imageName = desc_json["imageName"]
        description.body = desc_json["body"]

        # sections
        description.sections = []
        sections_json = desc_json["sections"]
        for section_json in sections_json:
            section = hello_python.landmark.DescriptionSection()
            section.id = section_json["id"]
            section.title = section_json["title"]
            section.headerImageName = section_json["headerImageName"]
            section.body = section_json["body"]
            section.footerImageName = section_json["footerImageName"]
            description.sections.append(section)

        # banners
        description.banners = []
        banners_json = desc_json["banners"]
        if banners_json != None:
            for banner_json in banners_json:
                banner = hello_python.landmark.Banner()
                banner.id = banner_json["id"]
                banner.imageName = banner_json["imageName"]
                banner.url = banner_json["url"]
                banner.alt = banner_json["alt"]
                description.banners.append(banner)

        landmark.description = description

        landmarks.append(landmark)

    return landmarks
