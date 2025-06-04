"""
 ***************************************************************************************************
 * @file   main.py
 * @author Yousef Naiem team
 * @brief Implementation for the Azka-bot chatbot application
 ***************************************************************************************************
 """

""" Imports ---------------------------------------------------------------------------------------"""
import random
from tkinter import Y
import os
from tabulate import tabulate
import json
import re
import string
import datetime
from datetime import *
#track order, order history
""" Public and private data ------------------------------------------------------------------------"""
application_info=["Full Name","Job Applied","Address","Phone Number","Email","National Identification Number (Raqam Qawmi)","Employment Desired","Worked for us before?","Explain (work)","Convicted Before?","Explain (convicted)","High School","HS Start Date","HS End date","HS Graduate?","College","College Start Date","College End Date","College Graduate?","Degree"]
jobs=["Delivery Driver","Store Clerk","Technical Support","Office Work"]
employment_desired=["Full-time", "Part-time","Seasonal"]
locations_list = ["Cairo Festival City Mall" , "Mall of Arabia", "Dandy Mega Mall", "City Centre Almaza", "City Stars", "Point 90"] #6 locations
Phone_speclist=["Dimensions","Weight","System-On-a-Chip(SoC)","CPU","RAM","Storage","Display","Battery","OS","Camera","SIM card","Wi-Fi","Bluetooth","Positioning"]
Laptop_speclist=["Dimensions","Weight","CPU","GPU","RAM","Storage","Display","Battery","OS","Camera","SIM card","Wi-Fi","Bluetooth","Positioning"]
Desktop_speclist=["CPU","GPU","RAM"]
allitems = [
    "iPhone 14 Pro Max.","iPhone 14 Pro.","iPhone 14 Plus.",
    "iPhone 14.","iPhone 13 Pro Max.","iPhone 13 Pro.","iPhone 13.",
    "iPhone 13 mini.","Galaxy S22 Ultra","Galaxy S22+","Galaxy S22","Galaxy S21 Ultra",
    "Galaxy S21+","Galaxy S21","Galaxy Z Flip4","Galaxy Z Fold4",
    "Galaxy Note20","Mate Xs 2","Mate X2","Mate 50 Pro","Mate 50","Mate 40 Pro+","Mate 40 Pro","Mate 40",
    "Pixel 7 Pro","Pixel 7","Pixel 6a",
    "iPad Pro","iPad Air","iPad","iPad mini","Galaxy Tab S8 Ultra","Galaxy Tab S8+","Galaxy Tab S8",
    "Legion 7i Gen 7 (16” Intel) Gaming Laptop","Yoga 9i (14” Intel) 2 in 1 Laptop",
    "ThinkPad X1 Extreme Gen 4 (16” Intel) Laptop","OMEN 16 2022 (INTEL)",
    "HP Spectre x360 13.5","HP Envy x360 15.6(Intel)","Legion Tower 7i Gen 7 with RTX 3080",
    "OMEN 45L (INTEL)",
    ]
