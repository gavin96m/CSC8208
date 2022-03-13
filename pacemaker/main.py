from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import json
import os
import base64


class appDCM:

    # imageDirectory = "./images"
    # logoFile = "/.png"

    userDirectory = "./user"
    userloginFile = "/userlogin.json"

    def __init__(self):
        self.checkUserDirectory()

        self.root = Tk()
        self.root.title("CSC8208")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure((0, 2), weight=1)
        self.root.rowconfigure(1, weight=3)

        self.createHeaderScreen()

        self.createLoginScreen()

        self.root.mainloop()


    def checkUserDirectory(self, defaultUsername=""):
        self.jsonUserlogin = {}
        if not os.path.exists(self.userDirectory):
            print("make " + self.userDirectory + " subdirectory")
            os.mkdir(self.userDirectory)

        if os.path.isfile(self.userDirectory + self.userloginFile):
            with open(self.userDirectory + self.userloginFile, "r") as fileIn:
                try:
                    self.jsonUserlogin = json.load(fileIn)
                    print("able to read .json file")
                    if ("default" not in self.jsonUserlogin or not isinstance(self.jsonUserlogin["default"], str)):
                        self.jsonUserlogin["default"] = defaultUsername
                except:
                    print("cannot load .json file")
                    self.jsonUserlogin["default"] = defaultUsername
        else:
            self.jsonUserlogin["default"] = defaultUsername
        with open(self.userDirectory + self.userloginFile, "w") as fileOut:
            json.dump(self.jsonUserlogin, fileOut)
        return self.jsonUserlogin["default"]


    def checkRowValue(self, rowValue):
        if not (rowValue == "top" or rowValue == "mid" or rowValue == "bot"):
            raise ValueError('<row> value must be either "top", "mid", or "bot"')
        else:
            if (rowValue == "top"):
                return 0
            if (rowValue == "bot"):
                return 2
            return 1

    def checkScreenExist(self, screenName):
        try:
            return screenName in self.screenDictionary
        except:
            self.screenDictionary = {"top": None, "mid": None, "bot": None}
            return False

    def addScreen(self, screenName, frame):
        if not self.checkScreenExist(screenName):
            self.screenDictionary[screenName] = frame

    def displayScreen(self, screenName, rowValue="mid"):
        if screenName in self.screenDictionary:
            self.checkRowValue(rowValue)
            if self.screenDictionary.get(rowValue) is not None:
                self.screenDictionary[rowValue].grid_forget()
            self.screenDictionary[rowValue] = self.screenDictionary[screenName]
            self.screenDictionary[rowValue].grid(row=self.checkRowValue(rowValue), column=0, sticky=W + E + N + S)
            self.rootWindowResize()
            return True
        else:
            print(screenName + " does not exist")
            return False

    def rootWindowResize(self):
        self.root.update()
        self.root.minsize(self.root.winfo_reqwidth(), self.root.winfo_reqheight())
        self.root.geometry('%dx%d' % (self.root.winfo_reqwidth(), self.root.winfo_reqheight()))
        self.root.resizable(1, 1)


    def createFont(self, name, fontName, size, weight="normal"):
        try:
            self.fontDictionary[name] = (fontName, size, weight)
        except:
            self.fontDictionary = {}
            self.fontDictionary[name] = (fontName, size, weight)

    def ttkCreateFont(self, name, fontName, size, weight="normal"):
        try:
            self.ttkStyle.configure(name, font=(fontName, size, weight))
        except:
            self.ttkStyle = ttk.Style()
            self.ttkStyle.configure(name, font=(fontName, size, weight))


    def createHeaderScreen(self):
        if self.checkScreenExist("headerScreen"):
            print("header screen already exist")
            self.displayScreen("headerScreen", "top")
            return False
        else:
            self.headerFrame = Frame(self.root, padx=20, pady=0)
            self.addScreen("headerScreen", self.headerFrame)

            self.displayScreen("headerScreen", "top")
            print("header screen created successfully")
            return True


    def createLoginScreen(self):
        if self.checkScreenExist("loginScreen"):
            print("login screen already exist")
            self.displayScreen("loginScreen")
            return False
        else:
            self.loginFrame = Frame(self.root, padx=20, pady=10)
            self.loginFrame.columnconfigure((1, 2), weight=1)
            self.loginFrame.rowconfigure((0, 1, 3), weight=1)
            self.addScreen("loginScreen", self.loginFrame)


            self.createFont("loginTitleFont", "TkDefaultFont", 30, "bold")
            self.createFont("loginFont", "TkDefaultFont", 12)
            self.ttkCreateFont("loginButton.TButton", "TkDefaultFont", 20, "bold")


            self.loginTitle = Label(self.loginFrame, text="Pacemaker Monitor", font=self.fontDictionary["loginTitleFont"],
                                    height=2)

            self.usernameLabel = Label(self.loginFrame, text="Username", font=self.fontDictionary["loginFont"])
            self.passwordLabel = Label(self.loginFrame, text="Password", font=self.fontDictionary["loginFont"])
            self.usernameEntry = ttk.Entry(self.loginFrame, font=self.fontDictionary["loginFont"])
            self.passwordEntry = ttk.Entry(self.loginFrame, font=self.fontDictionary["loginFont"], show="*")

            self.loginButton = ttk.Button(self.loginFrame, text="Login", style="loginButton.TButton",
                                          command=lambda: self.loginUser())
            self.rememberMeButton = ttk.Checkbutton(self.loginFrame, text="Remember Me")
            # self.smallRegisterButton = ttk.Button(self.loginFrame, text="Register",
            #                                       command=lambda: self.createRegisterScreen())

            self.loginTitle.grid(row=0, columnspan=3, sticky=N)

            self.usernameLabel.grid(row=1, sticky=E + S)
            self.passwordLabel.grid(row=2, sticky=E + N)
            self.usernameEntry.grid(row=1, column=1, columnspan=2, padx=5, pady=2, sticky=W + E + S)
            self.passwordEntry.grid(row=2, column=1, columnspan=2, padx=5, pady=2, sticky=W + E + N)

            self.loginButton.grid(row=3, columnspan=3, sticky=W + E + N + S, pady=10)
            self.rememberMeButton.grid(row=4, column=0, columnspan=2, sticky=W)
            #self.smallRegisterButton.grid(row=4, column=1, columnspan=2, sticky=E)

            # assign variable to entry
            self.usernameStr = StringVar()
            self.passwordStr = StringVar()
            self.usernameEntry.configure(textvariable=self.usernameStr)
            self.passwordEntry.configure(textvariable=self.passwordStr)

            # check for Remember Me username
            self.usernameStr.set(self.getUserlogin("default"))
            if (self.usernameStr.get() == ""):
                self.setButtonState(self.rememberMeButton, '!selected')
            else:
                self.setButtonState(self.rememberMeButton)


            self.displayScreen("loginScreen")
            print("login screen created successfully")
            return True


    def passwordHiding(self, string):
        if not isinstance(string, str):
            raise TypeError('<string> parameter must be type "str"')
        else:
            return str(base64.b64encode(string.encode()))

    def loginUser(self):
        tempPassword = self.passwordHiding(self.passwordStr.get())
        self.passwordStr.set("")

        if (self.usernameStr.get() in self.jsonUserlogin and tempPassword == self.jsonUserlogin[
            self.usernameStr.get()]):
            self.currentUsername = self.usernameStr.get()

            if not (self.rememberMeButton.state() == ()):
                self.setUserlogin("default", self.usernameStr.get())
            else:
                self.setUserlogin("default", "")
                self.usernameStr.set("")

            self.createProgramScreen()
            self.createEgram1()
            self.createEgram2()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")


    def getUserlogin(self, username):
        with open(self.userDirectory + self.userloginFile, "r") as fileIn:
            self.jsonUserlogin = json.load(fileIn)
        return self.jsonUserlogin[username]

    def setUserlogin(self, username, password):
        self.jsonUserlogin[username] = password
        with open(self.userDirectory + self.userloginFile, "w") as fileOut:
            json.dump(self.jsonUserlogin, fileOut)

    def setButtonState(self, button, state='selected'):
        if not ("alternate" in state):
            button.state(['!alternate'])
        button.state([state])


    def createProgramScreen(self):
        if self.checkScreenExist("programScreen"):
            print("program screen already exist")
            self.displayScreen("programScreen")

            self.readUserData(self.currentUsername)
            return False
        else:
            self.programFrame = Frame(self.root, padx=20, pady=10)
            self.programFrame.columnconfigure(0, weight=1)
            self.addScreen("programScreen", self.programFrame)

            self.createFont("programFont", "TkDefaultFont", 30, "bold")
            self.programTitle = Label(self.programFrame, text="Pacemaker Monitor",
                                      font=self.fontDictionary["programFont"])
            self.programTitle.grid(row=0)

            self.notebook = ttk.Notebook(self.programFrame)
            self.notebook.grid(row=1, column=0, padx=0, pady=0, sticky=W + E + N + S)


            self.paceSettingFrame = Frame(self.notebook)
            self.paceSettingFrame.columnconfigure((1, 3, 5), weight=1)
            self.notebook.add(self.paceSettingFrame, text="Pace Setting", padding=(10, 10))
            self.egramFrame = Frame(self.notebook)
            self.notebook.add(self.egramFrame, text="ECG", padding=(10, 10))
            #self.aboutAppFrame = Frame(self.notebook)
            #self.notebook.add(self.aboutAppFrame, text="Board Details", padding=(10, 10))


            self.pacingModeFrame = Frame(self.paceSettingFrame)
            self.programModeLabel = Label(self.pacingModeFrame, text="Select Pacing Mode:", pady=10)
            self.programModeLabel.grid(row=0, column=0, padx=5)
            self.programModeCombobox = ttk.Combobox(self.pacingModeFrame, state="readonly", width=6)
            self.programModeCombobox.grid(row=0, column=1)
            self.programModeCombobox['values'] = (
            'OFF', 'AAT', 'VVT', 'AOO', 'AAI', 'VOO', 'VVI', 'VDD', 'DOO', 'DDI', 'DDD')


            self.lowerRateLimitFrame = Frame(self.paceSettingFrame)
            self.upperRateLimitFrame = Frame(self.paceSettingFrame)
            #self.maximumSensorRateFrame = Frame(self.paceSettingFrame)
            self.fixedAVDelayFrame = Frame(self.paceSettingFrame)
            self.dynamicAVDelayFrame = Frame(self.paceSettingFrame)
            #self.minimumDynamicAVDelayFrame = Frame(self.paceSettingFrame)
            self.sensedAVDelayOffsetFame = Frame(self.paceSettingFrame)
            self.atrialAmplitudeFrame = Frame(self.paceSettingFrame)
            self.ventricularAmplitudeFrame = Frame(self.paceSettingFrame)
            #self.atrialAmplitudeUnregulatedFrame = Frame(self.paceSettingFrame)
            #self.ventricularAmplitudeUnregulatedFrame = Frame(self.paceSettingFrame)
            self.atrialPulseWidthFrame = Frame(self.paceSettingFrame)
            self.ventricularPulseWidthFrame = Frame(self.paceSettingFrame)
            self.atrialSensitivityFrame = Frame(self.paceSettingFrame)
            self.ventricularSensitivityFrame = Frame(self.paceSettingFrame)
            self.VRPFrame = Frame(self.paceSettingFrame)
            self.ARPFrame = Frame(self.paceSettingFrame)
            self.PVARPFrame = Frame(self.paceSettingFrame)
            self.PVARPExtensionFrame = Frame(self.paceSettingFrame)
            self.hysteresisFrame = Frame(self.paceSettingFrame)
            self.rateSmoothingFrame = Frame(self.paceSettingFrame)
            self.ATRDurationFrame = Frame(self.paceSettingFrame)
            self.ATRFallbackModeFrame = Frame(self.paceSettingFrame)
            self.ATRFallbackTimeFrame = Frame(self.paceSettingFrame)
            #self.ventricularBlankingFrame = Frame(self.paceSettingFrame)
            #self.activityThresholdFrame = Frame(self.paceSettingFrame)
            self.reactionTimeFrame = Frame(self.paceSettingFrame)
            self.responseFactorFrame = Frame(self.paceSettingFrame)
            self.recoveryTimeFrame = Frame(self.paceSettingFrame)


            self.label01 = Label(self.lowerRateLimitFrame, width=18, text="Lower Rate Limit")
            self.label02 = Label(self.upperRateLimitFrame, width=18, text="Upper Rate Limit")
            #self.label03 = Label(self.maximumSensorRateFrame, width=18, text="Maximum Sensor Rate")
            self.label04 = Label(self.fixedAVDelayFrame, width=18, text="Fixed AV Delay")
            self.label05 = Label(self.dynamicAVDelayFrame, width=18, text="Dynamic AV Delay")
            #self.label06 = Label(self.minimumDynamicAVDelayFrame, width=18, text="Minimum Dynamic\n AV Delay")
            self.label07 = Label(self.sensedAVDelayOffsetFame, width=18, text="Sensed AV Delay Offset")
            self.label08 = Label(self.atrialAmplitudeFrame, width=18, text="Atrial Amplitude")
            self.label09 = Label(self.ventricularAmplitudeFrame, width=18, text="Ventricular Amplitude")
            #self.label10 = Label(self.atrialAmplitudeUnregulatedFrame, width=18, text="Atrial Amplitude\n Unregulated")
            #self.label11 = Label(self.ventricularAmplitudeUnregulatedFrame, width=18,
            #                     text="Ventricular Amplitude\n Unregulated")
            self.label12 = Label(self.atrialPulseWidthFrame, width=18, text="Atrial Pulse Width")
            self.label13 = Label(self.ventricularPulseWidthFrame, width=18, text="Ventricular Pulse Width")
            self.label14 = Label(self.atrialSensitivityFrame, width=18, text="Atrial Sensitivity")
            self.label15 = Label(self.ventricularSensitivityFrame, width=18, text="Ventricular Sensitivity")
            self.label16 = Label(self.VRPFrame, width=18, text="VRP")
            self.label17 = Label(self.ARPFrame, width=18, text="ARP")
            self.label18 = Label(self.PVARPFrame, width=18, text="PVARP")
            self.label19 = Label(self.PVARPExtensionFrame, width=18, text="PVARP Extension")
            self.label20 = Label(self.hysteresisFrame, width=18, text="Hysteresis")
            self.label21 = Label(self.rateSmoothingFrame, width=18, text="Rate Smoothing")
            self.label22 = Label(self.ATRDurationFrame, width=18, text="ATR Duration")
            self.label23 = Label(self.ATRFallbackModeFrame, width=18, text="ATR Fallback Mode")
            self.label24 = Label(self.ATRFallbackTimeFrame, width=18, text="ATR Fallback Time")
            #self.label25 = Label(self.ventricularBlankingFrame, width=18, text="Ventricular Blanking")
            #self.label26 = Label(self.activityThresholdFrame, width=18, text="Activity Threshold")
            self.label27 = Label(self.reactionTimeFrame, width=18, text="Reaction Time")
            self.label28 = Label(self.responseFactorFrame, width=18, text="Response Factor")
            self.label29 = Label(self.recoveryTimeFrame, width=18, text="Recovery Time")


            self.entry01Str = StringVar()
            self.entry02Str = StringVar()
            self.entry03Str = StringVar()
            self.entry04Str = StringVar()
            self.entry05Str = StringVar()
            self.entry06Str = StringVar()
            self.entry07Str = StringVar()
            self.entry08Str = StringVar()
            self.entry09Str = StringVar()
            self.entry10Str = StringVar()
            self.entry11Str = StringVar()
            self.entry12Str = StringVar()
            self.entry13Str = StringVar()
            self.entry14Str = StringVar()
            self.entry15Str = StringVar()
            self.entry16Str = StringVar()
            self.entry17Str = StringVar()
            self.entry18Str = StringVar()
            self.entry19Str = StringVar()
            self.entry20Str = StringVar()
            self.entry21Str = StringVar()
            self.entry22Str = StringVar()
            self.entry23Str = StringVar()
            self.entry24Str = StringVar()
            self.entry25Str = StringVar()
            self.entry26Str = StringVar()
            self.entry27Str = StringVar()
            self.entry28Str = StringVar()
            self.entry29Str = StringVar()


            self.entry01 = Spinbox(self.lowerRateLimitFrame, state="readonly",
                                   values=(list(range(30, 51, 5)) + list(range(51, 90, 1)) + list(range(90, 176, 5))),
                                   width=8, textvariable=self.entry01Str)
            self.entry02 = Spinbox(self.upperRateLimitFrame, state="readonly", values=list(range(50, 176, 5)), width=8,
                                   textvariable=self.entry02Str)
            #self.entry03 = Spinbox(self.maximumSensorRateFrame, state="readonly", values=list(range(50, 176, 5)),
            #                       width=8, textvariable=self.entry03Str)
            self.entry04 = Spinbox(self.fixedAVDelayFrame, state="readonly", values=list(range(70, 301, 10)), width=8,
                                   textvariable=self.entry04Str)
            self.entry05 = Spinbox(self.dynamicAVDelayFrame, state="readonly", values=["OFF", "ON"], width=8,
                                   textvariable=self.entry05Str)
            #self.entry06 = Spinbox(self.minimumDynamicAVDelayFrame, state="readonly", values=list(range(30, 101, 10)),
            #                       width=8, textvariable=self.entry06Str)
            self.entry07 = Spinbox(self.sensedAVDelayOffsetFame, state="readonly",
                                   values=["OFF"] + list(np.arange(-10, -101, -10)), width=8,
                                   textvariable=self.entry07Str)
            self.entry08 = Spinbox(self.atrialAmplitudeFrame, state="readonly",
                                   values=["OFF"] + list(np.arange(0.5, 3.3, 0.1)) + list(np.arange(3.5, 7.5, 0.5)),
                                   width=8, textvariable=self.entry08Str)
            self.entry09 = Spinbox(self.ventricularAmplitudeFrame, state="readonly",
                                   values=["OFF"] + list(np.arange(0.5, 3.3, 0.1)) + list(np.arange(3.5, 7.5, 0.5)),
                                   width=8, textvariable=self.entry09Str)
            #self.entry10 = Spinbox(self.atrialAmplitudeUnregulatedFrame, state="readonly",
            #                       values=["OFF", 1.25, 2.5, 3.75, 5.0], width=8, textvariable=self.entry10Str)
            #self.entry11 = Spinbox(self.ventricularAmplitudeUnregulatedFrame, state="readonly",
            #                       values=["OFF", 1.25, 2.5, 3.75, 5.0], width=8, textvariable=self.entry11Str)
            self.entry12 = Spinbox(self.atrialPulseWidthFrame, state="readonly",
                                   values=[0.05] + list(np.arange(0.1, 2.0, 0.1)), width=8,
                                   textvariable=self.entry12Str)
            self.entry13 = Spinbox(self.ventricularPulseWidthFrame, state="readonly",
                                   values=[0.05] + list(np.arange(0.1, 2.0, 0.1)), width=8,
                                   textvariable=self.entry13Str)
            self.entry14 = Spinbox(self.atrialSensitivityFrame, state="readonly",
                                   values=[0.25, 0.5, 0.75] + list(np.arange(1.0, 10.5, 0.5)), width=8,
                                   textvariable=self.entry14Str)
            self.entry15 = Spinbox(self.ventricularSensitivityFrame, state="readonly",
                                   values=[0.25, 0.5, 0.75] + list(np.arange(1.0, 10.5, 0.5)), width=8,
                                   textvariable=self.entry15Str)
            self.entry16 = Spinbox(self.VRPFrame, state="readonly", values=list(range(150, 510, 10)), width=8,
                                   textvariable=self.entry16Str)
            self.entry17 = Spinbox(self.ARPFrame, state="readonly", values=list(range(150, 510, 10)), width=8,
                                   textvariable=self.entry17Str)
            self.entry18 = Spinbox(self.PVARPFrame, state="readonly", values=list(range(150, 510, 10)), width=8,
                                   textvariable=self.entry18Str)
            self.entry19 = Spinbox(self.PVARPExtensionFrame, state="readonly",
                                   values=["OFF"] + list(range(50, 450, 50)), width=8, textvariable=self.entry19Str)
            self.entry20 = Spinbox(self.hysteresisFrame, state="readonly",
                                   values=["OFF"] + list(range(30, 51, 5)) + list(range(51, 90, 1)) + list(
                                       range(90, 176, 5)), width=8, textvariable=self.entry20Str)
            self.entry21 = Spinbox(self.rateSmoothingFrame, state="readonly",
                                   values=["OFF"] + list(range(3, 24, 3)) + [25], width=8, textvariable=self.entry21Str)
            self.entry22 = Spinbox(self.ATRDurationFrame, state="readonly", values=["OFF", "ON"], width=8,
                                   textvariable=self.entry22Str)
            self.entry23 = Spinbox(self.ATRFallbackModeFrame, state="readonly",
                                   values=[10] + list(range(20, 100, 20)) + list(range(100, 2100, 100)), width=8,
                                   textvariable=self.entry23Str)
            self.entry24 = Spinbox(self.ATRFallbackTimeFrame, state="readonly", values=list(range(1, 6, 1)), width=8,
                                   textvariable=self.entry24Str)
            #self.entry25 = Spinbox(self.ventricularBlankingFrame, state="readonly", values=[30, 40, 50, 60], width=8,
            #                       textvariable=self.entry25Str)
            #self.entry26 = Spinbox(self.activityThresholdFrame, state="readonly",
            #                      values=["V-Low", "Low", "Med-Low", "Med", "Med-High", "High", "V-High"], width=8,
            #                      textvariable=self.entry26Str)
            self.entry27 = Spinbox(self.reactionTimeFrame, state="readonly", value=list(range(10, 60, 10)), width=8,
                                   textvariable=self.entry27Str)
            self.entry28 = Spinbox(self.responseFactorFrame, state="readonly", value=list(range(1, 17, 1)), width=8,
                                   textvariable=self.entry28Str)
            self.entry29 = Spinbox(self.recoveryTimeFrame, state="readonly", value=list(range(2, 17, 1)), width=8,
                                   textvariable=self.entry29Str)


            self.label01.grid(row=0, column=0, padx=5, pady=5, sticky=E)
            self.label02.grid(row=0, column=0, padx=5, pady=5, sticky=E)
            #self.label03.grid(row=0, column=0, padx=5, pady=5, sticky=E)
            self.label04.grid(row=0, column=0, padx=5, pady=5, sticky=E)
            self.label05.grid(row=0, column=0, padx=5, pady=5, sticky=E)
            #self.label06.grid(row=0, column=0, padx=5, pady=5, sticky=E)
            self.label07.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label08.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label09.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            #self.label10.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            #self.label11.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label12.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label13.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label14.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label15.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label16.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label17.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label18.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label19.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label20.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label21.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label22.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label23.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label24.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            #self.label25.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            #self.label26.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label27.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label28.grid(row=0, column=0, padx=5, pady=5, sticky=W)
            self.label29.grid(row=0, column=0, padx=5, pady=5, sticky=W)

            self.entry01.grid(row=0, column=1, sticky=E)
            self.entry02.grid(row=0, column=1, sticky=E)
            #self.entry03.grid(row=0, column=1, sticky=E)
            self.entry04.grid(row=0, column=1, sticky=E)
            self.entry05.grid(row=0, column=1, sticky=E)
            #self.entry06.grid(row=0, column=1, sticky=E)
            self.entry07.grid(row=0, column=1, sticky=E)
            self.entry08.grid(row=0, column=1, sticky=E)
            self.entry09.grid(row=0, column=1, sticky=E)
            #self.entry10.grid(row=0, column=1, sticky=E)
            #self.entry11.grid(row=0, column=1, sticky=E)
            self.entry12.grid(row=0, column=1, sticky=E)
            self.entry13.grid(row=0, column=1, sticky=E)
            self.entry14.grid(row=0, column=1, sticky=E)
            self.entry15.grid(row=0, column=1, sticky=E)
            self.entry16.grid(row=0, column=1, sticky=E)
            self.entry17.grid(row=0, column=1, sticky=E)
            self.entry18.grid(row=0, column=1, sticky=E)
            self.entry19.grid(row=0, column=1, sticky=E)
            self.entry20.grid(row=0, column=1, sticky=E)
            self.entry21.grid(row=0, column=1, sticky=E)
            self.entry22.grid(row=0, column=1, sticky=E)
            self.entry23.grid(row=0, column=1, sticky=E)
            self.entry24.grid(row=0, column=1, sticky=E)
            #self.entry25.grid(row=0, column=1, sticky=E)
            #self.entry26.grid(row=0, column=1, sticky=E)
            self.entry27.grid(row=0, column=1, sticky=E)
            self.entry28.grid(row=0, column=1, sticky=E)
            self.entry29.grid(row=0, column=1, sticky=E)


            self.pacingModeFrame.grid(row=0, column=0, sticky=N)
            self.lowerRateLimitFrame.grid(row=1, column=0)
            self.upperRateLimitFrame.grid(row=2, column=0)
            #self.maximumSensorRateFrame.grid(row=3, column=0)
            self.fixedAVDelayFrame.grid(row=3, column=0)
            self.dynamicAVDelayFrame.grid(row=4, column=0)
            #self.minimumDynamicAVDelayFrame.grid(row=6, column=0)
            self.sensedAVDelayOffsetFame.grid(row=5, column=0)
            self.atrialAmplitudeFrame.grid(row=6, column=0)
            self.ventricularAmplitudeFrame.grid(row=7, column=0)
            #self.atrialAmplitudeUnregulatedFrame.grid(row=0, column=1)
            #self.ventricularAmplitudeUnregulatedFrame.grid(row=1, column=1)
            self.atrialPulseWidthFrame.grid(row=0, column=1)
            self.ventricularPulseWidthFrame.grid(row=1, column=1)
            self.atrialSensitivityFrame.grid(row=2, column=1)
            self.ventricularSensitivityFrame.grid(row=3, column=1)
            self.VRPFrame.grid(row=4, column=1)
            self.ARPFrame.grid(row=5, column=1)
            self.PVARPFrame.grid(row=6, column=1)
            self.PVARPExtensionFrame.grid(row=7, column=1)
            self.hysteresisFrame.grid(row=0, column=2)
            self.rateSmoothingFrame.grid(row=1, column=2)
            self.ATRDurationFrame.grid(row=2, column=2)
            self.ATRFallbackModeFrame.grid(row=3, column=2)
            self.ATRFallbackTimeFrame.grid(row=4, column=2)
            #self.ventricularBlankingFrame.grid(row=5, column=2)
            #self.activityThresholdFrame.grid(row=6, column=2)
            self.reactionTimeFrame.grid(row=5, column=2)
            self.responseFactorFrame.grid(row=6, column=2)
            self.recoveryTimeFrame.grid(row=7, column=2)


            self.resetButton = ttk.Button(self.paceSettingFrame, text="Reset",
                                          command=lambda: self.resetUserData(self.currentUsername))
            self.resetButton.grid(row=10, column=0, padx=5, sticky=W + E)
            self.confirmButton = ttk.Button(self.paceSettingFrame, text="Save",
                                            command=lambda: self.writeUserData(self.currentUsername))
            self.confirmButton.grid(row=10, column=1, padx=5, sticky=W + E)
            self.uploadButton = ttk.Button(self.paceSettingFrame, text="Upload")
            self.uploadButton.grid(row=10, column=2, padx=5, sticky=W + E)

            self.profileButton = ttk.Button(self.paceSettingFrame, text="Logout", command=lambda: self.logoutUser())
            self.profileButton.grid(row=11, column=2, padx=5, sticky=E)

            self.readUserData(self.currentUsername)


            self.displayScreen("programScreen")
            print("program screen created successfully")
            return True

    pulseplot = False

    def change_state(self):
        if appDCM.pulseplot == True:
            appDCM.pulseplot = False
        else:
            appDCM.pulseplot = True

    # style.use("ggplot")
    xar = [0, 0.1]
    yar = [0, 0]

    def createEgram1(self):
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(211)
        self.ax.grid()
        self.line, = self.ax.plot(appDCM.xar, appDCM.yar)
        self.ax.set_ylim(-1, 1)
        self.graph = FigureCanvasTkAgg(self.fig, master=self.egramFrame)
        self.graph.get_tk_widget().pack(side=BOTTOM, fill=X)

        self.stopstartButton1 = ttk.Button(self.egramFrame, text="Start/Stop", command=lambda: self.gui_handler())
        self.stopstartButton1.pack(side=TOP)
        self.graph.draw()

    def createEgram2(self):
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(211)
        self.ax.grid()
        self.line, = self.ax.plot(appDCM.xar, appDCM.yar)
        self.ax.set_ylim(-1, 1)
        self.graph = FigureCanvasTkAgg(self.fig, master=self.egramFrame)
        self.graph.get_tk_widget().pack(side=BOTTOM, fill=X)

        self.stopstartButton2 = ttk.Button(self.egramFrame, text="Start/Stop", command=lambda: self.gui_handler())
        self.stopstartButton2.pack()
        self.graph.draw()

    def refresh(self):
        if appDCM.pulseplot == True:
            appDCM.xar = np.append(appDCM.xar, appDCM.xar[-1] + 0.1)
            appDCM.yar = np.append(appDCM.yar, np.sin(appDCM.xar[-1]))
            self.ax.set_xlim(appDCM.xar[-1] - 10, appDCM.xar[-1])
            self.line.set_data(appDCM.xar, appDCM.yar)
            self.graph.draw()
            self.root.after(10, self.refresh)

    def gui_handler(self):
        self.change_state()
        self.refresh()


    def displaySetting(self):
        print("\ndisplay value ==============================")
        print(self.label01.cget("text"), self.entry01Str.get())
        print(self.label02.cget("text"), self.entry02Str.get())
        #print(self.label03.cget("text"), self.entry03Str.get())
        print(self.label04.cget("text"), self.entry04Str.get())
        print(self.label05.cget("text"), self.entry05Str.get())
        #print(self.label06.cget("text"), self.entry06Str.get())
        print(self.label07.cget("text"), self.entry07Str.get())
        print(self.label08.cget("text"), self.entry08Str.get())
        print(self.label09.cget("text"), self.entry09Str.get())
        #print(self.label10.cget("text"), self.entry10Str.get())
        #print(self.label11.cget("text"), self.entry11Str.get())
        print(self.label12.cget("text"), self.entry12Str.get())
        print(self.label13.cget("text"), self.entry13Str.get())
        print(self.label14.cget("text"), self.entry14Str.get())
        print(self.label15.cget("text"), self.entry15Str.get())
        print(self.label16.cget("text"), self.entry16Str.get())
        print(self.label17.cget("text"), self.entry17Str.get())
        print(self.label18.cget("text"), self.entry18Str.get())
        print(self.label19.cget("text"), self.entry19Str.get())
        print(self.label20.cget("text"), self.entry20Str.get())
        print(self.label21.cget("text"), self.entry21Str.get())
        print(self.label22.cget("text"), self.entry22Str.get())
        print(self.label23.cget("text"), self.entry23Str.get())
        print(self.label24.cget("text"), self.entry24Str.get())
        #print(self.label25.cget("text"), self.entry25Str.get())
        #print(self.label26.cget("text"), self.entry26Str.get())
        print(self.label27.cget("text"), self.entry27Str.get())
        print(self.label28.cget("text"), self.entry28Str.get())
        print(self.label29.cget("text"), self.entry29Str.get())
        print("============================================\n")

    def readUserData(self, username):
        self.userDataFile = "/" + username + ".json"
        self.jsonUserData = {}
        try:
            with open(self.userDirectory + self.userDataFile, "r") as fileIn:
                self.jsonUserData = json.load(fileIn)  # read user data

                self.programModeCombobox.set(self.jsonUserData["paceMode"])
                self.entry01Str.set(self.jsonUserData["entry01"])
                self.entry02Str.set(self.jsonUserData["entry02"])
                #self.entry03Str.set(self.jsonUserData["entry03"])
                self.entry04Str.set(self.jsonUserData["entry04"])
                self.entry05Str.set(self.jsonUserData["entry05"])
                #self.entry06Str.set(self.jsonUserData["entry06"])
                self.entry07Str.set(self.jsonUserData["entry07"])
                self.entry08Str.set(self.jsonUserData["entry08"])
                self.entry09Str.set(self.jsonUserData["entry09"])
                #self.entry10Str.set(self.jsonUserData["entry10"])
                #self.entry11Str.set(self.jsonUserData["entry11"])
                self.entry12Str.set(self.jsonUserData["entry12"])
                self.entry13Str.set(self.jsonUserData["entry13"])
                self.entry14Str.set(self.jsonUserData["entry14"])
                self.entry15Str.set(self.jsonUserData["entry15"])
                self.entry16Str.set(self.jsonUserData["entry16"])
                self.entry17Str.set(self.jsonUserData["entry17"])
                self.entry18Str.set(self.jsonUserData["entry18"])
                self.entry19Str.set(self.jsonUserData["entry19"])
                self.entry20Str.set(self.jsonUserData["entry20"])
                self.entry21Str.set(self.jsonUserData["entry21"])
                self.entry22Str.set(self.jsonUserData["entry22"])
                self.entry23Str.set(self.jsonUserData["entry23"])
                self.entry24Str.set(self.jsonUserData["entry24"])
                #self.entry25Str.set(self.jsonUserData["entry25"])
                #self.entry26Str.set(self.jsonUserData["entry26"])
                self.entry27Str.set(self.jsonUserData["entry27"])
                self.entry28Str.set(self.jsonUserData["entry28"])
                self.entry29Str.set(self.jsonUserData["entry29"])

                print("read user data successfully")
        except:
            self.programModeCombobox.set("DDD")
            self.entry01Str.set("60")
            self.entry02Str.set("120")
            #self.entry03Str.set("120")
            self.entry04Str.set("150")
            self.entry05Str.set("OFF")
            #self.entry06Str.set("50")
            self.entry07Str.set("OFF")
            self.entry08Str.set("3.5")
            self.entry09Str.set("3.5")
            #self.entry10Str.set("3.75")
            #self.entry11Str.set("3.75")
            self.entry12Str.set("0.4")
            self.entry13Str.set("0.4")
            self.entry14Str.set("0.75")
            self.entry15Str.set("2.5")
            self.entry16Str.set("320")
            self.entry17Str.set("250")
            self.entry18Str.set("250")
            self.entry19Str.set("OFF")
            self.entry20Str.set("OFF")
            self.entry21Str.set("OFF")
            self.entry22Str.set("OFF")
            self.entry23Str.set("20")
            self.entry24Str.set("1")
            #self.entry25Str.set("40")
            #self.entry26Str.set("Med")
            self.entry27Str.set("30")
            self.entry28Str.set("8")
            self.entry29Str.set("5")
            print("user data is corrupted or does not yet exist")

    def writeUserData(self, username):
        self.displaySetting()
        self.jsonUserData = {}

        self.userDataFile = "/" + username + ".json"
        with open(self.userDirectory + self.userDataFile, "w") as fileOut:
            self.jsonUserData["paceMode"] = self.programModeCombobox.get()
            self.jsonUserData["entry01"] = self.entry01Str.get()
            self.jsonUserData["entry02"] = self.entry02Str.get()
            #self.jsonUserData["entry03"] = self.entry03Str.get()
            self.jsonUserData["entry04"] = self.entry04Str.get()
            self.jsonUserData["entry05"] = self.entry05Str.get()
            #self.jsonUserData["entry06"] = self.entry06Str.get()
            self.jsonUserData["entry07"] = self.entry07Str.get()
            self.jsonUserData["entry08"] = self.entry08Str.get()
            self.jsonUserData["entry09"] = self.entry09Str.get()
            #self.jsonUserData["entry10"] = self.entry10Str.get()
            #self.jsonUserData["entry11"] = self.entry11Str.get()
            self.jsonUserData["entry12"] = self.entry12Str.get()
            self.jsonUserData["entry13"] = self.entry13Str.get()
            self.jsonUserData["entry14"] = self.entry14Str.get()
            self.jsonUserData["entry15"] = self.entry15Str.get()
            self.jsonUserData["entry16"] = self.entry16Str.get()
            self.jsonUserData["entry17"] = self.entry17Str.get()
            self.jsonUserData["entry18"] = self.entry18Str.get()
            self.jsonUserData["entry19"] = self.entry19Str.get()
            self.jsonUserData["entry20"] = self.entry20Str.get()
            self.jsonUserData["entry21"] = self.entry21Str.get()
            self.jsonUserData["entry22"] = self.entry22Str.get()
            self.jsonUserData["entry23"] = self.entry23Str.get()
            self.jsonUserData["entry24"] = self.entry24Str.get()
            #self.jsonUserData["entry25"] = self.entry25Str.get()
            #self.jsonUserData["entry26"] = self.entry26Str.get()
            self.jsonUserData["entry27"] = self.entry27Str.get()
            self.jsonUserData["entry28"] = self.entry28Str.get()
            self.jsonUserData["entry29"] = self.entry29Str.get()
            json.dump(self.jsonUserData, fileOut)  # write to .json file
            print("write user data successfully")

    def resetUserData(self, username):
        self.programModeCombobox.set("DDD")
        self.entry01Str.set("60")
        self.entry02Str.set("120")
        #self.entry03Str.set("120")
        self.entry04Str.set("150")
        self.entry05Str.set("OFF")
        #self.entry06Str.set("50")
        self.entry07Str.set("OFF")
        self.entry08Str.set("3.5")
        self.entry09Str.set("3.5")
        #self.entry10Str.set("3.75")
        #self.entry11Str.set("3.75")
        self.entry12Str.set("0.4")
        self.entry13Str.set("0.4")
        self.entry14Str.set("0.75")
        self.entry15Str.set("2.5")
        self.entry16Str.set("320")
        self.entry17Str.set("250")
        self.entry18Str.set("250")
        self.entry19Str.set("OFF")
        self.entry20Str.set("OFF")
        self.entry21Str.set("OFF")
        self.entry22Str.set("OFF")
        self.entry23Str.set("20")
        self.entry24Str.set("1")
        #self.entry25Str.set("40")
        #self.entry26Str.set("Med")
        self.entry27Str.set("30")
        self.entry28Str.set("8")
        self.entry29Str.set("5")
        self.writeUserData(username)


    def logoutUser(self):
        self.root.config(menu="")
        self.createLoginScreen()
        self.createHeaderScreen()


login = appDCM()
