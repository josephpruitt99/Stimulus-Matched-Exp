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
expName = 'exp5'  # from the Builder filename that created this script
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

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = False

# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking SR Research

ioConfig['eyetracker.hw.sr_research.eyelink.EyeTracker'] = {
    'name': 'tracker',
    'model_name': 'EYELINK 1000 DESKTOP',
    'simulation_mode': False,
    'network_settings': '100.1.1.1',
    'default_native_data_file_name': 'EXPFILE',
    'runtime_settings': {
        'sampling_rate': 1000.0,
        'track_eyes': 'RIGHT_EYE',
        'sample_filtering': {
            'sample_filtering': 'FILTER_LEVEL_2',
            'elLiveFiltering': 'FILTER_LEVEL_OFF',
        },
        'vog_settings': {
            'pupil_measure_types': 'PUPIL_AREA',
            'tracking_mode': 'PUPIL_CR_TRACKING',
            'pupil_center_algorithm': 'CENTROID_FIT',
        }
    }
}

'''
# Setup eyetracking MOUSE GAZE
ioConfig['eyetracker.hw.mouse.EyeTracker'] = {
    'name': 'tracker',
    'controls': {
        'move': [],
        'blink':('MIDDLE_BUTTON',),
        'saccade_threshold': 0.5,
    }
}
'''

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=20.0, fillColor='', borderColor='black', lineWidth=20.0,
    innerRadius=20.0, innerFillColor='green', innerBorderColor='black', innerLineWidth=20.0,
    colorSpace='rgb', units=None
)

# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='NINE_POINTS', randomisePos=True, textColor='white',
    movementAnimation=True, targetDelay=1.0
)

# run calibration
calibration.run()

defaultKeyboard.clearEvents()

#Initialize 'Instructions' Routine
X = 128

noiseTexture = np.random.random([X,X])*2.-1.
gaborTexture = (
    visual.filters.makeGrating(res=X, cycles=X * .05) *
    visual.filters.makeMask(matrixSize=X, shape="gauss", range=[0, 1])
)

# Create text stimuli
instruction1 = visual.TextStim(win, text='Use the left and right arrow keys to read the instructions', pos=(0, 300), height=40, color='black')
instruction2 = visual.TextStim(win, text='In this experiment, you will be making judgements about whether a signal was absent or present. Here is an example of a present signal (see left) and an absent signal (see right).', pos=(0, 300), height=40, color='black')
instruction3 = visual.TextStim(win, text='At the start of a trial, two arrows will point to a location on the screen that you should attend to. \nKeep your eyes on the fixation cross while attending to the patch.', pos=(0,300), height=40,color='black')
instruction4 = visual.TextStim(win, text='After a brief delay, you will be presented with two patches on each side of the screen.', pos=(0, 300), height=40, color='black')
instruction5 = visual.TextStim(win, text='Your task is to determine whether a signal was present. \nThe patch you will respond about will be indicated by two arrows that will reappear.', pos=(0, 300), height=40, color='black')
instruction6 = visual.TextStim(win, text='The response patch may or may not be the same patch you were cued to attend to at the beginning of the trial.\nPlease only respond about the patch indicated at the end of the trial.', pos=(0, 300), height=40, color='black')
instruction7 = visual.TextStim(win, text='TO SUMMARIZE, there will be two patches displayed on the screen. Your task is to attend to the one that you are cued to before the trial. You will then make your judgement based on the signal being present or absent in the patch that is cued after the trial.\nMost of the time, the  pre- and post-cue patch will be the same, but sometimes they will not.', pos=(0, 300), height=35, color='black')
instruction8 = visual.TextStim(win, text="Please use the '1' and '2' buttons on the left side of the keyboard, NOT on the number pad", pos=(0, 300), height=40, color='black')
instruction9 = visual.TextStim(win, text='Please keep your eyes on the fixation cross the entire time. If you move your eyes from the fixation, a message will pop up on the screen to alert you.\nPress "SPACE" to begin a practice block', pos=(0, 300), height=40, color='black')


