# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from pathlib import Path
import pandas as pd
import random
import pickle
import math

# Ensure that relative paths start from the same directory as this script
thisDirectory = os.path.dirname(os.path.abspath(__file__))
os.chdir(thisDirectory)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'exp3'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': 'A',
}

# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = thisDirectory + os.sep + u'data/%s_%s_%s' % (expName, expInfo['participant'], expInfo['session'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/josephpruitt/Desktop/SDT_Exp_1/exp3/exp3.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = False

X = 128

noiseTexture = np.random.random([X,X])*2.-1.
gaborTexture = (
    visual.filters.makeGrating(res=X, cycles=X * .05) *
    visual.filters.makeMask(matrixSize=X, shape="gauss", range=[0, 1])
)

Signal1 = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(557, 0),
     opacity=0, ori=45, contrast=1, units='pix', blendmode='avg')

Noise1 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(557,0), contrast=1)

Signal2 = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(1158, 0),
     opacity=0, ori=45, contrast=1, units='pix', blendmode='avg')

Noise2 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(1158,0), contrast=1)

Signal3 = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(1716, 0),
     opacity=0, ori=45, contrast=1, units='pix', blendmode='avg')

Noise3 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(1716,0), contrast=1)

Signal4 = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(2274, 0),
     opacity=0, ori=45, contrast=1, units='pix', blendmode='avg')

Noise4 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(2274,0), contrast=1)

Signal5 = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(-557, 0),
     opacity=0, ori=45, contrast=1, units='pix', blendmode='avg')

Noise5 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(-557,0), contrast=1)

Signal6 = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(-1158, 0),
     opacity=0, ori=45, contrast=1, units='pix', blendmode='avg')

Noise6 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(-1158,0), contrast=1)

Signal7 = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(-1716, 0),
     opacity=0, ori=45, contrast=1, units='pix', blendmode='avg')

Noise7 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(-1716,0), contrast=1)

Signal8 = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(-2274, 0),
     opacity=0, ori=45, contrast=1, units='pix', blendmode='avg')

Noise8 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(-2274,0), contrast=1)

def DrawNoisyGratingStim(t, n):
    n.draw() # FIRST draw noise
    t.draw() # THEN draw signal (with opacity controlled)

while True:
    DrawNoisyGratingStim(Signal1, Noise1)
    DrawNoisyGratingStim(Signal2, Noise2)
    DrawNoisyGratingStim(Signal3, Noise3)
    DrawNoisyGratingStim(Signal4, Noise4)
    DrawNoisyGratingStim(Signal5, Noise5)
    DrawNoisyGratingStim(Signal6, Noise6)
    DrawNoisyGratingStim(Signal7, Noise7)
    DrawNoisyGratingStim(Signal8, Noise8)
    
    win.flip()
    keys = event.getKeys()
    for key in keys:
        if key == 'escape':  # Exit the program on pressing Esc key
            break
            
core.quit()

