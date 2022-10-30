import pygame
from typing import *

from numpy import floor


score: int
DataCollection = []
correct_count = 0
false_count = 0



def ms_to_mins(ms: int) -> list[str]:
    secs = float(floor(ms / 1000))
    txt_s = '{0:02d}'.format(int(secs % 60))
    mins = int(floor(secs / 60))
    return [str(mins), txt_s, '{0:03d}'.format(ms % 1000)]