#Create Task Stimuli
sf = 0.03 
contrast = 1.0  
noise_level = 0.3  
noise_size = 128
arrowVert = [(-0.4,0.05),(-0.4,-0.05),(-.2,-0.05),(-.2,-0.1),(0,0),(-.2,0.1),(-.2,0.05)]

Signal = visual.GratingStim(win, tex=gaborTexture, mask=None, sf=None, size=(128,128), pos=(-400, 0),
     opacity=0.2, contrast=1, units='pix', blendmode='avg')

Noise1 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(-400,0), contrast=1)
Noise2 = visual.GratingStim(win, tex=noiseTexture, mask='gauss', size=(128,128), pos=(400,0), contrast=1)

FixationCross = visual.ShapeStim(
    win=win, vertices='cross',
    size=(50, 50),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, units = 'pix', interpolate=True)
    
PreCueArrowDown = visual.ShapeStim(
    win=win, name='PreCueArrowDown', vertices=arrowVert,
    size=(250,250),
    ori=90.0, pos=[-400,300], anchor='center',
    lineWidth=2.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
PreCueArrowUp = visual.ShapeStim(
    win=win, name='PreCueArrowUp', vertices=arrowVert,
    size=(250,250),
    ori=-90.0, pos=[-400,-300], anchor='center',
    lineWidth=2.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
    
PostCueArrowDown = visual.ShapeStim(
    win=win, name='PostCueArrowDown', vertices=arrowVert,
    size=(250,250),
    ori=90.0, pos=[400,300], anchor='center',
    lineWidth=2.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
PostCueArrowUp = visual.ShapeStim(
    win=win, name='PostCueArrowUp', vertices=arrowVert,
    size=(250,250),
    ori=-90.0, pos=[400,-300], anchor='center',
    lineWidth=2.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)

fb_msg=''

SignalPresent = visual.TextStim(win, text="WAS THE SIGNAL PRESENT?\nYES (1) OR NO (2)", pos=(0,-300), height=32, color='black')
SignalPresent_stair = visual.TextStim(win, text=fb_msg, pos=(0,-300), height=32, color='black')

# Set initial visibility
instruction1.setAutoDraw(True)
instruction2.setAutoDraw(False)
instruction3.setAutoDraw(False)
instruction4.setAutoDraw(False)
instruction5.setAutoDraw(False)
instruction6.setAutoDraw(False)
instruction7.setAutoDraw(False)
instruction8.setAutoDraw(False)
instruction9.setAutoDraw(False)

FixationCross.setAutoDraw(True)

instructions = [instruction1, instruction2, instruction3, instruction4,instruction5, instruction6, instruction7, instruction8, instruction9]
num_instructions = len(instructions)
current_instruction_index = 0

# Respond to key presses
def toggle_instructions(key):
    global current_instruction_index
    instructions[current_instruction_index].setAutoDraw(False)
    if key == 'left':  # Flip to the previous instruction
        current_instruction_index = (current_instruction_index - 1) % num_instructions
    elif key == 'right':  # Flip to the next instruction
        current_instruction_index = (current_instruction_index + 1) % num_instructions
    instructions[current_instruction_index].setAutoDraw(True)

def DrawNoisyGratingStim(t, n):
    n.draw() # FIRST draw noise
    t.draw() # THEN draw signal (with opacity controlled)
# Display the stimuli

while True:
    win.flip()
    keys = event.getKeys()
    
    noiseTexture = np.random.random([X,X])*2.-1.
    gaborTexture = (
    visual.filters.makeGrating(res=X, cycles=X * .05) *
    visual.filters.makeMask(matrixSize=X, shape="circle", range=[0, 1])
    )
    
    for key in keys:
        if key == 'left' or key == 'right':  # Change the keys according to your preference
            toggle_instructions(key)
        if key == 'escape':  # Exit the program on pressing Esc key
            break
    if current_instruction_index == 1:
        DrawNoisyGratingStim(Signal, Noise1)
        Noise2.draw()
    if current_instruction_index == 2:
        PreCueArrowUp.draw()
        PreCueArrowDown.draw()
    if current_instruction_index == 3:
        DrawNoisyGratingStim(Signal, Noise1)
        Noise2.draw()
    if current_instruction_index == 4:
        PreCueArrowUp.draw()
        PreCueArrowDown.draw()
        SignalPresent.draw()
    if current_instruction_index == 5:
        PostCueArrowUp.draw()
        PostCueArrowDown.draw()
        SignalPresent.draw()
    if 'space' in keys:
        instructions[current_instruction_index].setAutoDraw(False)
        break
    if 'escape' in keys:
        win.close()
        core.quit()
win.flip()

Position=[0,0]

#Practice Block at 5 degrees

conditions = [{"Signal": "Present", "correct_answer": 1, "Position":-279,"Cue":"Valid"},
        {"Signal": "Absent", "correct_answer": 1, "Position":279, "Cue":"Valid"},
        {"Signal": "Present", "correct_answer": 2, "Position":-279,"Cue":"Invalid"},
        {"Signal": "Absent", "correct_answer": 2, "Position":279,"Cue":"Invalid"}]

def practice_routine(condition):
    trial_clock = core.Clock()
    FixationCross.setAutoDraw(True)
    while True:
        #Setup Stimuli
        win.flip()
        XPos = condition["Position"]
        PreCueArrowUp.setPos([XPos,-300])
        PreCueArrowDown.setPos([XPos,300])
        Signal.setPos([XPos,0])
        Noise1.setPos([XPos,0])
        oppositePosition = -XPos
        Noise2.setPos([oppositePosition,0])
        feedback_text = visual.TextStim(win, text='', pos=(0,300), color='black')
        if condition["Cue"] == "Valid":
            PostCueArrowUp.setPos([XPos,-300])
            PostCueArrowDown.setPos([XPos,300])
        elif condition["Cue"] == "Invalid":
            PostCueArrowUp.setPos([oppositePosition,-300])
            PostCueArrowDown.setPos([oppositePosition,300])
        trial_clock.reset()
        
        #Present or Absent Signal
        if condition["Signal"] == "Present":
            Signal.setOpacity(0.2)
        elif condition["Signal"] == "Absent":
            Signal.setOpacity(0)
        
        PreCueArrowUp.draw()
        PreCueArrowDown.draw()
        win.flip()
        
        #Draw Arrows and Stimuli
        while trial_clock.getTime() < 2:
            pass
        
        PreCueArrowUp.setAutoDraw(False)
        PreCueArrowDown.setAutoDraw(False)
        DrawNoisyGratingStim(Signal, Noise1)
        Noise2.draw()
        win.flip()
        
        while trial_clock.getTime() > 2 and trial_clock.getTime() < 2.3:
            pass
        
        Signal.setAutoDraw(False)
        Noise1.setAutoDraw(False)
        Noise2.setAutoDraw(False)
        PostCueArrowUp.draw()
        PostCueArrowDown.draw()
        SignalPresent.draw()
        win.flip()
        
        trial_clock.reset()
        response = event.getKeys()
        event.waitKeys()
        
        #Response
        break

for condition in conditions:
    practice_routine(condition)

#Post-Practice Questions
while True:
    keys = event.getKeys()
    questionsText = visual.TextStim(win, text="Please notify the researcher if you have any further questions before you begin the main task. Between each block you will have a 2-minute break; please open the door and notify the researcher when your break is over.", pos=(0,300), height=40, color='black')
    tryYourBest = visual.TextStim(win, text="We thank you for your participation in this experiment. You might find some trials hard to answer, but please your try your best. Press 'SPACE' to start.", pos=(0,-300), height=40, color='black')
    questionsText.draw()
    win.flip()
    
    if 'escape' in keys:
        win.close()
        core.quit()
        
    event.waitKeys()
        
    break

win.flip()

#Initialize Staircase Components
respText = visual.TextStim(win=win, name='respText',
    text= '1',
    font='Open Sans',
    pos=(0, --300), height=32.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);


#eyetracking
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start Only'
)

etRecord.status = STARTED

roi = visual.ROI(win, name='roi', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=(0, 0), size=(250,250), anchor='center', ori=0.0, units='pix')

win.mouseVisible = True

#Call Trials
def valid_trial_stair(XPos, invPos):
    random_side = random.randint(1,2)
    if random_side == 1:
        PreCueArrowUp.setPos([XPos,-300])
        PreCueArrowDown.setPos([XPos,300])
        PostCueArrowUp.setPos([XPos,-300])
        PostCueArrowDown.setPos([XPos,300])
        Signal.setPos([XPos, 0])
        Noise1.setPos([XPos, 0])
        Noise2.setPos([invPos, 0])
    elif random_side == 2:
        PreCueArrowUp.setPos([invPos,-300])
        PreCueArrowDown.setPos([invPos,300])
        PostCueArrowUp.setPos([invPos,-300])
        PostCueArrowDown.setPos([invPos,300])
        Signal.setPos([invPos, 0])
        Noise1.setPos([invPos, 0])
        Noise2.setPos([XPos, 0])

def invalid_trial_stair(XPos, invPos):
    random_side = random.randint(1,2)
    if random_side == 1:
        PreCueArrowUp.setPos([XPos,-300])
        PreCueArrowDown.setPos([XPos,300])
        PostCueArrowUp.setPos([invPos,-300])
        PostCueArrowDown.setPos([invPos,300])
        Signal.setPos([invPos, 0])
        Noise1.setPos([invPos, 0])
        Noise2.setPos([XPos, 0])
    elif random_side == 2:
        PreCueArrowUp.setPos([invPos,-300])
        PreCueArrowDown.setPos([invPos,300])
        PostCueArrowUp.setPos([XPos,-300])
        PostCueArrowDown.setPos([XPos,300])
        Signal.setPos([XPos, 0])
        Noise1.setPos([XPos, 0])
        Noise2.setPos([invPos, 0])

#Staircase
stairConditions = data.importConditions('stairConditions.xlsx')
trials = data.MultiStairHandler(stairType='QUEST', name='trials',
    nTrials=75,
    conditions=stairConditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials)  # add the loop to the experiment
# initialise values for first condition
level = trials._nextIntensity  # initialise some vals
condition = trials.currentStaircase.condition
total_trial_rep = 0 
response = keyboard.Keyboard()
stairValues_High = []
stairValues_Low = []

for level, condition in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    curr_trial_rep = 0
    eye_ok = False
    stair_clock = core.Clock()
    ISI = core.Clock()
    
    while not eye_ok: 
        # --- Prepare to start Routine "Staircase" ---
        stair_clock.reset()
        curr_trial_rep+=1
        
        continueRoutine = True
        routineForceEnded = False
        
        # update component parameters for each repeat
        contrastLVL = []
        
        #Orietnation
        Mask_Ori = random.randint(1,2)
        Mask_Ori_rand = 0
        if Mask_Ori == 1:
            Mask_Ori_rand = -45
        elif Mask_Ori == 2:
            Mask_Ori_rand = 45
        
        #Present or Absent Signal
        present_or_absent = random.randint(1,2)
        
        if  present_or_absent == 1:
            signalOpacity = level
            correctAnswer = '1'
        else:
            signalOpacity = 0
            correctAnswer = '2'
        
        roi.reset()
        Signal.setOpacity(signalOpacity)
        Signal.setOri(Mask_Ori_rand)
        
        if condition["cue"] == "Valid":
            valid_trial_stair(1000, -1000)
        elif condition["cue"] == "Invalid":
            invalid_trial_stair(1000, -1000)

        stair_clock.reset()
    
        PreCueArrowUp.draw()
        PreCueArrowDown.draw()
        win.flip()
        
        #Draw Arrows and Stimuli
        while stair_clock.getTime() < 1:
            pass
        
        roi.setAutoDraw(True)
        PreCueArrowUp.setAutoDraw(False)
        PreCueArrowDown.setAutoDraw(False)
        DrawNoisyGratingStim(Signal, Noise1)
        Noise2.draw()
        win.flip()
        
        if roi.isLookedIn:
            roi.wasLookedIn = True 
        else:
            roi.wasLookedIn = False 

        if roi.wasLookedIn == True:
            SignalPresent.setText("WAS THE SIGNAL \nPRESENT (1) OR ABSENT (2)?")
            eye_ok = True
        else:
            SignalPresent.setText('KEEP YOUR EYES ON THE FIXATION CROSS')
            eye_ok = False

        while stair_clock.getTime() > 1 and stair_clock.getTime() < 1.3:
            pass
        
        roi.setAutoDraw(False)
        Signal.setAutoDraw(False)
        Noise1.setAutoDraw(False)
        Noise2.setAutoDraw(False)
        PostCueArrowUp.draw()
        PostCueArrowDown.draw()
        SignalPresent.draw()
        win.flip()
        
        waitOnFlip = False
        if response.status == NOT_STARTED and  stair_clock.getTime() > 1.3:
            stair_clock.reset()
            response.keys = []
            response.rt = []
            theseKeys_allKeys = []
            event.waitKeys()
            response.status == STARTED
    
            while True:
                    theseKeys = response.getKeys(keyList=['1', '2', 'escape'], waitRelease=False, clear=True)
                    theseKeys_allKeys.extend(theseKeys)
                    
                    if 'escape' in theseKeys:
                        win.close()
                        core.quit()
                        
                    if theseKeys:
                        response.keys = theseKeys[-1].name  # just the last key pressed
                        response.rt = theseKeys[-1].rt

                    if response.keys in ['1', '2']:
                        if response.keys == correctAnswer:
                            response.corr = 1
                            continueRoutine = False
                        else:
                            response.corr = 0
                            continueRoutine = False

                        if not continueRoutine:
                            break
        
        thisExp.addData('signalOpacity', signalOpacity)
        
        thisExp.addData('level', level)
        
        if condition['label'] == 'low_opac_v':
            stairValues_Low.append(trials.intensity)
        elif condition['label'] == 'high_opac_v':
            stairValues_High.append(trials.intensity)
    
        #cheatNoise.stop()  # ensure sound has stopped at end of routine
        # the Routine "Staircase" was not non-slip safe, so reset the non-slip timer
    
    # store data for trials (MultiStairHandler)
    total_trial_rep += (curr_trial_rep-1)
    print(f'{eye_ok}')
    trials.addResponse(response.corr, level)
    trials.addOtherData('stair_response', theseKeys_allKeys[-1].name)
    trials.addOtherData('stair_rt', response.rt)
    trials.addOtherData('stair_correct', response.corr)
    thisExp.addData('stair_eye_ok', eye_ok)
    
    ISI.reset()
    SignalPresent.setText(" ")
    win.flip()
    while ISI.getTime() < 1:
        pass
    # the Routine "Staircase" was not non-slip safe, so reset the non-slip timer
    thisExp.nextEntry()

print(stairValues_Low)
print(stairValues_High)

while 0 in stairValues_Low:
    stairValues_Low.remove(0)

while 0 in stairValues_High:
    stairValues_High.remove(0)
    
etRecord2 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Stop Only'
)

high_opac = stairValues_High[-5:]
low_opac = stairValues_Low[-5:]

stairOpacity = (np.mean(high_opac) + np.mean(low_opac)) / 2
print(signalOpacity)

etRecord.status = FINISHED
etRecord2.status = STARTED
etRecord2.status = FINISHED

slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(600,150), pos=(0, 0), units=None,
    labels=('1: not at all confident', '2: somewhat confident', '3: quite confident', '4: extremely confident'), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Black', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=30.0,
    flip=False, ori=0.0, depth=-1, readOnly=False)
    