#===========================================================================================================================================================================================================================
#Iphone
#===================================================================================================================================================
iphone=[["iPhone 14 Pro Max.",["77.6 x 160.7 x 7.85 mm","240 g","Apple A16 Bionic","Cores : 6","6 GB","128 GB, 256 GB, 512 GB, 1024 GB","6.7 in, OLED, 1290 x 2796 pixels, 24 bit ","Li-lon","iOS 16","8000 x 6000 pixels, 3840 x 2160 pixels, 60 fps","eSIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.3"," GPS, A-GPS, GLONASS, Galileo, QZSS"]],["iPhone 14 Pro.",["71.5 x 147.5 x 7.85 mm","206 g","Apple A16 Bionic","Cores : 6"," 6 GB"," 128 GB, 256 GB, 512 GB, 1024 GB"," 6.1 in, OLED, 1179 x 2556 pixels, 24 bit"," Li-Ion"," iOS 16"," 8000 x 6000 pixels, 3840 x 2160 pixels, 60 fps","eSIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.3","  GPS, A-GPS, GLONASS, Galileo, QZSS"]],["iPhone 14 Plus.",["78.1 x 160.8 x 7.8 mm","203 g","Apple A15 Bionic APL1W07","Cores : 6","62 GB","128 GB, 256 GB, 512 GB"," 6.7 in, OLED, 1284 x 2778 pixels, 24 bit"," Li-Ion"," iOS 16"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","eSIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]],["iPhone 14.",["71.5 x 147.5 x 7.85 mm","206 g","Apple A16 Bionic","Cores : 6"," 6 GB"," 128 GB, 256 GB, 512 GB, 1024 GB"," 6.1 in, OLED, 1179 x 2556 pixels, 24 bit"," Li-Ion"," iOS 16"," 8000 x 6000 pixels, 3840 x 2160 pixels, 60 fps","eSIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.3","  GPS, A-GPS, GLONASS, Galileo, QZSS"]],["iPhone 13 Pro Max.",["78.1 x 160.8 x 7.65 mm","240 g","Apple A15 Bionic APL1W07","Cores : 6 Cores : 5"," 6 GB"," 128 GB, 256 GB, 512 GB, 1024 GB","6.7 in, OLED, 1284 x 2778 pixels, 24 bit"," 4352 mAh, Li-Ion"," iOS 15"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","  5.0","  GPS, A-GPS, GLONASS, Galileo, QZS"]],["iPhone 13 Pro.",["71.5 x 146.7 x 7.65 mm ","204 g","Apple A15 Bionic APL1W07","Cores : 6 Cores : 5"," 6 GB"," 128 GB, 256 GB, 512 GB, 1024 GB"," 6.1 in, OLED, 1170 x 2532 pixels, 24 bit ","3095 mAh, Li-Ion"," iOS 15"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","  5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]],["iPhone 13.",["71.5 x 146.7 x 7.65 mm","174 g"," Apple A15 Bionic A PL1W07","Cores : 6 Cores : 4"," 4 GB"," 128 GB, 256 GB, 512 GB"," 6.1 in, OLED, 1170 x 2532 pixels, 24 bit"," 3227 mAh, Li-Ion"," iOS 15"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","  5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]],["iPhone 13 mini.",["64.2 x 131.5 x 7.65 mm","141 g","Apple A15 Bionic APL1W07","Cores : 6 Cores : 4"," 4 GB"," 128 GB, 256 GB, 512 GB","5.4 in, OLED, 1080 x 2340 pixels, 24 bit"," 2406 mAh, Li-Ion"," IOS 14.1"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","  5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]]]
iphone14PM=["77.6 x 160.7 x 7.85 mm","240 g","Apple A16 Bionic","Cores : 6","6 GB","128 GB, 256 GB, 512 GB, 1024 GB","6.7 in, OLED, 1290 x 2796 pixels, 24 bit ","Li-lon","iOS 16","8000 x 6000 pixels, 3840 x 2160 pixels, 60 fps","eSIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.3"," GPS, A-GPS, GLONASS, Galileo, QZSS"]
iphone14P=["71.5 x 147.5 x 7.85 mm","206 g","Apple A16 Bionic","Cores : 6"," 6 GB"," 128 GB, 256 GB, 512 GB, 1024 GB"," 6.1 in, OLED, 1179 x 2556 pixels, 24 bit"," Li-Ion"," iOS 16"," 8000 x 6000 pixels, 3840 x 2160 pixels, 60 fps","eSIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.3","  GPS, A-GPS, GLONASS, Galileo, QZSS"]
iphone14plus=["78.1 x 160.8 x 7.8 mm","203 g","Apple A15 Bionic APL1W07","Cores : 6","5 4 GB, 128 GB, 256 GB, 512 GB"," 6.7 in, OLED, 1284 x 2778 pixels, 24 bit"," Li-Ion"," iOS 16"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","eSIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]
iphone14=["71.5 x 147.5 x 7.85 mm","206 g","Apple A16 Bionic","Cores : 6"," 6 GB"," 128 GB, 256 GB, 512 GB, 1024 GB"," 6.1 in, OLED, 1179 x 2556 pixels, 24 bit"," Li-Ion"," iOS 16"," 8000 x 6000 pixels, 3840 x 2160 pixels, 60 fps","eSIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.3","  GPS, A-GPS, GLONASS, Galileo, QZSS"]
iphone13promax=["78.1 x 160.8 x 7.65 mm","240 g","Apple A15 Bionic APL1W07","Cores : 6 Cores : 5"," 6 GB"," 128 GB, 256 GB, 512 GB, 1024 GB","6.7 in, OLED, 1284 x 2778 pixels, 24 bit"," 4352 mAh, Li-Ion"," iOS 15"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","  5.0","  GPS, A-GPS, GLONASS, Galileo, QZS"]
iphone13pro=["71.5 x 146.7 x 7.65 mm ","204 g","Apple A15 Bionic APL1W07","Cores : 6 Cores : 5"," 6 GB"," 128 GB, 256 GB, 512 GB, 1024 GB"," 6.1 in, OLED, 1170 x 2532 pixels, 24 bit ","3095 mAh, Li-Ion"," iOS 15"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","  5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]
iphone13=["71.5 x 146.7 x 7.65 mm","174 g"," Apple A15 Bionic A PL1W07","Cores : 6 Cores : 4"," 4 GB"," 128 GB, 256 GB, 512 GB"," 6.1 in, OLED, 1170 x 2532 pixels, 24 bit"," 3227 mAh, Li-Ion iOS 15"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","  5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]
iphone13mini=["64.2 x 131.5 x 7.65 mm","141 g","Apple A15 Bionic APL1W07","Cores : 6 Cores : 4"," 4 GB"," 128 GB, 256 GB, 512 GB","5.4 in, OLED, 1080 x 2340 pixels, 24 bit"," 2406 mAh, Li-Ion"," IOS 14.1"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","  5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]
Tablets_iphone=[["iPad Pro",["280.6 x 214.9 x 6.4 mm","682 g","Apple M2","Cores : 10 Cores : 8","8 GB, 16 GB","128 GB, 256 GB, 512 GB, 1024 GB, 2048 GB","12.9 in, IPS, 2732 x 2048 pixels, 24 bit"," Li-Polymer"," iPadOS 16"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","No Sim"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","5.0","GPS, A-GPS, GLONASS, Galileo"]],["iPad Air",["247.6 x 178.5 x 6.1 mm","460 g","Apple M1","Cores : 8 Cores : 8","8 GB","64 GB, 256 GB","10.9 in, IPS, 2360 x 1640 pixels, 24 bit","Li-Ion"," iPadOS 14.5"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","No Sim"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]],["iPad",["248.6 x 179.5 x 7 mm","477 g","Apple A14 Bionic","Cores : 6 Cores : 4","4 GB"," 64 GB, 256 GB","10.9 in, IPS, 2360 x 1640 pixels, 24 bit"," Li-PQualcommolymer"," iPadOS 16"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","No Sim"," 5GHz, ac, Dual band, Wi-Fi Hotspot"," 5.0","  GPS, A-GPS, GLONASS"]],["iPad mini",["195.4 x 134.8 x 6.3 mm","297 g","Apple A15 Bionic","Cores : 6 Cores : 5","4 GB","64 GB, 256 GB","8.3 in, IPS, 1488 x 2266 pixels, 24 bit"," Li-Ion"," iPadOS 15"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","No Sim"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.0 "," GPS, A-GPS, GLONASS, Galileo, QZSS"]]]
ipad_pro=["280.6 x 214.9 x 6.4 mm","682 g","Apple M2","Cores : 10 Cores : 8","8 GB, 16 GB","128 GB, 256 GB, 512 GB, 1024 GB, 2048 GB","12.9 in, IPS, 2732 x 2048 pixels, 24 bit"," Li-Polymer"," iPadOS 16"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","No Sim"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax","5.0","GPS, A-GPS, GLONASS, Galileo"]
ipad_air=["247.6 x 178.5 x 6.1 mm","460 g","Apple M1","Cores : 8 Cores : 8","8 GB","64 GB, 256 GB","10.9 in, IPS, 2360 x 1640 pixels, 24 bit","Li-Ion"," iPadOS 14.5"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","No Sim"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.0","  GPS, A-GPS, GLONASS, Galileo, QZSS"]
ipad=["248.6 x 179.5 x 7 mm","477 g","Apple A14 Bionic","Cores : 6 Cores : 4","4 GB"," 64 GB, 256 GB","10.9 in, IPS, 2360 x 1640 pixels, 24 bit"," Li-PQualcommolymer"," iPadOS 16"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","No Sim"," 5GHz, ac, Dual band, Wi-Fi Hotspot"," 5.0","  GPS, A-GPS, GLONASS"]
ipad_mini=["195.4 x 134.8 x 6.3 mm","297 g","Apple A15 Bionic","Cores : 6 Cores : 5","4 GB","64 GB, 256 GB","8.3 in, IPS, 1488 x 2266 pixels, 24 bit"," Li-Ion"," iPadOS 15"," 4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","No Sim"," 5GHz, ac, Dual band, Wi-Fi Hotspot, ax"," 5.0 "," GPS, A-GPS, GLONASS, Galileo, QZSS"]
#================================================================================================================================================================================
#Samsung
#================================================================================================================================================================================
samsung_phones=[["Galaxy S22 Ultra",["77.9 x 163.3 x 8.9 mm","228 g","Samsung Exynos 2200","Cortex-A510"," 8 GB, 12 GB"," 128 GB, 256 GB, 512 GB, 1024 GB"," 6.8 in, Dynamic AMOLED 2X, 1440 x 3080 pixels, 24 bit","5000 mAh, Li-Polymer","Android 12"," 108 MP, 7680 x 4320 pixels, 24 fps","Nano-SIM ","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","5.2","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy S22+",["75.8 x 157.4 x 7.6 mm","195 g","Samsung Exynos 2200","Cortex-A510"," 8 GB"," 128 GB, 256 GB"," 6.6 in, Dynamic AMOLED 2X, 1080 x 2340 pixels, 24 bit"," 4500 mAh, Li-Polymer","Android 12"," 50 MP, 7680 x 4320 pixels, 24 fps","Nano-SIM ","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax"," 5.2 "," GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy S22",["70.6 x 146 x 7.6 mm","167 g","Samsung Exynos 2200","Cortex-A510"," 8 GB"," 128 GB, 256 GB"," 6.1 in, Dynamic AMOLED 2X, 1080 x 2340 pixels, 24 bit"," 3700 mAh, Li-Polymer","Android 12"," 50 MP, 7680 x 4320 pixels, 24 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","  5.2","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy S21 Ultra",["75.6 x 165.1 x 8.9 mm","229 g","Qualcomm Snapdragon 888","Cortex-A55","12 GB, 16 GB"," 128 GB, 256 GB, 512 GB"," 6.8 in, Dynamic AMOLED 2X, 1440 x 3200 pixels, 24 bit","5000 mAh, Li-Polymer"," Android 11 ","12000 x 9000 pixels, 7680 x 4320 pixels, 30 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax, Wi-Fi 6E"," 5.2","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy S21+",["75.6 x 161.5 x 7.8 mm","202 g","Qualcomm Snapdragon 888","Cortex-A55"," 8 GB"," 128 GB, 256 GB"," 6.7 in, Dynamic AMOLED, 1080 x 2400 pixels, 24 bit"," 4800 mAh, Li-Polymer"," Android 11"," 4032 x 3024 pixels, 7680 x 4320 pixels, 30 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax, Wi-Fi 6E","5.2"," GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy S21",["74.5 x 155.7 x 7.9 mm","177 g","Qualcomm Snapdragon 888","Cortex-A55","6 GB, 8 GB"," 128 GB, 256 GB"," 6.4 in, Dynamic AMOLED 2X, 1080 x 2400 pixels, 24 bit"," 4500 mAh, Li-Polymer","Android 12 ","4032 x 3024 pixels, 7680 x 4320 pixels, 30 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax"," 5.2","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy Z Flip4",["71.9 x 165.2 x 6.9 mm","187 g","Qualcomm Snapdragon 8+ Gen 1","Cortex-A510 "," 8 GB"," 256 GB , 512 GB"," 6.7 in, Dynamic AMOLED, 1080 x 2640 pixels, 24 bit"," 3700 mAh, Li-Polymer"," Android 12","4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, ax"," 5.1","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy Z Fold4",["130.1 x 155.1 x 6.3 mm","263 g","Qualcomm Snapdragon 8+ Gen 1","Cortex-A510","12 GB","256 GB, 512 GB, 1024 GB","7.6 in, Dynamic AMOLED 2X, 2208 x 1768 pixels, 24 bit","4400 mAh, Li-Polymer","Android 12L",": 8190 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy Note20",["75.2 x 161.6 x 8.3 mm","192 g","Qualcomm Snapdragon 865 Plus","Kryo 485"," 8 GB"," 256 GB Memory cards : microSD, microSDHC, microSDXC"," 6.7 in, Super AMOLED Plus, 1080 x 2400 pixels, 24 bit","4300 mAh, Li-Polymer","Android 10"," 4032 x 3024 pixels, 7680 x 4320 pixels, 24 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","  5.0","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]]]
Tablets_samsung=[["Galaxy Tab S8 Ultra",["285 x 185 x 5.7 mm","597 g","Qualcomm Snapdragon 8 Gen 1","Cortex-A510","8 GB, 12 GB, 16 GB","128 GB, 256 GB, 512 GB","14.6 in, AMOLED, 2960 x 1848 pixels, 24 bit","11200 mAh, Li-Polymer","Android 12","4160 x 3120 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Direct, ax","5.2","A-GPS"]],["Galaxy Tab S8+",["285 x 185 x 5.7 mm","597 g","Qualcomm Snapdragon 8 Gen 1","Cortex-A510","8 GB","128 GB, 256 GB","12.4 in, AMOLED, 2800 x 1752 pixels, 24 bit","10090 mAh, Li-Polymer","Android 12","4160 x 3120 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Direct, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo"]],["Galaxy Tab S8",["253.8 x 165.4 x 6.3 mm","507 g","Qualcomm Snapdragon 8 Gen 1","Cortex-A510","8 GB","128 GB, 256 GB","11 in, AMOLED, 2560 x 1600 pixels, 24 bit","8000 mAh, Li-Polymer","Android 12","4160 x 3120 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Direct, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo"]]]
Galaxy_S22_Ultra=["77.9 x 163.3 x 8.9 mm","228 g","Samsung Exynos 2200","Cortex-A510"," 8 GB, 12 GB"," 128 GB, 256 GB, 512 GB, 1024 GB"," 6.8 in, Dynamic AMOLED 2X, 1440 x 3080 pixels, 24 bit","5000 mAh, Li-Polymer","Android 12"," 108 MP, 7680 x 4320 pixels, 24 fps","Nano-SIM ","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","5.2","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_S22_plus=["75.8 x 157.4 x 7.6 mm","195 g","Samsung Exynos 2200","Cortex-A510"," 8 GB"," 128 GB, 256 GB"," 6.6 in, Dynamic AMOLED 2X, 1080 x 2340 pixels, 24 bit"," 4500 mAh, Li-Polymer","Android 12"," 50 MP, 7680 x 4320 pixels, 24 fps","Nano-SIM ","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax"," 5.2 "," GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_S22=["70.6 x 146 x 7.6 mm","167 g","Samsung Exynos 2200","Cortex-A510"," 8 GB"," 128 GB, 256 GB"," 6.1 in, Dynamic AMOLED 2X, 1080 x 2340 pixels, 24 bit"," 3700 mAh, Li-Polymer","Android 12"," 50 MP, 7680 x 4320 pixels, 24 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","  5.2","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_S21_Ultra=["75.6 x 165.1 x 8.9 mm","229 g","Qualcomm Snapdragon 888","Cortex-A55","12 GB, 16 GB"," 128 GB, 256 GB, 512 GB"," 6.8 in, Dynamic AMOLED 2X, 1440 x 3200 pixels, 24 bit","5000 mAh, Li-Polymer"," Android 11 ","12000 x 9000 pixels, 7680 x 4320 pixels, 30 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax, Wi-Fi 6E"," 5.2","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_S21_plus=["75.6 x 161.5 x 7.8 mm","202 g","Qualcomm Snapdragon 888","Cortex-A55"," 8 GB"," 128 GB, 256 GB"," 6.7 in, Dynamic AMOLED, 1080 x 2400 pixels, 24 bit"," 4800 mAh, Li-Polymer"," Android 11"," 4032 x 3024 pixels, 7680 x 4320 pixels, 30 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax, Wi-Fi 6E","5.2"," GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_S21=["74.5 x 155.7 x 7.9 mm","177 g","Qualcomm Snapdragon 888","Cortex-A55","6 GB, 8 GB"," 128 GB, 256 GB"," 6.4 in, Dynamic AMOLED 2X, 1080 x 2400 pixels, 24 bit"," 4500 mAh, Li-Polymer","Android 12 ","4032 x 3024 pixels, 7680 x 4320 pixels, 30 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax"," 5.2","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_Z_Flip4=["71.9 x 165.2 x 6.9 mm","187 g","Qualcomm Snapdragon 8+ Gen 1","Cortex-A510 "," 8 GB"," 256 GB , 512 GB"," 6.7 in, Dynamic AMOLED, 1080 x 2640 pixels, 24 bit"," 3700 mAh, Li-Polymer"," Android 12","4032 x 3024 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, ax"," 5.1","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_Z_Fold4=["130.1 x 155.1 x 6.3 mm","263 g","Qualcomm Snapdragon 8+ Gen 1","Cortex-A510","12 GB","256 GB, 512 GB, 1024 GB","7.6 in, Dynamic AMOLED 2X, 2208 x 1768 pixels, 24 bit","4400 mAh, Li-Polymer","Android 12L",": 8190 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_Note20=["75.2 x 161.6 x 8.3 mm","192 g","Qualcomm Snapdragon 865 Plus","Kryo 485"," 8 GB"," 256 GB"," 6.7 in, Super AMOLED Plus, 1080 x 2400 pixels, 24 bit","4300 mAh, Li-Polymer","Android 10"," 4032 x 3024 pixels, 7680 x 4320 pixels, 24 fps","Nano-SIM"," 5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","  5.0","  GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_Tab_s8_ultra=["285 x 185 x 5.7 mm","597 g","Qualcomm Snapdragon 8 Gen 1","Cortex-A510","8 GB, 12 GB, 16 GB","128 GB, 256 GB, 512 GB","14.6 in, AMOLED, 2960 x 1848 pixels, 24 bit","11200 mAh, Li-Polymer","Android 12","4160 x 3120 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Direct, ax","5.2","A-GPS"]
Galaxy_Tab_S8_plus=["285 x 185 x 5.7 mm","597 g","Qualcomm Snapdragon 8 Gen 1","Cortex-A510","8 GB","128 GB, 256 GB","12.4 in, AMOLED, 2800 x 1752 pixels, 24 bit","10090 mAh, Li-Polymer","Android 12","4160 x 3120 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Direct, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo"]
Galaxy_Tab_S8=["253.8 x 165.4 x 6.3 mm","507 g","Qualcomm Snapdragon 8 Gen 1","Cortex-A510","8 GB","128 GB, 256 GB","11 in, AMOLED, 2560 x 1600 pixels, 24 bit","8000 mAh, Li-Polymer","Android 12","4160 x 3120 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Direct, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo"]
#=======================================================================================================================================================================================================================
# Huawei:
#=======================================================================================================================================================================================================================
huawei_phones=[["Mate 50 Pro",["75.5 x 162.1 x 8.5 mm","205 g","Qualcomm Snapdragon 8+ Gen 1","Cortex-X2,Cortex-A710,Cortex-A510"," 8 GB, 12 GB","256 GB, 512 GB"," 6.74 in, OLED, 1212 x 2616 pixels, 30 bit","4700 mAh, Li-Polymer","HarmonyOS 3.0","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS,Galileo,BeiDou"]],["Mate 50",["76.1 x 161.5 x 7.98 mm","206 g","Qualcomm Snapdragon 8+ Gen 1","Cortex-X2,Cortex-A710,Cortex-A510","8 GB","128 GB, 256 GB, 512 GB","6.7 in, OLED, 1224 x 2700 pixels, 30 bit","4460 mAh, Li-Polymer","HarmonyOS 3.0","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS,Galileo,BeiDou"]],["Mate 40 Pro+",["75.5 x 162.9 x 8.8 mm","230 g","Huawei HiSilicon KIRIN 9000","Cortex-A77,Cortex-A55","12 GB","256 GB"," 6.76 in, Flex OLED, 1344 x 2772 pixels, 24 bit","4400 mAh, Li-Polymer","Android 10 ","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS,Galileo,BeiDou"]],["Mate 40 Pro",["75.5 x 162.9 x 9.1 mm","212 g","Huawei HiSilicon KIRIN 9000","Cortex-A77,Cortex-A55","8 GB","128 GB, 256 GB, 512 GB","6.76 in, Flex OLED, 1344 x 2772 pixels, 24 bit","4400 mAh, Li-Polymer","Android 10","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS,Galileo,BeiDou"]],["Mate 40",["72.5 x 158.6 x 8.8 mm","188 g","Huawei HiSilicon KIRIN 9000E","Cortex-A77,Cortex-A55","8 GB","128 GB, 256 GB","6.5 in, Flex OLED, 1080 x 2376 pixels, 24 bit","4200 mAh, Li-Polymer","Android 10","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2 ","GPS,Galileo,BeiDou"]],["Mate Xs 2",["75.5 x 156.5 x 11.1 mm"," 257 g","Qualcomm Snapdragon 888","Cortex-A55"," 8 GB, 12 GB","256 GB, 512 GB","6.5 in, OLED, 1176 x 2480 pixels, 30 bit","4880 mAh, Li-Polymer","Harmony OS 2"," 8190 x 6120 pixels, 3840 x 2160 pixels, 30 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct","5.2","GPS,Galileo,BeiDou"]],["Mate X2",["74.6 x 161.8 x 14.7 mm","295 g","Huawei HiSilicon KIRIN 9000","Cortex-A55","8 GB","256 GB, 512 GB","6.45 in, OLED, 1160 x 2700 pixels, 24 bit","4500 mAh, Li-Polymer","Android 10","8192 x 6144 pixels, 3840 x 2160 pixels, 30 fps","Nano-SIM, Nano-SIM / NMSD","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, ax","5.2","GPS,Galileo,BeiDou"]]]
Mate_50_Pro=["75.5 x 162.1 x 8.5 mm","205 g","Qualcomm Snapdragon 8+ Gen 1","Cortex-X2,Cortex-A710,Cortex-A510"," 8 GB, 12 GB","256 GB, 512 GB"," 6.74 in, OLED, 1212 x 2616 pixels, 30 bit","4700 mAh, Li-Polymer","HarmonyOS 3.0","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS,Galileo,BeiDou"]
Mate_50=["76.1 x 161.5 x 7.98 mm","206 g","Qualcomm Snapdragon 8+ Gen 1","Cortex-X2,Cortex-A710,Cortex-A510","8 GB","128 GB, 256 GB, 512 GB","6.7 in, OLED, 1224 x 2700 pixels, 30 bit","4460 mAh, Li-Polymer","HarmonyOS 3.0","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS,Galileo,BeiDou"]
Mate_40_Pro_plus=["75.5 x 162.9 x 8.8 mm","230 g","Huawei HiSilicon KIRIN 9000","Cortex-A77,Cortex-A55","12 GB","256 GB"," 6.76 in, Flex OLED, 1344 x 2772 pixels, 24 bit","4400 mAh, Li-Polymer","Android 10 ","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS,Galileo,BeiDou"]
Mate_40_Pro=["75.5 x 162.9 x 9.1 mm","212 g","Huawei HiSilicon KIRIN 9000","Cortex-A77,Cortex-A55","8 GB","128 GB, 256 GB, 512 GB","6.76 in, Flex OLED, 1344 x 2772 pixels, 24 bit","4400 mAh, Li-Polymer","Android 10","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2","GPS,Galileo,BeiDou"]
Mate_40=["72.5 x 158.6 x 8.8 mm","188 g","Huawei HiSilicon KIRIN 9000E","Cortex-A77,Cortex-A55","8 GB","128 GB, 256 GB","6.5 in, Flex OLED, 1080 x 2376 pixels, 24 bit","4200 mAh, Li-Polymer","Android 10","8192 x 6144 pixels, 3840 x 2160 pixels, 60 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display","5.2 ","GPS,Galileo,BeiDou"]
Mate_Xs_2=["75.5 x 156.5 x 11.1 mm"," 257 g","Qualcomm Snapdragon 888","Cortex-A55"," 8 GB, 12 GB","256 GB, 512 GB","6.5 in, OLED, 1176 x 2480 pixels, 30 bit","4880 mAh, Li-Polymer","Harmony OS 2"," 8190 x 6120 pixels, 3840 x 2160 pixels, 30 fps","Nano-SIM, Nano-SIM/NMSD","Dual band, Wi-Fi Hotspot, Wi-Fi Direct","5.2","GPS,Galileo,BeiDou"]
Mate_X2=["74.6 x 161.8 x 14.7 mm","295 g","Huawei HiSilicon KIRIN 9000","Cortex-A55","8 GB","256 GB, 512 GB","6.45 in, OLED, 1160 x 2700 pixels, 24 bit","4500 mAh, Li-Polymer","Android 10","8192 x 6144 pixels, 3840 x 2160 pixels, 30 fps","Nano-SIM, Nano-SIM / NMSD","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, ax","5.2","GPS,Galileo,BeiDou"]
#Google
google_phones=[["Pixel 7 Pro",["76.6 x 162.9 x 8.9 mm","212 g","Google Tensor G2","ARM Cortex-A55","12 GB","128 GB, 256 GB, 512 GB","6.71 in, AMOLED, 1440 x 3120 pixels, 24 bit","5000 mAh, Li-Polymer","Android 13","50 MP, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo, QZSS"]],["Pixel 7",["73.2 x 155.6 x 8.7 mm","197 g","Google Tensor G2","ARM Cortex-A55","8 GB","128 GB, 256 GB","6.3 in, AMOLED, 1080 x 2400 pixels, 24 bit","4355 mAh, Li-Polymer","Android 13","50 MP, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo, QZSS"]],["Pixel 6a",["74.8 x 158.6 x 8.9 mm","207 g","Google Tensor","ARM Cortex-A55","8 GB","128 GB, 256 GB","6.4 in, AMOLED, 1080 x 2340 pixels, 24 bit","4600 mAh, Li-Polymer","Android 12","50 MP, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo, QZSS"]]]
Pixel_7_Pro=["76.6 x 162.9 x 8.9 mm","212 g","Google Tensor G2","ARM Cortex-A55","12 GB","128 GB, 256 GB, 512 GB","6.71 in, AMOLED, 1440 x 3120 pixels, 24 bit","5000 mAh, Li-Polymer","Android 13","50 MP, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo, QZSS"]
Pixel_7=["73.2 x 155.6 x 8.7 mm","197 g","Google Tensor G2","ARM Cortex-A55","8 GB","128 GB, 256 GB","6.3 in, AMOLED, 1080 x 2400 pixels, 24 bit","4355 mAh, Li-Polymer","Android 13","50 MP, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo, QZSS"]
Pixel_6=["74.8 x 158.6 x 8.9 mm","207 g","Google Tensor","ARM Cortex-A55","8 GB","128 GB, 256 GB","6.4 in, AMOLED, 1080 x 2340 pixels, 24 bit","4600 mAh, Li-Polymer","Android 12","50 MP, 3840 x 2160 pixels, 60 fps","Nano-SIM","5GHz, ac, Dual band, Wi-Fi Hotspot, Wi-Fi Direct, Wi-Fi Display, ax","5.2","GPS, A-GPS, GLONASS, BeiDou, Galileo, QZSS"]

#laptops
#lenovo
laptop_lenovo=[["Legion 7i Gen 7 (16” Intel) Gaming Laptop",["358.1 x 263.5 x 19.4 mm","2.5 kg","Intel Core i7-12800HX","GeForce RTX 3070 Ti Mobile 8 GB","16 GB","512 GB","2560 x 1600 (165Hz)","99.9 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No GPS"]],["Yoga 9i (14” Intel) 2 in 1 Laptop",["318 x 230 x 15.25 mm","1.4 kg","Intel Core i7-1260P","Intel Iris Xe","16 GB","1 TB","3840 x 2400","75 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No GPS"]],["ThinkPad X1 Extreme Gen 4 (16” Intel) Laptop",["360mm x 254mm x 18mm","1.8 kg","Intel Core i7-11800H","GeForce RTX 3060 Mobile 6 GB","16 GB","512 GB","2560 x 1600","90 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No GPS"]]]
legion_7i_Gen_7_Intel_Gaming_Laptop=["358.1 x 263.5 x 19.4 mm","2.5 kg","Intel Core i7-12800HX","GeForce RTX 3070 Ti Mobile 8 GB","16 GB","512 GB","2560 x 1600 (165Hz)","99.9 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No GPS"]
Yoga_9i_Intel_2_in_1_Laptop=["318 x 230 x 15.25 mm","1.4 kg","Intel Core i7-1260P","Intel Iris Xe","16 GB","1 TB","3840 x 2400","75 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No GPS"]
ThinkPad_3X1_3Extreme_3Gen_34_3_Intel_Laptop=["360mm x 254mm x 18mm","1.8 kg","Intel Core i7-11800H","GeForce RTX 3060 Mobile 6 GB","16 GB","512 GB","2560 x 1600","90 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No GPS"]
#Hp
laptop_HP=[["OMEN 16 2022 (INTEL)",["369 x 248 x 23 mm","2.29 kg","Intel Core i7-12700H","GeForce RTX 3070 Mobile 8GB","16 GB","1 TB","1920 x 1080 (144Hz)","84 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No Gps"]],["HP Spectre x360 13.5",["307 x 195 x 17 mm","1.3 kg","Intel Core i5-1135G7","Intel Iris Xe","16 GB","512 GB","1920 x 1080","60 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No GPS"]],["HP Envy x360 15.6(Intel)",["306.5 x 194.5 x 16.5 mm","1.3 kg","Intel Core i7-1165G7","Intel Iris Xe","16 GB","512 GB","1920 x 1080","51 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No Gps"]]]
omen_16_2022_INTEL=["369 x 248 x 23 mm","2.29 kg","Intel Core i7-12700H","GeForce RTX 3070 Mobile 8GB","16 GB","1 TB","1920 x 1080 (144Hz)","84 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No Gps"]
HP_Spectre_x360=["307 x 195 x 17 mm","1.3 kg","Intel Core i5-1135G7","Intel Iris Xe","16 GB","512 GB","1920 x 1080","60 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No GPS"]
HP_Envy_x360_Intel=["306.5 x 194.5 x 16.5 mm","1.3 kg","Intel Core i7-1165G7","Intel Iris Xe","16 GB","512 GB","1920 x 1080","51 Wh","Windows 11","1920 x 1080","No Sim","6E","5.2","No Gps"]

#desktops
pc_lenovo=[["Legion Tower 7i Gen 7 with RTX 3080",["Intel Core i9-12900K","RTX 3080","32 GB"]]]
pc_hp=[["OMEN 45L (INTEL)",["Intel Core i7-12700K","RTX 3060","16 GB"]]]
Legion_Tower = ["Intel Core i9-12900K","RTX 3080","32 GB"]
Omen_45L = ["Intel Core i7-12700K","RTX 3060","16 GB"]

iphone_cat = [["iPhone 14",["iPhone 14 Pro Max.", "iPhone 14 Pro.", "iPhone 14 Plus.", "iPhone 14."],["Space Black.", "Silver.", "Gold.", "Deep Purple."],["128GB.", "256GB.", "512GB."]],["iPhone 13",["iPhone 13 Pro Max.", "iPhone 13 Pro.", "iPhone 13.", "iPhone 13 mini."],["Graphite.", "Gold.", "Silver.", "Sierra Blue.", "Alpine Green."],["128GB.", "256GB.", "512GB"]]]
samsung = [["Galaxy S22",["Galaxy S22 Ultra.","Galaxy S22+.","Galaxy S22."],["Phantom White.","Phantom Black.","Green.","Graphite.","Pink Gold.","Sky Blue.","Violet."],["128GB.","256GB."]],["Galaxy S21",["Galaxy S21 Ultra.","Galaxy S21+.","Galaxy S21."],["Phantom Violet.","Phantom Pink.","Phantom White.","Phantom Gray."],["128GB","256GB","512GB"]],["Galaxy Z Flip4",["Galaxy Z Flip4"],["Bora Purple.","Blue.","Pink Gold.","Graphite."],["128GB.","256GB.","512GB."]],["Galaxy Z Fold4",["Galaxy Z Fold4"],["Phantom Black.","Graygreen.","Beige.","Burgundy."],["256GB","512GB"]],["Galaxy Note20",["Galaxy Note20"],["Mystic Black.","Mystic Bronze.","Mystic White."],["256GB."]]]
huawei = [["Mate50",["Mate50 Pro.","Mate50."],["Olive Green.","White.","Green.","Silver.","Gold.","Black."],["256GB.", "512GB."]],["Mate40",["Mate40 Pro+.","Mate40 Pro.","Mate40"],["Mystic Silver.","White.","Black.","Green.","Yellow."],["128GB.","256GB.","512GB."]],["Mate X",["Mate Xs 2.","Mate X2."],["Titanium Gray.","Diamond Black.","Black.","Midnight Blue.","Mocha Brown."],["128GB","256GB","512GB"]]]
google = [["Pixel 7",["Pixel 7 Pro.","Pixel 7."],["Obsidian.", "Snow.","Lemongrass."],["128GB","256GB"]],["Pixel6",["Pixel6a."],["Sage.","Chalk.","Charcoal."],["128GB."]]]
ipad_cat = [["ipad pro",["iPad Pro."],["Space Grey.", "Silver."],["128GB.", "256GB.", "512GB", "1TB.","2TB."]],["ipad air",["iPad Air."],["Space Grey.","Pink.","Purple.","Blue.","Starlight."],["64GB.","256GB."]],["ipad",["iPad."],["Blue.","Pink.", "Yellow.","Silver."],["64GB.", "256GB."]],["ipad mini",["iPad Mini."],["Space Grey.","Pink.","Purple.","Starlight."],["64GB.","256GB."]]]
stablet = [["galaxy tab s8",["Galaxy Tab S8 Ultra.","Galaxy Tab S8+.","Galaxy Tab S8"],["Graphite.","Silver.","Pink Gold."],["128GB.", "256GB."]]]
lenovolap = [["legion",["Legion 7i Gen 7 (16” Intel) Gaming Laptop."]],["yoga",["Yoga 9i (14” Intel) 2 in 1 Laptop"]],["ThinkPad",["ThinkPad."]]]
hplap = [["Omen",["OMEN 16 2022 (INTEL)"]],["spectre",["HP Spectre x360 13.5"]],["Envy",["HP Envy x360 15.6 (Intel)."]]]
LenovoPC = [["legion tower",["Legion Tower 7i Gen 7 with RTX 3080"]]]
HPPC= [["omen",["OMEN 45L (INTEL)"]]]

phone_manf = ["Apple.", "Samsung.", "Huawei.", "Google."]

tablet_manf =["Apple.", "Samsung."]

laptop_manf = ["Lenovo.", "HP."]

PC_manf = ["Lenovo.", "HP."]

iphone_prices= [[1099.99,1199.99,1399.99],[999.99,1099.99,1299.99],[899.99,999.99,1199.99],[799.99,899.99,1099.99],[1099.99,1199.99,1399.99],[999.99,1099.99,1299.99],[799.99,899.99,999.99],[699.99,799.99,899.99]]
samsung_phone_prices= [[974.99,1074.99,1174.99],[849.99,899.99],[724.99,774.99],[874.99,974.99,1074.99],[749.99,799.99,849.99],[624.99,674.99,724.99],[999.99,1059.99,1179.99],[1799.99,1999.99,2159.99],[1299.99]]
huawei_phone_prices= [[1819.99,1919.99],[1149.99,1249.99],[1699.99,1749.99,1849.99],[1649.99,1699.99,1749.99],[999,1049.99,1099.99],[2299.99,2399.99,2499.99],[4299.99,4399.99,4499.99]]
google_phone_prices=[[849.99,999.99],[659.99,719.99],[319.99]]
ipad_prices=[[799.99,899.99,1099.99,1499.99,1899.99],[599.99,749.99],[449.99,599.99],[499.99,649.99]]
samsung_tablet_prices= [[1149.99,1199.99],[1099.99,1149.99],[899.99,849.99]]
lenovo_laptop_prices= [1949.99,974.99,1449.99]
hp_laptop_prices=[1299.99,1249.99,1099.99]
lenovo_pc_prices=[2239.99]
hp_pc_prices=[1549.99]
"""
 * @brief 
 * @param 
 * @retval 
 * @req/@task
 """






application_info=["Full Name","Job Applied","Address","Phone Number","Email","National Identification Number (Raqam Qawmi)","Employment Desired","Worked for us before?","Explain (work)","Convicted Before?","Explain (convicted)","High School","HS Start Date","HS End date","HS Graduate?","College","College Start Date","College End Date","College Graduate?","Degree"]
jobs=["Delivery Driver","Store Clerk","Technical Support","Office Worker"]
employment_desired=["Full-time", "Part-time","Seasonal"]

def iphone_view_or_compare(apple_specs):
    View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(iphone[apple_specs-1][0])))
    if View_or_Compare==1:
        for x in range(len(Phone_speclist)):
            print("{}) {}: {}".format(x+1,Phone_speclist[x],iphone[apple_specs-1][1][x]))
    return View_or_Compare      
def samsung_view_or_compare(samsung_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(samsung_phones[samsung_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Phone_speclist)):
                        print("{}) {}: {}".format(x+1,Phone_speclist[x],samsung_phones[samsung_specs-1][1][x]))
                return View_or_Compare
def hauwei_view_or_compare(huawei_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(huawei_phones[huawei_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Phone_speclist)):
                        print("{}) {}: {}".format(x+1,Phone_speclist[x],huawei_phones[huawei_specs-1][1][x]))
                return View_or_Compare
def google_view_or_compare(google_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(google_phones[google_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Phone_speclist)):
                        print("{}) {}: {}".format(x+1,Phone_speclist[x],google_phones[google_specs-1][1][x]))
                return View_or_Compare
def ipad_view_or_compare(ipad_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(Tablets_iphone[ipad_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Phone_speclist)):
                        print("{}) {}: {}".format(x+1,Phone_speclist[x],Tablets_iphone[ipad_specs-1][1][x]))
                return View_or_Compare
def samsung_tablet_view_or_compare(samsung_tablet_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(Tablets_samsung[samsung_tablet_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Phone_speclist)):
                        print("{}) {}: {}".format(x+1,Phone_speclist[x],Tablets_samsung[-1][1][x]))
                return View_or_Compare
def lenovo_laptop_view_or_compare(lenovo_laptop_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(laptop_lenovo[lenovo_laptop_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Laptop_speclist)):
                        print("{}) {}: {}".format(x+1,Laptop_speclist[x],laptop_lenovo[-1][1][x]))
                return View_or_Compare
def hp_laptop_view_or_compare(hp_laptop_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(laptop_HP[hp_laptop_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Laptop_speclist)):
                        print("{}) {}: {}".format(x+1,Laptop_speclist[x],laptop_HP[-1][1][x]))
                return View_or_Compare
def lenovo_pc_view_or_compare(lenovo_pc_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(pc_lenovo[lenovo_pc_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Desktop_speclist)):
                        print("{}) {}: {}".format(x+1,Desktop_speclist[x],pc_lenovo[-1][1][x]))
                return View_or_Compare
def hp_pc_view_or_compare(hp_pc_specs):
                View_or_Compare=int(input("""do you want to view the specs of {} or compare it with another device:
1) View 
2) Compare
""".format(pc_hp[hp_pc_specs-1][0])))
                if View_or_Compare==1:
                    for x in range(len(Desktop_speclist)):
                        print("{}) {}: {}".format(x+1,Desktop_speclist[x],pc_hp[-1][1][x]))
                return View_or_Compare
def featured_items():
    featured_items_small = random.sample(allitems,5)
    print("""Here are some featured items:\n1){}\n2){}\n3){}\n4){}\n5){}\nDo you want to add any of these item to cart? (Y/N)""".format(featured_items_small[0],featured_items_small[1],featured_items_small[2],featured_items_small[3],featured_items_small[4]))
    add_to_cart_fi = input().upper()
    if add_to_cart_fi == "Y":
        choice_to_cart = int(input("Choose an item to add to cart: "))
        featured_choice = featured_items_small[choice_to_cart-1]
        index= allitems.index(featured_choice)
        if index < 28:
            device_type = 1
            if index < 8:
                manf = 1
            elif index < 17:
                manf = 2
            elif index < 24:
                manf = 3
            elif index < 27:
                manf = 4
        elif index < 34:
            device_type = 2
            if index < 31:
                manf = 1
            elif index < 34:
                manf = 2
        elif index < 40:
            device_type = 3
            if index < 37:
                manf = 1
            elif index < 40:
                manf = 2
        else:
            device_type = 4
            if index == 40:
                manf = 1
            elif index == 41:
                manf = 1
    return device_type,manf,featured_choice
#device spesificaitions
#Second choices for compare 
def second_phone_choice():
    smartphone_specs=int(input("""Select a device manufacturer:
1)	Apple.
2)	Samsung.
3)	Huawei.
4)	Google.
""")) 
    if smartphone_specs==1:
        second_manifacturer= iphone.copy()
        print("Which Apple phone would you like to view?")
        n=1
        for x in iphone:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_phone=int(input("Enter your choice: "))-1
        
    if smartphone_specs==2:
        second_manifacturer= samsung_phones.copy()
        print("Which Samsung phone would you like to view?")
        n=1
        for x in samsung_phones:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_phone=int(input("Enter your choice: "))-1

        
    if smartphone_specs==3:
        second_manifacturer= huawei_phones.copy()
        print("Which Huawei phone would you like to view?")
        n=1
        for x in huawei_phones:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_phone=int(input("Enter your choice: "))-1

    if smartphone_specs==4:
        second_manifacturer= google_phones.copy()
        print("Which Google phone would you like to view?")
        n=1
        for x in google_phones:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_phone=int(input("Enter your choice: "))-1

    return second_manifacturer,second_phone
def second_tablet_choice():
    tablet_specs=int(input("""Here's a list of the tablet manufacturers: (Please choose an option)
    1) Apple
    2) Samsung
    """))
    if tablet_specs==1:
        second_manifacturer= Tablets_iphone.copy()
        print("Which iPad would you like to view?")
        n=1
        for x in Tablets_iphone:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_tablet=int(input("Enter your choice: "))-1
        

    if tablet_specs==2:
        second_manifacturer= Tablets_samsung.copy()
        print("Which Samsung Tablet would you like to view?")
        n=1
        for x in Tablets_samsung:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_tablet=int(input("Enter your choice: "))-1
    
    return second_manifacturer,second_tablet

def second_laptop_choice():
    laptop_specs=int(input("""Here's a list of the laptop manufacturers: (Please choose an option)
1) Lenovo
2) Hp
"""))
    if laptop_specs==1:
        second_manifacturer=laptop_lenovo.copy()
        print("Which Lenovo laptop would you like to view?")
        n=1
        for x in laptop_lenovo:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_laptop=int(input("Enter your choice: "))-1
    if laptop_specs==2:
        second_manifacturer= laptop_HP.copy()
        print("Which Hp laptop would you like to view?")
        n=1
        for x in laptop_HP:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_laptop=int(input("Enter your choice: "))-1
        
    return second_manifacturer,second_laptop

def second_desktop_choice():
    pc_specs=int(input("""Here's a list of the PC manufacturers: (Please choose an option)
1) Lenovo
2) Hp
"""))
    if pc_specs==1:
        second_manifacturer= pc_lenovo.copy()
        print("Which Lenovo PC would you like to view?")
        n=1
        for x in pc_lenovo:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_PC=int(input("Enter your choice: "))-1
    if pc_specs==2:
        second_manifacturer=pc_hp.copy()
        print("Which Hp PC would you like to view?")
        n=1
        for x in pc_hp:
            print("{})   {}".format(n,x[0]))
            n+=1
        second_PC=int(input("Enter your choice: "))-1

    return second_manifacturer,second_PC

#Compare function
def compare_devices(device_specs,manf1,phone1,manf2,phone2):
    datalist=[]
    for x in range(len(device_specs)):
        datalist.append([device_specs[x],manf1[phone1][1][x],manf2[phone2][1][x]])
    print(tabulate(datalist, headers=["Specifications",manf1[phone1][0],manf2[phone2][0]], tablefmt="grid"))
    datalist.clear()


def sdevice(cust_need, cust_device):
    if cust_need == 1:
        cust_device = int(input("""Great! What type of device are you looking for? Please choose an option.
        1)	Smartphone.
        2)	Tablet.
        3)	Laptop.
        4)	Desktop PC.
        """))

    return cust_device

"""
 * @brief 
 * @param 
 * @retval 
 * @req/@task
 """
def sphone_manf(cust_device, cust_manf):
    if cust_device == 1:
        print("Here's a list of the phone manufacturers")
        n=1
        for x in phone_manf:
            print("{})   {}".format(n,x))
            n+=1

    cust_manf = int(input("Enter your choice: "))

    while cust_manf >4:
        print("Invalid input (please choose one of the given options)")
        cust_manf = int(input("Enter your choice: "))
    
    return cust_manf
     
def stablet_manf(cust_device, cust_manf_tablet):
    if cust_device == 2:
        print("Here's a list of the tablet manufacturers")
        n=1
        for x in tablet_manf:
            print("{})   {}".format(n,x))
            n+=1

    cust_manf_tablet = int(input("Enter your choice: "))
        
    return cust_manf_tablet

def slaptop_manf(cust_device, cust_manf_laptop):
    if cust_device == 3:
        print("Here's a list of the laptop manufacturers")
        n=1
        for x in laptop_manf:
            print("{})   {}".format(n,x))
            n+=1

    cust_manf_laptop = int(input("Enter your choice: "))
     
    return cust_manf_laptop

def sPC_manf(cust_device, cust_manf_PC):
    if cust_device == 4:
        print("Here's a list of the Desktop manufacturers")
        n=1
        for x in PC_manf:
            print("{})   {}".format(n,x))
            n+=1

    cust_manf_PC = int(input("Enter your choice: "))
    
    return cust_manf_PC


def sphone_apple(cust_manf, iphone_model):
    if cust_manf == 1:
        print("Which Apple phone would you like to purchase?")
        n=1
        for x in iphone_cat[0][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=5
        for x in iphone_cat[1][1]:
            print("{})   {}".format(n,x))
            n+=1

    iphone_model = int(input("Enter your choice: "))
    
    

    
    return iphone_model

def sphone_samsung(cust_manf, samsung_model):
    if cust_manf ==2:
        print("Which Samsung phone would you like to purchase?")
        n=1
        for x in samsung[0][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=4
        for x in samsung[1][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=7
        for x in samsung[2][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=8
        for x in samsung[3][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=9
        for x in samsung[4][1]:
            print("{})   {}".format(n,x))
            n+=1

    samsung_model = int(input("Enter your choice: "))

    return samsung_model

def sphone_huawei(cust_manf, huawei_model):
    if cust_manf ==3:
        print("Which Huawei phone would you like to purchase?")
        n=1
        for x in huawei[0][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=3
        for x in huawei[1][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=6
        for x in huawei[2][1]:
            print("{})   {}".format(n,x))
            n+=1



    huawei_model = int(input("Enter your choice: "))
    


    return huawei_model


def sphone_google(cust_manf, google_model):
    if cust_manf ==4:
        print("Which Google phone would you like to purchase?")
        n=1
        for x in google[0][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=3
        for x in google[1][1]:
            print("{})   {}".format(n,x))
            n+=1


    google_model = int(input("Enter your choice: "))
    


    return google_model

def stablet_apple(cust_manf_tablet, ipad_model):
    if cust_manf_tablet ==1:
        print("Which iPad would you like to purchase?")
        n=1
        for x in ipad_cat[0][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=2
        for x in ipad_cat[1][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=3
        for x in ipad_cat[2][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=4
        for x in ipad_cat[3][1]:
            print("{})   {}".format(n,x))
            n+=1


    ipad_model = int(input("Enter your choice: "))
    

    return ipad_model

def stablet_samsung(cust_manf_tablet, tsamsung_model):
    if cust_manf_tablet ==2:
        print("Which Samsung tablet would you like to purchase?")
        n=1
        for x in stablet[0][1]:
            print("{})   {}".format(n,x))
            n+=1


    tsamsung_model = int(input("Enter your choice: "))
    

    return tsamsung_model

def slaptop_lenovo(cust_manf_laptop, Llenovo_model):
    if cust_manf_laptop ==1:
        print("Which Lenovo laptop would you like to purchase?")
        n=1
        for x in lenovolap[0][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=2
        for x in lenovolap[1][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=3
        for x in lenovolap[2][1]:
            print("{})   {}".format(n,x))
            n+=1

    Llenovo_model = int(input("Enter your choice: "))
    

    return Llenovo_model

def slaptop_hp(cust_manf_laptop, Lhp_model):
    if cust_manf_laptop ==2:
        print("Which HP laptop would you like to purchase?")
        n=1
        for x in hplap[0][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=2
        for x in hplap[1][1]:
            print("{})   {}".format(n,x))
            n+=1

        n=3
        for x in hplap[2][1]:
            print("{})   {}".format(n,x))
            n+=1



    Lhp_model = int(input("Enter your choice: "))
    

    return Lhp_model

def sPC_lenovo(cust_manf_PC, PClenovo_model):
    if cust_manf_PC ==1:
        print("Which Lenovo PC would you like to purchase?")
        n=1
        for x in LenovoPC[0][1]:
            print("{})   {}".format(n,x))
            n+=1

    PClenovo_model = int(input("Enter your choice: "))
    

    return PClenovo_model

def sPC_HP(cust_manf_PC, PCHP_model):
    if cust_manf_PC ==2:
        print("Which HP PC would you like to purchase?")
        n=1
        for x in HPPC[0][1]:
            print("{})   {}".format(n,x))
            n+=1

    PCHP_model = int(input("Enter your choice: "))
    

    return PCHP_model

def sphone_storage_apple(iphone_model, iphone_storage):
    print("Please select your storage size for your iPhone.")
    if iphone_model <= 4:
        n=1
        for x in iphone_cat[0][3]:
            print("{})   {}".format(n,x))
            n+=1

    if iphone_model >=5:
        n=1
        for x in iphone_cat[1][3]:
            print("{})   {}".format(n,x))
            n+=1

    iphone_storage = int(input("Enter your choice: "))
    
        

    return iphone_storage

def sphone_storage_samsung(samsung_model, samsung_storage):
    print("Please select your storage size for your samsung phone.")
    if samsung_model <= 3:
        n=1
        for x in samsung[0][3]:
            print("{})   {}".format(n,x))
            n+=1

    if samsung_model >=4 and samsung_model <= 6:
        n=1
        for x in samsung[1][3]:
            print("{})   {}".format(n,x))
            n+=1

    if samsung_model ==7:
        n=1
        for x in samsung[2][3]:
            print("{})   {}".format(n,x))
            n+=1

    if samsung_model ==8:
        n=1
        for x in samsung[3][3]:
            print("{})   {}".format(n,x))
            n+=1

    if samsung_model ==9:
        n=1
        for x in samsung[4][3]:
            print("{})   {}".format(n,x))
            n+=1

    samsung_storage = int(input("Enter your choice: "))
        

    return samsung_storage

def sphone_storage_huawei(huawei_model, huawei_storage):
    print("Please select your storage size for your huawei phone.")
    if huawei_model <= 2:
        n=1
        for x in huawei[0][3]:
            print("{})   {}".format(n,x))
            n+=1

    if huawei_model >=3 and huawei_model <= 5:
        n=1
        for x in huawei[1][3]:
            print("{})   {}".format(n,x))
            n+=1

    if huawei_model >=6:
        n=1
        for x in huawei[2][3]:
            print("{})   {}".format(n,x))
            n+=1

    huawei_storage = int(input("Enter your choice: "))

    return huawei_storage

def sphone_storage_google(google_model, google_storage):
    print("Please select your storage size for your Google phone.")
    if google_model <= 2:
        n=1
        for x in google[0][3]:
            print("{})   {}".format(n,x))
            n+=1

    if google_model >=3:
        n=1
        for x in google[1][3]:
            print("{})   {}".format(n,x))
            n+=1


    google_storage = int(input("Enter your choice: "))

    return google_storage

def stablet_storage_apple(ipad_model, ipad_storage):
    print("Please select your storage size for your iPad.")
    if ipad_model == 1:
        n=1
        for x in ipad_cat[0][3]:
            print("{})   {}".format(n,x))
            n+=1

    if ipad_model ==2:
        n=1
        for x in ipad_cat[1][3]:
            print("{})   {}".format(n,x))
            n+=1

    if ipad_model ==3:
        n=1
        for x in ipad_cat[2][3]:
            print("{})   {}".format(n,x))
            n+=1

    if ipad_model ==4:
        n=1
        for x in ipad_cat[3][3]:
            print("{})   {}".format(n,x))
            n+=1



    ipad_storage = int(input("Enter your choice: "))

    return ipad_storage

def stablet_storage_samsung(tsamsung_model, tsamsung_storage):
    print("Please select your storage size for your Samsung tablet.")
    if tsamsung_model >= 1:
        n=1
        for x in stablet[0][3]:
            print("{})   {}".format(n,x))
            n+=1

    tsamsung_storage = int(input("Enter your choice: "))

    return tsamsung_storage

def sphone_colour_apple(iphone_model, iphone_colour):
    print("Please select an available colour for your iPhone.")
    n=1
    if iphone_model <= 4:
        for x in iphone_cat[0][2]:
            print("{})   {}".format(n,x))
            n+=1
    n=1
    if iphone_model >=5:
        for x in iphone_cat[1][2]:
            print("{})   {}".format(n,x))
            n+=1


    iphone_colour = int(input("Enter your choice: "))
    
       
    

    return iphone_colour

def sphone_colour_samsung(samsung_model, samsung_colour):
    print("Please select an available colour for your samsung phone.")
    n=1
    if samsung_model <= 3:
        for x in samsung[0][2]:
            print("{})   {}".format(n,x))
            n+=1

    if samsung_model >=4 and samsung_model <= 6:
        n=1
        for x in samsung[1][2]:
            print("{})   {}".format(n,x))
            n+=1

    if samsung_model ==7:
        n=1
        for x in samsung[2][2]:
            print("{})   {}".format(n,x))
            n+=1

    if samsung_model ==8:
        n=1
        for x in samsung[3][2]:
            print("{})   {}".format(n,x))
            n+=1

    if samsung_model ==9:
        n=1
        for x in samsung[4][2]:
            print("{})   {}".format(n,x))
            n+=1


    samsung_colour = int(input("Enter your choice: "))
    


    return samsung_colour

def sphone_colour_huawei(huawei_model, huawei_colour):
    print("Please select an available colour for your huawei phone.")
    n=1
    if huawei_model <= 2:
        for x in huawei[0][2]:
            print("{})   {}".format(n,x))
            n+=1

    if huawei_model >=3 and huawei_model <= 5:
        n=1
        for x in huawei[1][2]:
            print("{})   {}".format(n,x))
            n+=1

    if huawei_model >=6:
        n=1
        for x in huawei[2][2]:
            print("{})   {}".format(n,x))
            n+=1



    huawei_colour = int(input("Enter your choice: "))



    return huawei_colour

def sphone_colour_google(google_model, google_colour):
    print("Please select an available colour for your Goodle phone.")
    n=1
    if google_model <= 2:
        for x in google[0][2]:
            print("{})   {}".format(n,x))
            n+=1

    if google_model >=3:
        n=1
        for x in google[1][2]:
            print("{})   {}".format(n,x))
            n+=1


    google_colour = int(input("Enter your choice: "))



    return google_colour

def stablet_colour_apple(ipad_model, ipad_colour):
    print("Please select an available colour for your iPad.")
    n=1
    if ipad_model == 1:
        for x in ipad_cat[0][2]:
            print("{})   {}".format(n,x))
            n+=1

    if ipad_model ==2:
        n=1
        for x in ipad_cat[1][2]:
            print("{})   {}".format(n,x))
            n+=1

    if ipad_model ==3:
        n=1
        for x in ipad_cat[2][2]:
            print("{})   {}".format(n,x))
            n+=1

    if ipad_model ==4:
        n=1
        for x in ipad_cat[3][2]:
            print("{})   {}".format(n,x))
            n+=1


    ipad_colour = int(input("Enter your choice: "))


    return ipad_colour

def stablet_colour_samsung(tsamsung_model, tsamsung_colour):
    print("Please select an available colour for your Samsung tablet.")
    n=1
    if tsamsung_model >= 1:
        for x in stablet[0][2]:
            print("{})   {}".format(n,x))
            n+=1

    tsamsung_colour = int(input("Enter your choice: "))


    return tsamsung_colour

def final_order_iphone(total, iphone_colour, iphone_model, iphone_storage):
    price= iphone_prices[iphone_model-1][iphone_storage-1]
    
    iphone_model1 = iphone_model


    if iphone_model1 <= 4:
        iphone_model = iphone_cat[0][1][iphone_model -1]
        

    if iphone_model1 > 4:
        iphone_model = iphone_cat[1][1][iphone_model -5]

    if iphone_model1 <= 4:
        iphone_storage = iphone_cat[0][3][iphone_storage -1]
        

    if iphone_model1 > 4:
        iphone_storage = iphone_cat[1][3][iphone_storage -1]

    if iphone_model1 <= 4:
        iphone_colour = iphone_cat[0][2][iphone_colour -1]
       

    if iphone_model1 >4:
        iphone_colour = iphone_cat[1][2][iphone_colour -1]
    

    
    total = [iphone_model, iphone_colour, iphone_storage, price]

    print(f"Alright, the item you have selected is, {total[0]}, colour; {total[1]}, storage; {total[2]}: {total[3]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_samsung(total, samsung_colour, samsung_model, samsung_storage):
    price= samsung_phone_prices[samsung_model-1][samsung_storage-1]
    
    
    samsung_model1 = samsung_model

    if samsung_model1 <= 3:
        samsung_model = samsung[0][1][samsung_model -1]

    if samsung_model1 > 3 and samsung_model1 <= 6:
        samsung_model = samsung[1][1][samsung_model -4]

    if samsung_model1 == 7:
        samsung_model = samsung[2][1][samsung_model -7]

    if samsung_model1 == 8:
        samsung_model = samsung[3][1][samsung_model -8]

    if samsung_model1 >= 9:
        samsung_model = samsung[4][1][samsung_model -9]

    if samsung_model1 <= 3:
        samsung_storage = samsung[0][3][samsung_storage -1]

    if samsung_model1 > 3 and samsung_model1 <= 6:
        samsung_storage = samsung[1][3][samsung_storage -1]
        
    if samsung_model1 == 7:
        samsung_storage = samsung[2][3][samsung_storage -1]
        
    if samsung_model1 == 8:
        samsung_storage = samsung[3][3][samsung_storage -1]
        
    if samsung_model1 >= 9:
        samsung_storage = samsung[4][3][samsung_storage -1]

    if samsung_model1 <= 3:
        samsung_colour = samsung[0][2][samsung_colour -1]

    if samsung_model1 > 3 and samsung_model1 <= 6:
        samsung_colour = samsung[1][2][samsung_colour -1]

    if samsung_model1 ==7:
        samsung_colour = samsung[2][2][samsung_colour -1]

    if samsung_model1 ==8:
        samsung_colour = samsung[3][2][samsung_colour -1]

    if samsung_model1 ==9:
        samsung_colour = samsung[4][2][samsung_colour -1]


    total = [samsung_model, samsung_colour, samsung_storage, price]

    print(f"Alright, the item you have selected is, {total[0]}, colour; {total[1]}, storage; {total[2]}: {total[3]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_huawei(total, huawei_colour, huawei_model, huawei_storage):
    price= huawei_phone_prices[huawei_model-1][huawei_storage-1]
    

    huawei_model1 = huawei_model


    if huawei_model1 <=2:
        huawei_model = huawei[0][1][huawei_model -1]

    if huawei_model1 >= 3 and huawei_model1 <6:
        huawei_model = huawei[1][1][huawei_model -3]

    if huawei_model1 >=6:
        huawei_model = huawei[2][1][huawei_model -6]

    if huawei_model1 <= 2:
        huawei_storage = huawei[0][3][huawei_storage -1]

    if huawei_model1 >=3 and huawei_model1 <= 5:
        huawei_storage = huawei[1][3][huawei_storage - 1]
            
    if huawei_model1 >=6:
        huawei_storage = huawei[2][3][huawei_storage -1]

    if huawei_model1 <= 2:
        huawei_colour = huawei[0][2][huawei_colour -1]

    if huawei_model1 >=3 and huawei_model1 <= 5:
        huawei_colour = huawei[1][2][huawei_colour -1]
            
    if huawei_model1 >=6:
        huawei_colour = huawei[2][2][huawei_colour -1]
            

    total = [huawei_model, huawei_colour, huawei_storage, price]

    print(f"Alright, the item you have selected is, {total[0]}, colour; {total[1]}, storage; {total[2]}: {total[3]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_google(total, google_colour, google_model, google_storage):
    price= google_phone_prices[google_model-1][google_storage-1]
    

    google_model1 = google_model

    if google_model1 <=2:
        google[0][1][google_model - 1]

    if google_model1 > 2:
        google_model = google[1][1][google_model -3]

    if google_model1 <= 2:
        google_storage = google[0][3][google_storage -1]

    if google_model1 >=3:
        google_storage = google[1][3][google_storage -1]

    if google_model1 <= 2:
        google_colour = google[0][2][google_colour -1]

    if google_model1 >=3:
        google_colour = google[1][2][google_colour -1]


    total = [google_model, google_colour, google_storage, price]

    print(f"Alright, the item you have selected is, {total[0]}, colour; {total[1]}, storage; {total[2]}: {total[3]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_ipad(total, ipad_colour, ipad_model, ipad_storage):
    price= ipad_prices[ipad_model-1][ipad_storage-1]
    

    ipad_model1 = ipad_model

    if ipad_model1 ==1:
        ipad_model = ipad_cat[0][1][ipad_model -1]
            
    if ipad_model1 ==2:
        ipad_model = ipad_cat[1][1][ipad_model -2]
            

    if ipad_model1 ==3:
        ipad_model = ipad_cat[2][1][ipad_model -3]
            

    if ipad_model1 ==4:
        ipad_model = ipad_cat[3][1][ipad_model -4]

    if ipad_model1 == 1:
        ipad_storage = ipad_cat[0][3][ipad_storage -1]
            
    if ipad_model1 ==2:
        ipad_storage = ipad_cat[1][3][ipad_storage -1]

    if ipad_model1 ==3:
        ipad_storage = ipad_cat[2][3][ipad_storage -1]

    if ipad_model1 ==4:
        ipad_storage = ipad_cat[3][3][ipad_storage -1]

    if ipad_model1 == 1:
        ipad_colour = ipad_cat[0][2][ipad_colour -1]

    if ipad_model1 ==2:
        ipad_colour = ipad_cat[1][2][ipad_colour -1]

    if ipad_model1 ==3:
        ipad_colour = ipad_cat[2][2][ipad_colour -1]

    if ipad_model1 ==4:
        ipad_colour = ipad_cat[3][2][ipad_colour -1]

    total = [ipad_model, ipad_colour, ipad_storage, price]

    print(f"Alright, the item you have selected is, {total[0]}, colour; {total[1]}, storage; {total[2]}: {total[3]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_tsamsung(total, tsamsung_colour, tsamsung_model, tsamsung_storage):
    price= samsung_tablet_prices[tsamsung_model-1][tsamsung_storage-1]
    

    tsamsung_model1 =tsamsung_model

    if tsamsung_model1 >= 1:
        tsamsung_model = stablet[0][1][tsamsung_model -1]

    if tsamsung_model1 >= 1:
        tsamsung_storage = stablet[0][3][tsamsung_storage -1]

    if tsamsung_model1 >= 1:
        tsamsung_colour = stablet[0][2][tsamsung_colour -1]

    total = [tsamsung_model, tsamsung_colour, tsamsung_storage, price]

    print(f"Alright, the item you have selected is, {total[0]}, colour; {total[1]}, storage; {total[2]}: {total[3]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_Llenovo(total, Llenovo_model):
    price= lenovo_laptop_prices[Llenovo_model-1]
    
    Llenovo_model1 = Llenovo_model
    
    if Llenovo_model1 == 1:
        Llenovo_model = lenovolap[0][1][Llenovo_model -1]
            

    if Llenovo_model1 == 2:
        Llenovo_model = lenovolap[1][1][Llenovo_model -2]
            
    if Llenovo_model1 == 3:
        Llenovo_model = lenovolap[2][1][Llenovo_model -3]
            
    total = [Llenovo_model, price]

    print(f"Alright, the item you have selected is, {total[0]}: {total[1]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_Lhp(total, Lhp_model):
    price= hp_laptop_prices[Lhp_model-1]

    Lhp_model1 = Lhp_model

    if Lhp_model1 ==1:
        Lhp_model = hplap[0][1][Lhp_model -1]
            
    if Lhp_model1 ==2:    
        Lhp_model = hplap[1][1][Lhp_model -2]

    if Lhp_model1 ==3:
        Lhp_model = hplap[2][1][Lhp_model -3]
    

    total = [Lhp_model, price]

    print(f"Alright, the item you have selected is, {total[0]}: {total[1]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_PClenovo(total, PClenovo_model):
    price= lenovo_pc_prices[PClenovo_model-1]


    PClenovo_model1 = PClenovo_model
        
    if PClenovo_model1 ==1:  
        PClenovo_model = LenovoPC[0][1][PClenovo_model -1]
        
    total = [PClenovo_model, price]

    print(f"Alright, the item you have selected is, {total[0]}: {total[1]}")
    print("Item succesfully added to the cart!")

    return total

def final_order_PCHP(total, PCHP_model):
    price= hp_pc_prices[PCHP_model-1]
    

    PCHP_model1 = PCHP_model

    if PCHP_model1 ==1:
        PCHP_model = HPPC[0][1][PCHP_model -1]

    total = [PCHP_model, price]

    print(f"Alright, the item you have selected is, {total[0]}: {total[1]}")
    print("Item succesfully added to the cart!")

    return total

def address(current_acc):
    f= open(login_file())
    data= json.load(f)
    if "address" not in data['accounts'][current_acc].keys() or data['accounts'][current_acc]["address"]=="":
        address= str(input("""Almost ready. But first please enter your address.
    Please enter your address:
    """))
        data['accounts'][current_acc]["address"]=address
        json_obj= json.dumps(data, indent= 4)
        with open(login_file(), "w") as outfile:
            outfile.write(json_obj)
    else: 
        correct_address=input(f"""{data['accounts'][current_acc]["address"]}
Is this your current address? (Y/N)
""")
        if correct_address.upper()=="Y": address=data['accounts'][current_acc]["address"]
        else: 
            address= str(input("""Please enter your address:
    """))
            change_saved=input("Do you want to change the address saved on your account with this one? (Y/N) ")
            if change_saved.upper()=="Y": 
                print("New address saved.")
                data['accounts'][current_acc]["address"]=address
                json_obj= json.dumps(data, indent= 4)
                with open(login_file(), "w") as outfile:
                    outfile.write(json_obj)
            
    return address

def phone_number(current_acc):
    f= open(login_file())
    data= json.load(f)
    if "phone_number" not in data['accounts'][current_acc].keys() or data['accounts'][current_acc]["phone_number"]=="":
        phone_number= str(input("""Now, please enter your phone number.
    Please enter your phone number:
    """))
        data['accounts'][current_acc]["phone_number"]=phone_number
        json_obj= json.dumps(data, indent= 4)
        with open(login_file(), "w") as outfile:
            outfile.write(json_obj)
    else: 
        correct_phone_number=input(f"""{data['accounts'][current_acc]["phone_number"]}
Is this your current phone number? (Y/N)
""")
        if correct_phone_number.upper()=="Y": phone_number=data['accounts'][current_acc]["phone_number"]
        else: 
            phone_number= str(input("""Please enter your phone number:
    """))
            change_saved=input("Do you want to change the phone number saved on your account with this one? (Y/N) ")
            if change_saved.upper()=="Y": 
                print("New phone number saved.")
                data['accounts'][current_acc]["phone_number"]=phone_number
                json_obj= json.dumps(data, indent= 4)
                with open(login_file(), "w") as outfile:
                    outfile.write(json_obj)
            
    return phone_number


def payment(current_acc):
    f= open(login_file())
    data= json.load(f)
    if "saved_card" not in data['accounts'][current_acc].keys() or len(data['accounts'][current_acc]["saved_card"])==0:
        print("Enter Payment Information")
        print(" ")
        payment_method_info = {"Card Holder name" : "", "Card Number" : "", "Expiry Date" : "", "CVV" : "", "PIN" : ""}
        for i in payment_method_info:
            info = input("Enter {}: ".format(i))
            payment_method_info[i] = info
        data['accounts'][current_acc]["saved_card"]=payment_method_info
        json_obj= json.dumps(data, indent= 4)
        with open(login_file(), "w") as outfile:
            outfile.write(json_obj)
    else: 
        correct_payment_method_info=input(f"""{data['accounts'][current_acc]["saved_card"]}
Is this your current card information? (Y/N)
""")
        if correct_payment_method_info.upper()=="Y": payment_method_info=data['accounts'][current_acc]["saved_card"]
        else: 
            print("Enter Your Payment Information")
            print(" ")
            payment_method_info = {"Card Holder name" : "", "Card Number" : "", "Expiry Date" : "", "CVV" : "", "PIN" : ""}
            for i in payment_method_info:
                info = input("Enter {}: ".format(i))
                payment_method_info[i] = info
            change_saved=input("Do you want to change the payment information saved on your account with this one? (Y/N) ")
            if change_saved.upper()=="Y": 
                print("New payment information saved.")
                data['accounts'][current_acc]["saved_card"]=payment_method_info
                json_obj= json.dumps(data, indent= 4)
                with open(login_file(), "w") as outfile:
                    outfile.write(json_obj)
            
    return payment_method_info

def place_order(current_acc,cart):
    cust_address=address(current_acc)
    cust_phone_number= phone_number(current_acc)
    cash_or_cred= input("Would you like to pay in cash (1) or credit (2)? ")
    while cash_or_cred!="1" and cash_or_cred!="2":
        print("Invalid Choice")
        cash_or_cred= input("Please enter a valid choice (1 or 2): ")
    cash_or_cred= int(cash_or_cred)
    if cash_or_cred==2: cust_payment_info= payment(current_acc)
    elif cash_or_cred==1: print("Cash Payment")
    f= open("Orders.json")
    data= json.load(f)
    temp_dic={}
    temp_dic["order_id"]= data["Orders"][-1]["order_id"]+1
    temp_dic["account_index"]= current_acc
    temp_dic["address"]= cust_address
    temp_dic["contact"]= cust_phone_number
    temp_dic["order_details"]= cart
    if cash_or_cred==2: temp_dic["payment"]= "Card"
    elif cash_or_cred==1: temp_dic["payment"]= "Cash"
    data["Orders"].append(temp_dic)
    json_obj= json.dumps(data, indent= 4)
    with open("Orders.json", "w") as outfile:
        outfile.write(json_obj)
    print(f"""Order ID: {temp_dic["order_id"]}
    Your order has been placed and will be delivered to {cust_address}, 
    We will contact you on {cust_phone_number} once your order is out for delivery.
    """)
    f= open(login_file())
    data= json.load(f)
    if "previous_orders" not in data['accounts'][current_acc].keys() or len(data['accounts'][current_acc]["previous_orders"])==0:
        data['accounts'][current_acc]["previous_orders"]= []
    ctime= datetime.now()
    ctime2 = str(ctime).replace(("."+str(ctime.microsecond)),'')
    dic= {}
    dic[ctime2]= cart
    data['accounts'][current_acc]["previous_orders"].append(dic)
    json_obj= json.dumps(data, indent= 4)
    with open(login_file(), "w") as outfile:
        outfile.write(json_obj)
    repeat_order= False
    return repeat_order

def shopping_cart(cart, current_acc,repeat_order):
    if len(cart) == 0:
            print("Your cart is empty.")
            add_or_exit= input("""Please choose an option to continue.
    1.) Add an item to cart.
    2.) Save and exit.
        """)
            while add_or_exit not in ["1","2"]:
                print("Invalid Choice")
                add_or_exit= input("Please enter a valid choice (1 or 2): ")
            add_or_exit= int(add_or_exit)
            if add_or_exit==1: showcart=3
            elif add_or_exit==2: showcart=5
    else:
        print("This is what is in your shopping cart")
        cart_table=[]
        z=1
        total_price=0
        for x in cart:
            while len(x)<4:
                x.insert(1," ")
            total_price+= x[3]
            cart_table.append([z,x[0],x[1]+", "+x[2],"$"+str(x[3])])
            z+=1
        cart_table.append([" "," ","Total","$"+str(total_price)])
        print(tabulate(cart_table, headers=["Item No.","Item Name","Description","Price"], tablefmt="grid"))
        cart_table.clear()
        showcart= input("""Please choose an option to continue.
    1.) Place Order.
    2.) Remove item from cart.
    3.) Add another item to cart.
    4.) Clear cart. 
    5.) Save and exit.
        """)
        while showcart not in [str(x) for x in [1,2,3,4,5]]:
            print("Invalid Choice")
            showcart= input("Please choose an option from 1-5: ")
        showcart=int(showcart)
    if showcart ==1:
        print("Shipping costs $20 all over Egypt.")
        repeat_order=place_order(current_acc,cart)
        cart.clear()
    if showcart == 2:
        remove_item= input("Please enter the No. of the item you wish to remove: ")
        while remove_item not in [str(x) for x in range(1,len(cart)+1)]:
            print("Invalid Choice")
            remove_item= input("Please enter a choice from your cart: ")
        remove_item=int(remove_item)
        cart.pop(remove_item-1)
        print("Item removed from the cart.")
        cart,repeat_order=shopping_cart(cart, current_acc,repeat_order)

    if showcart == 3:
        repeat_order=True
    if showcart == 4:
        cart.clear()
        print("Cart has been cleared")
        cart,repeat_order=shopping_cart(cart, current_acc,repeat_order)
    f= open(login_file())
    data= json.load(f)
    data['accounts'][current_acc]["cart"]= cart
    json_obj= json.dumps(data, indent= 4)
    with open(login_file(), "w") as outfile:
        outfile.write(json_obj)
    if showcart==5: repeat_order= False
    return cart,repeat_order

#Validation##################################################
def email_validate(email):
    valid=False
    while not valid:
        pat = "^[a-z.A-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,email): valid=True
        else: email= input("The email format is incorrect. Please Re-enter your email: ")
    return email
def password_validate(passwd):
    val = False
    while not val:
        val = True
        if len(passwd) < 8:
            print('Password too short. Length should be at least 8')
            val = False
            
        if len(passwd) > 20:
            print('Password too long. Length should be not be greater than 20')
            val = False
            
        if not any(char.isdigit() for char in passwd):
            print('Password should have at least one numeral.')
            val = False
            
        if not any(char.isupper() for char in passwd):
            print('Password should have at least one uppercase letter.')
            val = False
            
        if not any(char.islower() for char in passwd):
            print('Password should have at least one lowercase letter.')
            val = False
            
        if not any(char in list(string.punctuation) for char in passwd):
            print('Password should have at least one symbol.')
            val = False
        if not val:
            passwd=input("Please Re-enter your desired password: ")
    return passwd
        
def validate_name(name):
    val= False
    while not val:
        if not any(char.isdigit() or char in string.punctuation.replace("-","") for char in name):
            val=True
        else: name= input("Name can't contain numbers or special characters (excluding '-'). Please re-enter your name: ")
    return name

def validate_selection(x,y,string):
    valid=False
    while not valid:
        valid=True
        if not string.isnumeric() or string not in [str(x) for x in range(x,y+1)]:
            valid=False
            string= input("Please choose one of the given options: ")
    return int(string)

def validate_adress(string):
    valid=False
    while not valid:
        valid=True
        pat = "^[A-Za-z]-[0-9]{2}$"
        if re.match(pat,string): 
            valid=True
        else: 
            string = input("The adress format is incorrect. Please Re-enter your adress in the following format (<StreetName> <StreetNumber>): ")
    return string

def validate_phonenumber(string):
    valid=False
    while not valid:
        valid=True
        if any(char in list(string.punctuation) for char in string) or any(char.isalpha() for char in string) or len(string)!=11:
            string = input("The phone number format is either wrong or number lenght(11) is incorrect.")
            

        else:
            valid=True
            

    return int(string)

def validate_cc(string, string2, string3, string4, string5):
    valid=False
    while not valid:
        valid=True
        pat1 = "^[A-Za-z]$"
        pat2 = "^[0-9]{16}$"
        pat3 = "^[0-9]{2}+/[0-9]{2}$"
        pat4 = "^[0-9]{3}$"
        pat5 = "^[0-9]{4}$"
        if not re.match(pat1,string):
            valid=False
            print("Name cannot contain numbers or special letters")

        if not re.match(pat2, string2) and string ==16:
            valid=False
            print("The Card Number cannot contain any letters or special characters.")

        if not re.match(pat3,string3):
            valid=False
            print("The Expiry date cannot contain any letters or special characters. And has to follow the following format(MM/DD)")

        if not re.match(pat4, string4) and string4 ==3:
            valid=False
            print("The CVV Number cannot contain any letters or special characters. And may only be 3 numbers long.")

        if not re.match(pat5, string5):
            valid=False
            print("The Card Number cannot contain any letters or special characters. And may only be 4 numbers long.")

        if not valid:
            string = input("Please input the Card Holder name again: ")
            string2 = input("Please input the Card Number again: ")
            string3 = input("Please input the Expiry date again: ")
            string4 = input("Plese input your CVV number again: ")
            string5 = input("Please input your PIN again: ")

    return string,string2,string3,string4,string5
        
                  

    
#register and login#################
def login_file():
    dir= os.path.dirname(__file__)
    dir=dir.replace("\\","/")
    dir+= "/Accounts.json"
    return dir
def register(cust_email,datasource):
    current_id= datasource['accounts'][-1]['id']+1
    newest_account={}
    newest_account['id']=current_id
    newest_account['customer_full_name']=validate_name(input("Pls enter your full name: "))
    newest_account['email']=cust_email
    password=''
    password_attempt=None
    while password!=password_attempt:
        password=password_validate(input("pls enter your desired password: "))
        password_attempt=input("pls enter the password again: ")
        if password!=password_attempt: print("Passwords don't match.")
    newest_account['password']=password
    datasource['accounts'].append(newest_account)
    json_obj= json.dumps(datasource, indent= 4)
    with open(login_file(), "w") as outfile:
        outfile.write(json_obj)
    current_account= current_id-1
    return current_account 
def login(email=None):
    logged_in=False
    while logged_in==False:
        if not email:
            email=email_validate(input("Please enter your email: "))
        f= open(login_file())
        data= json.load(f)
        for i in data['accounts']:
            if i["email"]==email:
                account_found=True
                current_account=data['accounts'].index(i)
                break
            else: account_found=False
        f.close()
        if not account_found:
            print("There is no account with that email address.You will need to register")
            current_account= register(email,data)
            logged_in=True
        else: 
            password_correct=False
            while password_correct==False:
                password=input("Pls enter your password: ")
                if password==data['accounts'][current_account]['password']:
                    password_correct=True
                    logged_in=True
    return current_account

def order_history(current_acc):
    valid=True
    f = open (login_file())
    display = json.load(f)
    n=1
    if "previous_orders" not in display['accounts'][current_acc].keys() or len(display['accounts'][current_acc]["previous_orders"])==0:
        print("You don't have any orders.")
        valid=False
    else:
        for x in display["accounts"][current_acc]["previous_orders"]:
            for k in x.keys():
                print(f"{n}) Order date: {k},\n Order details: {x[k]}")
            n+=1
    f.close()
    return display,valid


def log_or_reg():
    logORreg= input("Please choose an option: 1.Login 2.Register\n")
    while (not logORreg.isdigit()) or (int(logORreg)!=1 and int(logORreg)!=2):
        print("Invalid Choice")
        logORreg= input("Please choose an option: 1.Login 2.Register\n")
    if int(logORreg)==1: current_account=login()
    elif int(logORreg)==2:
        email=email_validate(input("Pls enter your email: "))
        f= open(login_file())
        data= json.load(f)
        for i in data['accounts']:
            if i["email"]==email:
                account_found=True
                current_account=data['accounts'].index(i)
                break
            else: account_found=False
        if account_found:
            print("Account already exists. Please login.")
            current_account=login(email)
        else: current_account=register(email,data)
    return current_account

def locations_function():
    print("""We have stores in 1.{}, 2.{}, 3.{}, 4.{}, 5.{}, 6.{}.
        """.format(locations_list[0], locations_list[1], locations_list[2], locations_list[3], locations_list[4], locations_list[5]))
    inspect_location = int(input("Choose a location to learn more: "))
    if inspect_location == 1:
        print("""Azka Tronics store in {} in the {} floor.
        Mall Location: {}.""".format(locations_list[0],"second","https://goo.gl/maps/fMR5h9nFsKjaDU1H9"))
    elif inspect_location == 2:
        print("""Azka Tronics store in {} in the {} floor.
        Mall Location: {}.""".format(locations_list[1],"fourth","https://goo.gl/maps/Ef2DpumrqXdtSqoTA"))
    elif inspect_location == 3:
        print("""Azka Tronics store in {} in the {} floor.
        Mall Location: {}.""".format(locations_list[2],"third","https://goo.gl/maps/og5dbUqiaBkYcP3j9"))
    elif inspect_location == 4:
        print("""Azka Tronics store in {} in the {} floor.
        Mall Location: {}.""".format(locations_list[3],"ground","https://goo.gl/maps/WMf3mk7q98gJC5hEA"))
    elif inspect_location == 5:
        print("""Azka Tronics store in {} in the {} floor.
        Mall Location: {}.""".format(locations_list[4],"fifth","https://goo.gl/maps/5vMtoLoJL5YVpqBo7"))
    elif inspect_location == 6:
        print("""Azka Tronics store in {} in the {} floor.
        Mall Location: {}.""".format(locations_list[5],"second","https://goo.gl/maps/RThzNWtzeTEG3G148"))
    else:
        print("Invalid choice")
        pass

  

#-----------------------------------------order product----------------------------------------------------------------
def order_product(current_acc,checked=False):
    cust_need = 1
    cust_manf = None
    cust_device = None
    cust_manf_tablet = None
    cust_manf_laptop = None
    cust_manf_PC = None
    iphone_model = 0
    iphone_colour = None
    iphone_storage = None
    total = 0
    cart = []
    samsung_model = 0
    samsung_storage = None
    samsung_colour = None
    huawei_model = 0
    huawei_storage = None
    huawei_colour = None
    google_model = 0
    google_storage = None
    google_colour = None
    ipad_model = 0
    ipad_storage = None
    ipad_colour = None
    tsamsung_model = 0
    tsamsung_storage = None
    tsamsung_colour = None
    Llenovo_model = 0
    Lhp_model = 0
    PClenovo_model = 0
    PCHP_model=0
    repeat_order= True
    f= open(login_file())
    data= json.load(f)
    if not checked:
        if "cart" in data['accounts'][current_acc].keys() and len(data['accounts'][current_acc]["cart"])!=0:
            cart= data['accounts'][current_acc]["cart"].copy()
            check_cart= input(f"You already have {len(cart)} item(s) in your cart would you like to check them out? (Y/N) ")
            while check_cart.upper()!="Y" and check_cart.upper()!="N":
                check_cart= input("Please enter a valid choice (Y/N): ")
            if check_cart.upper()=="Y": cart,repeat_order=shopping_cart(cart, current_acc,repeat_order)
        checked=True
    if "cart" in data['accounts'][current_acc].keys() and len(data['accounts'][current_acc]["cart"])!=0:
        cart= data['accounts'][current_acc]["cart"].copy()
    if repeat_order:
        repeat_order= False
        cust_device = sdevice(cust_need, cust_device)
        if cust_device == 1:
            cust_manf = sphone_manf(cust_device, cust_manf)
            if cust_manf ==1:
                iphone_model = sphone_apple(cust_manf, iphone_model)
                iphone_storage = sphone_storage_apple(iphone_model, iphone_storage)
                iphone_colour = sphone_colour_apple(iphone_model, iphone_colour)
                total = final_order_iphone(total, iphone_colour, iphone_model, iphone_storage)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
            if cust_manf ==2:
                samsung_model = sphone_samsung(cust_manf, samsung_model)
                samsung_storage = sphone_storage_samsung(samsung_model, samsung_storage)
                samsung_colour = sphone_colour_samsung(samsung_model, samsung_colour)
                total = final_order_samsung(total, samsung_colour, samsung_model, samsung_storage)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
            if cust_manf ==3:
                huawei_model = sphone_huawei(cust_manf, huawei_model)
                huawei_storage = sphone_storage_huawei(huawei_model, huawei_storage)
                huawei_colour = sphone_colour_huawei(huawei_model, huawei_colour)
                total = final_order_huawei(total, huawei_colour, huawei_model, huawei_storage)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
            if cust_manf ==4:
                google_model = sphone_google(cust_manf, google_model)
                google_storage = sphone_storage_google(google_model, google_storage)
                google_colour = sphone_colour_google(google_model, google_colour)
                total = final_order_google(total, google_colour, google_model, google_storage)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
                

        if cust_device ==2:
            cust_manf_tablet = stablet_manf(cust_device, cust_manf_tablet)
            if cust_manf_tablet ==1:
                ipad_model = stablet_apple(cust_manf_tablet, ipad_model)
                ipad_storage = stablet_storage_apple(ipad_model, ipad_storage)
                ipad_colour = stablet_colour_apple(ipad_model, ipad_colour)
                total = final_order_ipad(total, ipad_colour, ipad_model, ipad_storage)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
            if cust_manf_tablet ==2:
                tsamsung_model = stablet_samsung(cust_manf_tablet, tsamsung_model)
                tsamsung_storage = stablet_storage_samsung(tsamsung_model, tsamsung_storage)
                tsamsung_colour = stablet_colour_samsung(tsamsung_model, tsamsung_colour)
                total = final_order_tsamsung(total, tsamsung_colour, tsamsung_model, tsamsung_storage)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)

        if cust_device ==3:
            cust_manf_laptop = slaptop_manf(cust_device, cust_manf_laptop)
            if cust_manf_laptop ==1:
                Llenovo_model = slaptop_lenovo(cust_manf_laptop, Llenovo_model)
                total = final_order_Llenovo(total, Llenovo_model)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
            if cust_manf_laptop ==2:
                Lhp_model = slaptop_hp(cust_manf_laptop, Lhp_model)
                total = final_order_Lhp(total, Lhp_model)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
        
        if cust_device ==4:
            cust_manf_PC = sPC_manf(cust_device, cust_manf_PC)
            if cust_manf_PC == 1:
                PClenovo_model = sPC_lenovo(cust_manf_PC, PClenovo_model)
                total = final_order_PClenovo(total, PClenovo_model)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
            if cust_manf_PC == 2:
                PCHP_model = sPC_HP(cust_manf_PC, PCHP_model)
                total = final_order_PCHP(total, PCHP_model)
                cart.append(total)
                cart,repeat_order = shopping_cart(cart, current_acc,repeat_order)
    if repeat_order: order_product(current_acc,checked)
#-----------------------------------------Track order----------------------------------------------------------------
def track_order(Order_date):
    Today_date = date.today()
    string_td_date=(str(Today_date))
    days = datetime.now()

    date_diff = datetime.strptime(string_td_date, "%Y-%m-%d") - datetime.strptime(Order_date, "%Y-%m-%d")
    
    if date_diff.days<=1:
        print("Your order is pending and will be confirmed soon.")
    elif date_diff.days==2:
        print("Your order is confirmed and will be shipped as soon as possible.")
    elif date_diff.days==3:
        print("Your order is being shipped.")
    elif date_diff.days==4:
        print("Waiting for carrier to pick up and deliver you package.")
    elif date_diff.days==5:
        print("Order is out for delivery!")
    else:
        print("""Order is delivered!\n
Please send us a review on the overall service.
Or contact us if the order wasn't delivered or have any concerns.
See you again soon!""")






"""
 * Start of code execution
 """

def main():  
    
    cust_need= input("""
        Hi there, this is Azka-bot, Azka-tronic's chatbot, how can I help? Please choose an option.
1)	Order a product.
2)	View our products.
3)	Track an order.
4)	Know our store locations.
5)	Work for us.
6)  View order history.
""")
    while (not cust_need.isdigit()) or (int(cust_need) not in [x for x in range(1,7)]):
        cust_need=(input("Please enter a valid choice."))
    cust_need= int(cust_need)
    if cust_need==1 or cust_need==3 or cust_need==6:
        current_acc=log_or_reg()
    
    if cust_need==1: order_product(current_acc)

    if cust_need==2:
        # featured_itemsfunction()
        device_specs=int(input("""What device do you want to view the specs of:
1)	Smartphone.
2)	Tablet.
3)	Laptop.
4)	Desktop PC.   
"""))
        if device_specs==1:
            spec_list= Phone_speclist.copy()
            smartphone_specs=int(input("""Select a device manufacturer:
1)	Apple.
2)	Samsung.
3)	Huawei.
4)	Google.
""")) 
            if smartphone_specs==1:
                first_manifacturer= iphone.copy()
                print("Which Apple phone would you like to view?")
                n=1
                for x in iphone:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                apple_specs=int(input("Enter your choice: "))
                first_device=apple_specs-1
                comparechoice=iphone_view_or_compare(apple_specs)

            if smartphone_specs==2:
                first_manifacturer= samsung_phones.copy()
                print("Which Samsung phone would you like to view?")
                n=1
                for x in samsung_phones:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                samsung_specs=int(input("Enter your choice: "))
                first_device=samsung_specs-1
                comparechoice=samsung_view_or_compare(samsung_specs)
            
            if smartphone_specs==3:
                first_manifacturer=huawei_phones.copy()
                print("Which Huawei phone would you like to view?")
                n=1
                for x in huawei_phones:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                huawei_specs=int(input("Enter your choice: "))
                first_device=huawei_specs-1
                comparechoice=hauwei_view_or_compare(huawei_specs)

            if smartphone_specs==4:
                first_manifacturer=google_phones.copy()
                print("Which Google phone would you like to view?")
                n=1
                for x in google_phones:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                google_specs=int(input("Enter your choice: "))
                first_device=google_specs-1
                comparechoice=google_view_or_compare(google_specs)

        if device_specs ==2:
            spec_list= Phone_speclist.copy()
            tablet_specs=int(input("""Here's a list of the tablet manufacturers: (Please choose an option)
1) Apple
2) Samsung
"""))
            if tablet_specs==1:
                first_manifacturer=Tablets_iphone.copy()
                print("Which iPad would you like to view?")
                n=1
                for x in Tablets_iphone:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                ipad_specs=int(input("Enter your choice: "))
                first_device=ipad_specs-1
                comparechoice=ipad_view_or_compare(ipad_specs)
        
            if tablet_specs==2:
                first_manifacturer=Tablets_samsung.copy()
                print("Which Samsung Tablet would you like to view?")
                n=1
                for x in Tablets_samsung:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                samsung_tablet_specs=int(input("Enter your choice: "))
                first_device=samsung_tablet_specs-1
                comparechoice=samsung_tablet_view_or_compare(samsung_tablet_specs)
    
        if device_specs ==3:
            spec_list=Laptop_speclist.copy()
            laptop_specs=int(input("""Here's a list of the laptop manufacturers: (Please choose an option)
1) Lenovo
2) Hp
"""))
            if laptop_specs==1:
                first_manifacturer=laptop_lenovo.copy()
                print("Which Lenovo laptop would you like to view?")
                n=1
                for x in laptop_lenovo:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                lenovo_laptop_specs=int(input("Enter your choice: "))
                first_device=lenovo_laptop_specs-1
                comparechoice=lenovo_laptop_view_or_compare(lenovo_laptop_specs)
            if laptop_specs==2:
                first_manifacturer=laptop_HP.copy()
                print("Which Hp laptop would you like to view?")
                n=1
                for x in laptop_HP:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                hp_laptop_specs=int(input("Enter your choice: "))
                first_device=hp_laptop_specs-1
                comparechoice=hp_laptop_view_or_compare(hp_laptop_specs)
    
        if device_specs==4:
            spec_list=Desktop_speclist.copy()
            pc_specs=int(input("""Here's a list of the PC manufacturers: (Please choose an option)
1) Lenovo
2) Hp
"""))
            if pc_specs==1:
                first_manifacturer=pc_lenovo.copy()
                print("Which Lenovo PC would you like to view?")
                n=1
                for x in pc_lenovo:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                lenovo_pc_specs=int(input("Enter your choice: "))
                first_device=lenovo_pc_specs-1
                comparechoice=lenovo_pc_view_or_compare(lenovo_pc_specs)
            if pc_specs==2:
                first_manifacturer=pc_hp.copy()
                print("Which Hp PC would you like to view?")
                n=1
                for x in pc_hp:
                    print("{})   {}".format(n,x[0]))
                    n+=1
                hp_pc_specs=int(input("Enter your choice: "))
                first_device=hp_pc_specs-1
                comparechoice=hp_pc_view_or_compare(hp_pc_specs)
        if comparechoice==2:
            if device_specs==1: second_manf,second_device=second_phone_choice()
            elif device_specs==2: second_manf,second_device=second_tablet_choice()
            elif device_specs==3: second_manf,second_device=second_laptop_choice()
            elif device_specs==4: second_manf,second_device=second_desktop_choice()
            compare_devices(spec_list,first_manifacturer,first_device,second_manf,second_device)
    if cust_need==3:
        orders,valid=order_history(current_acc)
        if valid:
            order_track= input("Please choose which order you would like to track: ")
            while (not order_track.isdigit()) or (int(order_track) not in [x for x in range(1,len(orders["accounts"][current_acc]["previous_orders"])+1)]):
                print("Invalid Choice")
                order_track= input("Please choose a number from the list above: ")
            order_track= int(order_track)
            for k in orders["accounts"][current_acc]["previous_orders"][order_track-1].keys():
                order_date= k.split()
            track_order(order_date[0])
    if cust_need==4:
        locations_function()
    if cust_need==5:
        current_application=[]
        job_choice= int(input("""Please choose the desired position: 
1)Delivery Driver
2)Store Clerk
3)Tech Support
4)Office Work
"""))
        print("Personal Info: ")
        current_application.append(input("Please enter your full name: ")) #index 0
        current_application.append(jobs[job_choice-1]) #index 1
        current_application.append(input("Please enter your address: ")) #index 2
        current_application.append(input("Please enter your phone number: ")) #index 3
        current_application.append(input("Please enter your email: ")) #index 4
        id= input("Do you have an Egyption national ID? (Y/N) ")
        if id.upper()=="Y": current_application.append(input("Please enter your National Identification Number (Raqam Qawmi): ")) #index 5
        else: current_application.append("None") #index 5
        employment_desired_choice= int(input("""Please choose the work schedule your desire:
1) Full-time
2) Part-time
3) Seasonal
"""))
        current_application.append(employment_desired[employment_desired_choice-1])#index 6
        print("Employment Eligibilty: ")
        worked_before=input("Worked for us before? (Y/N) ")
        current_application.append(worked_before.upper()) #index 7
        if worked_before.upper()=="Y": current_application.append(input("Please describe your previous experience including dates: ")) #index 8
        else: current_application.append("None") #index 8
        convicted_before=input("Have you been convicted of a felony before? (Y/N) ")
        current_application.append(convicted_before.upper()) #index 9
        if convicted_before.upper()=="Y": current_application.append(input("Please explain: ")) #index 10
        else: current_application.append("None") #index 10
        print("Education: ")
        current_application.append(input("Please enter your High School's Name, including city: ")) #index 11
        current_application.append(input("Please enter your High School start date (DD/MM/YYYY): ")) #index 12
        current_application.append(input("Please enter your High School end date (DD/MM/YYYY): ")) #index 13
        current_application.append(input("Did you graduate High School? (Y/N) ").upper()) #index 14
        college= input("Did you go to college? (Y/N) ")
        if college.upper()=="Y":
            current_application.append(input("Please enter your College's Name, including city: ")) #index 15
            current_application.append(input("Please enter your College start date (DD/MM/YYYY): ")) #index 16
            current_application.append(input("Please enter your College end date (DD/MM/YYYY): ")) #index 17
            grad_college=input("Did you graduate College? (Y/N) ")
            if grad_college.upper()=="Y": 
                current_application.append("Y") #index 18
                current_application.append(input("Please enter your Degree: ")) #index 19
            else:
                current_application.append("N") #index 18
                current_application.append("None") #index 19
        else:
            current_application.append("None") #index 15
            current_application.append("None") #index 16
            current_application.append("None") #index 17
            current_application.append("N") #index 18
            current_application.append("None") #index 19
        data_correct="N"
        while data_correct.upper()=="N":
            for x in range(len(application_info)):
                print("{}) {}:   {}".format(x+1,application_info[x],current_application[x]))
            data_correct=input("Is all your data correct? (Y/N) ")
            if data_correct.upper()=="N": 
                data_change= int(input("Please enter the number of the wrong data: "))
                current_application[data_change-1]= input("Please enter the correct value: ")
        if data_correct.upper()=="Y":
            dir= os.path.dirname(__file__)
            dir=dir.replace("\\","/")
            dir+= "/JOB_APPLICATIONS.txt"
            f= open(dir,"a+")
            f.write("{} \n" .format(current_application))
            print("""Thank you {} for your application to the {} role at Azka-tronics.
    We will contact you soon on {}.
            
    In the event that you are accepted, you will be invited to an interview.
    P.S. Don't forget to get all your papers to the interview: id/passport/CV/Portfolio
    """.format(current_application[0],current_application[1],current_application[3]))
        exit()

    if cust_need == 6:
        orders,valid=order_history(current_acc)
        if valid:
            reorder_status= input("Would like to reorder one of these orders?\n If so enter the order number, if not enter 0: ")
            while (not reorder_status.isdigit()) or (int(reorder_status) not in [x for x in range(0,len(orders["accounts"][current_acc]["previous_orders"])+1)]):
                reorder_status= input("Please select a valid choice: ")
            reorder_status=int(reorder_status)
            if reorder_status==0: pass
            else: 
                for v in orders["accounts"][current_acc]["previous_orders"][reorder_status-1].values():
                    order_info= v
                    place_order(current_acc,order_info)


if __name__ == "__main__":
    main()


    """ End of file --------------------------------------------------------------------------------"""