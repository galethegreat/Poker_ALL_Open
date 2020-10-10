import os
import win32gui
import time
import sys
import subprocess


#png or PNG makes a difference it is CASE sensative !
BOT_LEFT_IMG = 'BBDefense_BTN.png'
TOP_LEFT_IMG = 'Gale3BetBTNDef.png'
BOT_RIGHT_IMG = 'GaleRFI - Copy - Copy.PNG'
TOP_RIGHT_IMG = '3BetIPPotBluffs.PNG'

BOT_LEFT_PATH = 'F:\\CrushPoker\\OverNightMonster\\Charts\\BigBlind\\' + BOT_LEFT_IMG
TOP_LEFT_PATH = 'F:\\CrushPoker\\OverNightMonster\\Charts\\3BDef\\' + TOP_LEFT_IMG
BOT_RIGHT_PATH = 'F:\\CrushPoker\\OverNightMonster\\Charts\\RFI\\' + BOT_RIGHT_IMG
TOP_RIGHT_PATH = 'F:\\CrushPoker\\OverNightMonster\\Charts\\3BetNotes\\' + TOP_RIGHT_IMG

folder_paths = [BOT_LEFT_PATH, TOP_LEFT_PATH, BOT_RIGHT_PATH, TOP_RIGHT_PATH]

POKER_TRACKER_PATH = "C:\\Program Files (x86)\\PokerTracker 4\\PokerTracker4.exe"
POKER_STARS_PATH = "F:\games\poker stars\PokerStars\PokerStarsUpdate.exe"

TOP_RIGHT_COORD = [954+1920,0,980,530]
TOP_LEFT_COORD = [-10+1920,0,980,530]
BOTTOM_RIGHT_COORD = [954+1920,515,980,530]
BOTTOM_LEFT_COORD = [-10+1920,515,980,530]

#could be empty
#WPV = ''
WPV = " - Windows Photo Viewer"

def openCharts(paths):
    for path in paths:
        os.startfile(path)

def enumHandler(hwnd, lParam):
     if win32gui.IsWindowVisible(hwnd):
         if (TOP_LEFT_IMG + WPV) in win32gui.GetWindowText(hwnd):
             win32gui.MoveWindow(hwnd, TOP_LEFT_COORD[0], TOP_LEFT_COORD[1], TOP_LEFT_COORD[2],TOP_LEFT_COORD[3], True)
         elif (TOP_RIGHT_IMG + WPV) in win32gui.GetWindowText(hwnd):
             win32gui.MoveWindow(hwnd, TOP_RIGHT_COORD[0], TOP_RIGHT_COORD[1], TOP_RIGHT_COORD[2],TOP_RIGHT_COORD[3], True)
         elif (BOT_LEFT_IMG + WPV) in win32gui.GetWindowText(hwnd):
             win32gui.MoveWindow(hwnd, BOTTOM_LEFT_COORD[0], BOTTOM_LEFT_COORD[1], BOTTOM_LEFT_COORD[2],BOTTOM_LEFT_COORD[3], True)
         elif (BOT_RIGHT_IMG + WPV) in win32gui.GetWindowText(hwnd):
             win32gui.MoveWindow(hwnd, BOTTOM_RIGHT_COORD[0], BOTTOM_RIGHT_COORD[1], BOTTOM_RIGHT_COORD[2],BOTTOM_RIGHT_COORD[3],  True)

openCharts(folder_paths)
subprocess.Popen([POKER_TRACKER_PATH])
time.sleep(0.5)
subprocess.Popen([POKER_STARS_PATH])
time.sleep(0.5)

win32gui.EnumWindows(enumHandler, None)
