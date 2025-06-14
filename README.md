# Bot-Set-Up for MAC

### Download Google Chrome
If chrome is not already installed on the computer, download [chrome](https://www.google.com/intl/en_us/chrome/) and open it 

### Installing python3
- This can be easily done using conda. First download [miniconda](https://docs.conda.io/en/latest/miniconda.html). Ensure that the version of miniconda is compatabile with the machine (i.e. x86/M1).

- Install Miniconda by opening terminal, going to Downloads and then installing the software on terminal (following the terminal instructions)

  ```
  cd ~/Downloads
  bash Miniconda3-latest-MacOSX-x86_64.sh 
  ```  
  *the second line is for non-m1 chip, for m1 chip use ```bash Miniconda3-latest-MacOSX-arm64.sh ```

- close and reopen terminal. If conda is sucessfully installed one should see ```(base)``` on each line of terminal. To check if python3 has been sucesfully installed, run ```python --version``` and ensure the version is python3.*

### Installing python dependencies
A few python packages are necessary. Run the following 2 lines in terminal to get relevant dependencies:

```
pip install selenium==4.22.0
pip install numpy
```

### Downloading chromedriver


The [chromedriver](https://googlechromelabs.github.io/chrome-for-testing/#stable) is used by selenium to control the bot. 

#### New Macs with M1 Chips
For Mac with new chips (M1-M3), use the following [link](https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.68/mac-arm64/chromedriver-mac-arm64.zip)

The when the file is downloaded, open the .zip file on finder to unzip the file, then open terminal and run the following command 


```
cd ~/Downloads
sudo mv chromedriver-mac-arm64/chromedriver /usr/local/bin
```

you will have to type the password on terminal (note characters won't show, but click enter when done anyways)

#### (Aternative) Old intel-based macs 
For older macs, use the following [link](https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.61/mac-x64/chromedriver-mac-x64.zip)

When the file is downloaded, open the .zip file on finder to unzip the file, then open terminal and run the following command

```
cd ~/Downloads
sudo mv chromedriver-mac-x64/chromedriver /usr/local/bin 
```

you will have to type the password on terminal (note characters won't show, but click enter when done anyways)

### Setting up Source code
first download the code base by cloning this repo

``` 
cd ~/Downloads
git clone https://github.com/adianliusie/usa_today_bot_2024
```

Then move the `run` file to be easily accessible from the home directory
``` 
mv usa_today_bot_2024/run ~
```

Then try running the script
```
cd ~
bash run
```

This won't work due to security preferences. Open System Preference > Security & Privacy > General, and then allow using the chromedriver.

Script should now work if on terminal you type ```bash run```!



