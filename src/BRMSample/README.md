# RadioHead
RFID-Reader/module software for Oodi library

Open the terminal.

Install libusb libraries:

```  Code:
  sudo apt-get install libusb-1.0-0-dev
```

Install Qt:

```  Code:
sudo apt-get install build-essential

sudo apt-get install qtcreator

sudo apt-get install qt5-default
```

Use qmake command for the .pro file to generate a makefile:

```  Code:
  qmake BRMSample.pro
```

This should have generated a Makefile.
So the final step should simply be:
  
```Code:
  make
```
This will run gnu make and build our executable.

You can view the application by running:

```  Code:
  ./BRMSample
```
Which should be located ./release




