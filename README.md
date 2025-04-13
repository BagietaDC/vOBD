
# vOBD

Python functional program for OBD interface



## 🔧 Requirements
• ELM327 OBD2 USB Interface  
• Python 3.8+ → https://www.python.org/downloads/

⚠️ During Python installation, check:
☑ Add Python to PATH  
☑ tcl/tk and IDLE
## 💾 Installation
1. Unzip the `.zip` file into a new folder (e.g. on Desktop).  
2. Open CMD as Administrator.  
3. Navigate to the folder:  
   cd [PASTE_PATH_HERE]

4. In CMD, enter the following:
   python -m pip install --upgrade pip  
   pip install obd pyserial

5. Launch the program:
   python obdmain-cmd.py    ← command-line mode (CMD)  
   python obdmain-gui.pyw    ← graphical interface (GUI)
## 🛠 Common issues
❌ ELM327 not connecting?  
• Check Device Manager (Ports COM)  
• Should show up as COM3, COM4, etc.

❌ "Python not found"  
• Make sure Python was added to PATH.  
• Try using `python3` instead of `python`.

❌ "[…] The parameter is incorrect."  
• Ensure ELM327 is plugged in correctly.  
• Make sure the car ignition is ON (not just accessories).
## 🧰 Feature explanation
🧾 TOP MENU:
• File:
  - Save log → saves all communication  
  - Exit → closes the app

• Tools:
  - Select parameters → list of monitored values  
  - Emulator mode → shows random data without ELM327

BUTTONS:
• Connect to interface → connects to ELM327  
• Read DTCs → shows active OBD error codes  
• Read Freeze Frames → data from the error moment  
• Clear DTCs → clears active codes (if possible)  
• Monitor parameters → live data from vehicle  
• Save log → saves full session in `Logs` folder  
• Exit → closes the program

CONSOLE:
• Shows command log, responses and errors

PARAMETER WINDOW:
• Displays live vehicle data (RPM, Speed, Temp, etc.)