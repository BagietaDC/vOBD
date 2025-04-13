───────────────────────────────────────────────
         ____  ____  _____  
        / __ \|  _ \|  __ \ 
 __   _| |  | | |_) | |  | |
 \ \ / / |  | |  _ <| |  | |
  \ V /| |__| | |_) | |__| |
   \_/  \____/|____/|_____/ 

───────────────────────────────────────────────
              >>>  vOBD WINDOWS  <<<

───────────────────────────────────────────────
🔧 WYMAGANIA:
───────────────────────────────────────────────
• Interfejs ELM327 OBD2 USB
• Python 3.8+ → https://www.python.org/downloads/

⚠️ Podczas instalacji Pythona zaznacz:
☑ Add Python to PATH
☑ tcl/tk and IDLE

───────────────────────────────────────────────
💾 INSTALACJA:
───────────────────────────────────────────────
1. Rozpakuj plik `.zip` do nowego folderu (np. na pulpit).
2. Uruchom CMD jako administrator.
3. Przejdź do folderu:
   cd [WKLEJ_TUTAJ_ŚCIEŻKĘ]

4. W CMD wpisz kolejno:
   python -m pip install --upgrade pip  
   pip install obd pyserial

5. Uruchom program:
   python obdmain-cmd.py    ← tryb tekstowy (CMD)
   python obdmain-gui.pyw    ← tryb graficzny (GUI)

───────────────────────────────────────────────
🛠 NAJCZĘSTSZE PROBLEMY:
───────────────────────────────────────────────
❌ Nie działa połączenie z ELM327?
• Sprawdź w Menedżerze Urządzeń (Porty COM)
• Powinien być wykryty jako COM3, COM4, itp.

❌ "Python not found"
• Upewnij się, że dodałeś Pythona do PATH.
• Spróbuj użyć `python3` zamiast `python`.

❌ "[…] Parametr jest niepoprawny."
• Sprawdź, czy ELM327 jest dobrze podłączony.
• Sprawdź zapłon w samochodzie – musi być włączony.

───────────────────────────────────────────────
🧰 WYJAŚNIENIE FUNKCJI:
───────────────────────────────────────────────

🧾 GÓRNE MENU:
• File:
  - Save log → zapisuje wszystkie komunikaty
  - Exit → zamyka aplikację

• Narzędzia:
  - Choose parameters → lista danych do monitorowania
  - Emulator mode → losowe dane bez fizycznego ELM327

🔘 PRZYCISKI:
• Connect with interface → nawiązuje połączenie z ELM327
• Read DTC → pokazuje błędy OBD (np. Check Engine)
• Read Freeze Frames → dane z momentu błędu
• Delete DTC → usuwa obecne błędy (jeśli możliwe)
• Monitor parameters → na żywo pokazuje dane z auta
• Save log → zapisuje całą sesję do pliku `.txt` w folderze `Logs`
• Exit → wyłącza program

🪟 KONSOLA:
• Pokazuje logi z połączenia, komendy, odpowiedzi, błędy

📊 OKNO PARAMETRÓW:
• Tabela z bieżącymi wartościami danych (RPM, Speed, Temp, itd.)




              >>>  ENGLISH VERSION  <<<

───────────────────────────────────────────────
🔧 REQUIREMENTS:
───────────────────────────────────────────────
• ELM327 OBD2 USB Interface  
• Python 3.8+ → https://www.python.org/downloads/

⚠️ During Python installation, check:
☑ Add Python to PATH  
☑ tcl/tk and IDLE

───────────────────────────────────────────────
💾 INSTALLATION:
───────────────────────────────────────────────
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

───────────────────────────────────────────────
🛠 COMMON ISSUES:
───────────────────────────────────────────────
❌ ELM327 not connecting?  
• Check Device Manager (Ports COM)  
• Should show up as COM3, COM4, etc.

❌ "Python not found"  
• Make sure Python was added to PATH.  
• Try using `python3` instead of `python`.

❌ "[…] The parameter is incorrect."  
• Ensure ELM327 is plugged in correctly.  
• Make sure the car ignition is ON (not just accessories).

───────────────────────────────────────────────
🧰 FEATURE EXPLANATION:
───────────────────────────────────────────────

🧾 TOP MENU:
• File:
  - Save log → saves all communication  
  - Exit → closes the app

• Tools:
  - Select parameters → list of monitored values  
  - Emulator mode → shows random data without ELM327

🔘 BUTTONS:
• Connect to interface → connects to ELM327  
• Read DTCs → shows active OBD error codes  
• Read Freeze Frames → data from the error moment  
• Clear DTCs → clears active codes (if possible)  
• Monitor parameters → live data from vehicle  
• Save log → saves full session in `Logs` folder  
• Exit → closes the program

🪟 CONSOLE:
• Shows command log, responses and errors

📊 PARAMETER WINDOW:
• Displays live vehicle data (RPM, Speed, Temp, etc.)
