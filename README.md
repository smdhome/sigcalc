# sigcalc
# Signum Price Calculator

## 1. PURPOSE OF THE SIGCALC PROGRAM:
The sigcalc program will graphically display the current prices for Signa, Bitcoin (BTC), Litecoin (LTC), and Etherium (ETH) in terms of US Dollars ($).  It will also display the price of Signa in terms of BTC, LTC, and ETH.  The current price data is queried from the Coingecko database.  

Note that, Coingecko limits the query frequency and may not respond if called too
rapidly.  In general this does not present a problem.  

## 2. USING THE SIGCALC PROGRAM:
Start the sigcalc program by double clicking on sigcalc.exe.  Alternatively, if Python 3 and the requisite Python packages, tk, requests, and coingecko, are installed, the Python script can be run by the command: python sigcalc.py.

The graphical user interface (GUI) will be displayed along with a black diagnostic window. Under normal circumstances, this black window can be ignored.  This black window may provide information if the Python program encounters a problem.

To display or refresh the price data, click the "Fetch Prices" button.  To exit the program click the X in the upper right of the display or click the "Exit" button on the lower right.

## 3. MAINTAINING THE SIGCALC PROGRAM:
The sigcalc program was coded for Python 3.11.1 on Windows 10 (64-bit) and the developer should install this version of Python (or later) to modify the program or to make enhancements.  Python 3.11.1 can be downloaded at: https://www.python.org/downloads/

Warning: Multiple version of Python may be installed and co-exist on Windows systems. To ensure the correct version of Python (3.11.1) is invoked, confirm that Path environment variable contains the correct path to python.exe (the Python interpreter) and to pip.exe (for Python package installation).

### Python 3.11.1 Windows installation is normally placed in:
C:\Users\<username>\AppData\Local\Programs\Python\Python311\
Where <username> is the users login name on the system.

### The pip.exe program is located here:
C:\Users\<username>\AppData\Local\Programs\Python\Python311\Scripts

### Edit the “Path” Environment variable (on Windows)
1. Click on the start menu and type “env”.
2. Click on “Edit environment Variables for your account”.
3. In the “User variables” pane (upper pane), select “the “Path” variable and click edit.
4. Confirm there are no entries for earlier versions of Python. Highlight and click Delete if so.
5. Click OK.
6. In the “System variables” pane (upper pane), select “the “Path” variable and click edit.
7. Click New to add two new directories to the system Path environment variable:
   - C:\Users\<username>\AppData\Local\Programs\Python\Python311\Scripts\
   - C:\Users\<username>\AppData\Local\Programs\Python\Python311\
Where <username> is the users login name on the system.
9. Confirm there are no other Python-related directories listed for Path and delete them if so.
10. Click OK to save changes.
11. Click OK again to exit the environment variables dialog.

### Check the Environment
1. Open a command window as follows:
  - Click on the start button and type “cmd”.
  - Right click on the Command Prompt App and select “Run as administrator”. 
You may need to specify a privileged account and password to successfully open a command prompt with admin rights.
2. Type “where python” at the command prompt.  Confirm that the specific version of Python is located at:
  - C:\Users\<username>\AppData\Local\Programs\Python\Python311
4. Type “where pip” at the command prompt. Confirm that the specific version of Python is located at:
  - C:\Users\<username>\AppData\Local\Programs\Python\Python311\Scripts\
5. Keep this privileged command prompt open for Python library installation steps below.

### Install supporting Python Extensions:
The following Python extensions are needed to maintain the sigcalc program:
1. tkinter – A GUI interface based on Tcl/Tk
2. requests - Allows programs to directly send HTTP/1.1 requests.
3. coingecko - API to access the Coingecko realtime cryptocurrency price database.
4. pyinstaller – Creates a stand-alone executable for distribution.

### Perform these installations as follows:
1. Type “pip install tk” and wait for the installation to complete.
2. Type “pip install requests” and wait for the installation to complete.
3. Type "pip install --upgrade coingecko"
4. Type “pip install pyinstaller” and wait for the installation to complete.

### Optionally Install Development Environment
The sigcalc program consists of a single source code file, sigcalc.py. This file may 
be maintained using any text editor.  However, Microsoft Visual Studio or PyCharm are 
also recommended development environments.

### These development environments may be found at:
  - https://visualstudio.microsoft.com/downloads/
  - https://www.jetbrains.com/pycharm/download/#section=windows

Refer to the applicable websites for installation and usage instructions for these tools.

### Building a Stand-alone Executable for sigcalc:
To create a single .exe file that can be distributed and run without the need to install 
a specific Python version or specific Python libraries, pyinstaller is used. Follow the 
steps below to generate an exe file from the sigcalc.py script:
1. Open a command window as follows:
  - Click on the start button and type “cmd”.
  - Right click on the Command Prompt App and select “Run as administrator”. You may need to specify a privileged account and password to successfully open a command prompt with admin rights.
2. Change the directory to the location of the sigcalc.py file using the “cd” command.
3. Type: “pyinstaller -F sigcalc.py” and wait for the processing to complete.
4. The new executable will be placed in the “dist” subdirectory below the current directory. E.g., “./dist/sigcalc.exe”.
Note that this executable file is very large (>11MB) and may be too large to send via email.

## 4. CHANGING THE BASE CURRENCY (OPTIONAL):
It should be possible to replace US Dollars with any supported currency.  Take note of 
all the instances of "USD" or "usd" in strings and when used in variable names.  Coingecko
supports the following currencies:
  "btc",
  "eth",
  "ltc",
  "bch",
  "bnb",
  "eos",
  "xrp",
  "xlm",
  "link",
  "dot",
  "yfi",
  "usd",
  "aed",
  "ars",
  "aud",
  "bdt",
  "bhd",
  "bmd",
  "brl",
  "cad",
  "chf",
  "clp",
  "cny",
  "czk",
  "dkk",
  "eur",
  "gbp",
  "gel",
  "hkd",
  "huf",
  "idr",
  "ils",
  "inr",
  "jpy",
  "krw",
  "kwd",
  "lkr",
  "mmk",
  "mxn",
  "myr",
  "ngn",
  "nok",
  "nzd",
  "php",
  "pkr",
  "pln",
  "rub",
  "sar",
  "sek",
  "sgd",
  "thb",
  "try",
  "twd",
  "uah",
  "vef",
  "vnd",
  "zar",
  "xdr",
  "xag",
  "xau",
  "bits", and
  "sats".