while True:
        keys = event.getKeys()
        FixationCross.setAutoDraw(False)
        stairbreakText = visual.TextStim(win, text="In addition to the task you just completed, the next 6 sessions will also include a confidence judgement after your response. \nPlease use your mouse to respond how confident you are in your judgement on a scale from 1 to 4. \nPress 'SPACE' to continue ", height=40, pos=(0,400), color='black')
        stairbreakText.setAutoDraw(True)
        slider.setAutoDraw(True)
        win.flip()
        if 'escape' in keys:
                core.quit()
        
        event.waitKeys()
        FixationCross.setAutoDraw(True)
        slider.setAutoDraw(False)
        stairbreakText.text = ""
        win.flip()
        break
        
#Post-Staircase Break
def break_screen():
    while True:
        keys = event.getKeys()
        stairbreakText = visual.TextStim(win, text="You now have a 2-minute break before your next session", pos=(0,300), height=40, color='black')
        stairbreakText.setAutoDraw(True)
        timer_text = visual.TextStim(win, text='', pos=(0,-300), height=40, color='black')
        duration = 120
        timer = core.Clock()
        
        if 'escape' in keys:
                core.quit()
                
        # Start the timer
        timer.reset()

        # Main loop
        while timer.getTime() < duration:
            remaining_time = int(duration - timer.getTime())
            timer_text.text = 'Break Time: {} seconds'.format(remaining_time)
            timer_text.draw()
            win.flip()
        
        stairbreakText.text = "Break Complete! Press 'SPACE' to begin the next session."
        
        event.waitKeys()
        stairbreakText.text = ""
        win.flip()
        break

