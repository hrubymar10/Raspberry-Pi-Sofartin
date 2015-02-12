#!/bin/bash
echo "Automated Installer Program For I2C LCD Screens"
echo "Installer by Ryanteck LTD."
echo "Updating APT & Installing python-smbus, if password is asked by sudo please enter it"
#sudo apt-get update

sudo apt-get install python-smbus -y
echo "Should now be installed, now checking revision"
revision=`python -c "import RPi.GPIO as GPIO; print GPIO.RPI_REVISION"`

if [ $revision = "1" ]
then
echo "I2C Pins detected as 0"
cp installConfigs/i2c_lib_0.py ./i2c_lib.py
else
echo "I2C Pins detected as 1"
cp installConfigs/i2c_lib_1.py ./i2c_lib.py
fi
echo "I2C Library setup for this revision of Raspberry Pi, if you change revision a modification will be required to i2c_lib.py"
echo "Now overwriting modules & blacklist. This will enable i2c Pins"
sudo cp installConfigs/modules /etc/
sudo cp installConfigs/raspi-blacklist.conf /etc/modprobe.d/
echo "Should be now all finished. Please press any key to now reboot. After rebooting run"
echo "'sudo python lcd.py' from this directory"
read -n1 -s
sudo reboot
