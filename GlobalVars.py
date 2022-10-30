import pygame
from typing import *

from numpy import floor

startTime: Any
firstStage = [

]

def ms_to_mins(ms :int) -> list[str]:
    secs = float(floor(ms / 1000))
    txt_s = '{0:02d}'.format(int(secs))
    mins = int(floor(secs / 60))
    return [str(mins), txt_s, '{0:03d}'.format(ms % 1000)]
def zero():
    firstStage = []