#Main Task
condition_file = 'conditions.xlsx'
conditions = data.importConditions(condition_file)

# Set the number of trials per break and the total number of breaks
num_trials = 176
num_breaks = 6

def valid_trial():
    PreCueArrowUp.setPos([XPos,-300])
    PreCueArrowDown.setPos([XPos,300])
    PostCueArrowUp.setPos([XPos,-300])
    PostCueArrowDown.setPos([XPos,300])
    Signal.setPos([XPos, 0])
    Noise1.setPos([XPos, 0])
    Noise2.setPos([invPos, 0])

def invalid_trial():
    PreCueArrowUp.setPos([XPos,-300])
    PreCueArrowDown.setPos([XPos,300])
    PostCueArrowUp.setPos([invPos,-300])
    PostCueArrowDown.setPos([invPos,300])
    Signal.setPos([invPos, 0])
    Noise1.setPos([invPos, 0])
    Noise2.setPos([XPos, 0])

def zero_trial():
    PreCueArrowUp.setPos([XPos,-300])
    PreCueArrowDown.setPos([XPos,300])
    PostCueArrowUp.setPos([XPos,-300])
    PostCueArrowDown.setPos([XPos,300])
    Signal.setPos([XPos, 0])
    Noise1.setPos([XPos, 0])
    Noise2.setPos([4000,500]) #off screen

