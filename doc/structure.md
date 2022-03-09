[toc]

# Background Info

## Requirement

1. The heart rate must not be too fast 
2. The heart rate must not be too slow 
3. The ventricles must contract at a particular interval after the atria contract 





# Pacemaker System

## System Components: Device

- Detects and provides therapy for bradycardia conditions 

- Provides programmable, single- and dual-chamber, rate-adaptive pacing, both permanent and temporary 
- May measure physical activity resulting in a sensor indicated rate for pacing the heart
- Provides sensor output data and rate histograms 
- Provides diagnostic features including 
  - Real-time telemetry markers 
  - EGMs 
  - P and R wave measurements 
  - Lead impedance 
  - Battery status tests 



## System Components: Device Controller-Monitor 

- Primary implant, pre-discharge  electrophysiology (EP) support, and follow-up device for the pacemaker system 
- Programs and interrogates the device 
- Commands delivery of a “Pace Now” pace 
- Acquires and shows diagnostics and lead signal measurement information, sensor history and trending information, and multi-channel monitoring
- Monitors battery status 



## System Components: Lead System 

- Implanted in the patient 
- Allows the device to sense intrinsic activity of the heart’s electrical signals 
- Delivers pacing therapy to the patient’s heart 
- Leads are connected to the pulse generator via its header



# Pacemaker Operating States

## Permanent state (main)

> Normal state of operation



## Temporary Pacing

> Used to test system parameters or provide patient diagnostic testing



## Magnet State

> Battery status



# Parameters



<img src="para.png" style="zoom:150%;" />





## Parameter List

Lower Rate Limit

Upper Rate Limit

Fixed AV Delay

Dynamic AV Delay

Sensed AV Delay Offset

Atrial Amplitude

Ventricualr Amplitude

Atrial Pulse Width

Ventricular Pulse Width

Atrial Sensitivity

Ventricular Sensitivity

VRP

ARP

Hysteresis

---------(Below will be review and confirm the following, tentatively)

-PVARP

-PVARP Extension

-Rate Smoothing

-ATR Duration

-ATR Fallback Mode

-ATR Fallback Time