'''main_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=conditions,
    seed=None, name='main_trials')
thisExp.addLoop(main_trials)  # add the loop to the experiment
thisTrial = main_trials.trialList[0]  # so we can initialise stimuli with some values'''

for break_num in range(num_breaks):
    #break
    break_screen()
    win.flip()
    
    # Shuffle conditions
    conditions = np.random.permutation(conditions)
        
    # Main loop for trials within each break
    for trial_num in range(num_trials):
        # Get the current condition for this trial
        current_condition = conditions[trial_num]
        etRecord.status = STARTED
        FixationCross.setAutoDraw(True)
        curr_trial_rep = 0
        # Present the trial
        eye_ok = False
        stair_clock = core.Clock()
        ISI = core.Clock()
        conf_clock = core.Clock()
        while not eye_ok: 
            win.mouseVisible = False
            stair_clock.reset()
            curr_trial_rep+=1
            win.mouseVisible = True
            continueRoutine = True
            routineForceEnded = False
            
            # update component parameters for each repeat
            contrastLVL = []
            
            #Orietnation
            Mask_Ori = random.randint(1,2)
            Mask_Ori_rand = 0
            if Mask_Ori == 1:
                Mask_Ori_rand = -45
            elif Mask_Ori == 2:
                Mask_Ori_rand = 45
            
            #Present or Absent Signal
            present_or_absent = random.randint(1,2)
            
            if current_condition['Stimulus'] == 'signal':
                signalOpacity = stairOpacity
                correctAnswer = '1'
            elif current_condition['Stimulus'] == 'noise':
                signalOpacity = 0
                correctAnswer = '2'
            
            roi.reset()
            Signal.setOpacity(signalOpacity)
            Signal.setOri(Mask_Ori_rand)
            XPos = current_condition["position"]
            invPos = -XPos
            
            if current_condition["position"] == 0:
                zero_trial()
            elif current_condition["cue"] == "Valid":
                valid_trial()
            elif current_condition["cue"] == "Invalid":
                invalid_trial()
            
            stair_clock.reset()
        
            PreCueArrowUp.draw()
            PreCueArrowDown.draw()
            win.flip()
            
            #Draw Arrows and Stimuli
            while stair_clock.getTime() < 1:
                pass
            
            roi.setAutoDraw(True)
            PreCueArrowUp.setAutoDraw(False)
            PreCueArrowDown.setAutoDraw(False)
            DrawNoisyGratingStim(Signal, Noise1)
            Noise2.draw()
            
            if current_condition['position'] == 0:
                FixationCross.setAutoDraw(False)

            win.flip()
            
            if roi.isLookedIn:
                roi.wasLookedIn = True 
            else:
                roi.wasLookedIn = False 

            if roi.wasLookedIn == True:
                SignalPresent.setText("WAS THE SIGNAL \nPRESENT (1) OR ABSENT (2)?")
                eye_ok = True
            else:
                SignalPresent.setText('KEEP YOUR EYES ON THE FIXATION CROSS')
                eye_ok = False

            while stair_clock.getTime() > 1 and stair_clock.getTime() < 1.3:
                pass
            
            roi.setAutoDraw(False)
            Signal.setAutoDraw(False)
            Noise1.setAutoDraw(False)
            Noise2.setAutoDraw(False)
            PostCueArrowUp.draw()
            PostCueArrowDown.draw()
            SignalPresent.draw()
            
            if current_condition['position'] == 0:
                FixationCross.setAutoDraw(True)
                
            win.flip()
            
            waitOnFlip = False
            if response.status == NOT_STARTED and stair_clock.getTime() > 1.3:
                stair_clock.reset()
                response.keys = []
                response.rt = []
                theseKeys_allKeys = []
                event.waitKeys()
                response.status == STARTED
                
                while True:
                    theseKeys = response.getKeys(keyList=['1', '2', 'escape'], waitRelease=False, clear=True)
                    theseKeys_allKeys.extend(theseKeys)
                        
                    if 'escape' in theseKeys:
                        win.close()
                        core.quit()
                        
                    if theseKeys:
                        response.keys = theseKeys[-1].name  # just the last key pressed
                        response.rt = theseKeys[-1].rt

                    if response.keys in ['1', '2']:
                        if response.keys == correctAnswer:
                            response.corr = 1
                            confRoutine = True
                            break
                        else:
                            response.corr = 0
                            confRoutine = True
                            break

            if eye_ok == True:
                while confRoutine is True:
                    conf_clock.reset
                    win.mouseVisible = True
                    slider.setAutoDraw(True)
                    FixationCross.setAutoDraw(False)
                    win.flip()
                    
                    if slider.getRating() is not None:
                        conf_rt = conf_clock.getTime()
                        slider.setAutoDraw(False)
                        FixationCross.setAutoDraw(True)
                        confRoutine = False
                        
            
        thisExp.addData('nTrial', (int(trial_num)+1)*break_num)
        thisExp.addData('position', current_condition['position'])
        thisExp.addData('validity', current_condition['cue'])
        thisExp.addData('Stimulus', current_condition['Stimulus'])
        thisExp.addData('orientation', Mask_Ori_rand)
        thisExp.addData('response_key', response.keys)
        thisExp.addData('response_rt', response.rt)
        thisExp.addData('response_correct', response.corr)
        thisExp.addData('confidence', slider.getRating())
        thisExp.addData('confidence_rt', conf_rt)
        thisExp.addData('eye_ok', eye_ok)
        thisExp.addData('trial_rep', curr_trial_rep)
        
        # Clear the screen before the next trial
        slider.reset()
        ISI.reset()
        SignalPresent.setText(" ")
        win.flip()
        while ISI.getTime() < 1:
            pass
        
        thisExp.nextEntry()

etRecord.status = FINISHED
etRecord2.status = STARTED
etRecord2.status = FINISHED

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)

while True:
    keys = event.getKeys()
    endText = visual.TextStim(win, text="You have completed this experiment. Thank you for your participation. Please notify the researcher.", pos=(0,300), color='black')
    endText.draw()
    win.flip()
    event.waitKeys()
    
    break

core.quit()