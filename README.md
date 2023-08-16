
# FBAC

Facebook account creator with PureVPN 🛡️🔑

This tool was made for educational purposes ONLY!


It's not perfect... Feel free to open pull requests if you've made some improvements.
## Features

- Full randomised user data
- Account verification with Email OTP
- Check if the account is banned after creation.
- Choose the number of accounts to be created.
- option to add created accounts as friends to a specific account
- Export successful and need verification accounts to separate text files.
- Switching VPN IPs automatically using PureVPN
- Switching User-agent automatically using a list
- Cleaning browser data using Bleachbit

## To-do

- Add Proxy compatibility
- Add NordVPN compatibility 

## Installation

### Pre-Requests


  Ubuntu OS🐧

  Python🐍

  PureVPN Subsctiption🛡️

  Google chrome + Chromedriver🔰

  Bleachbit🧹

### Setting Up Pre-Requests
* Python Libraries
```bash
pip install -r requirements.txt

```

* PureVPN
```bash
curl https://purevpn-dialer-assets.s3.amazonaws.com/cross-platform/linux-cli/production/cli-install.sh | sudo bash
```
Sign into PureVPN
```bash
purevpn-cli -l
```
* Google chrome

download google chrome version 114:
```bash
wget mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.133-1_amd64.deb
```
Install google chrome:
```bash
sudo dpkg -i google-chrome-stable_114.0.5735.133-1_amd64.deb
```
```bash
sudo apt-get install -f
```
* Webdriver

set up google chrome webdriver:
```bash
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
```
```bash
unzip chromedriver_linux64.zip
```
```bash
sudo mv chromedriver /usr/bin/chromedriver
```
```bash
sudo chown root:root /usr/bin/chromedriver
```
```bash
sudo chmod +x /usr/bin/chromedriver
```
* Bleachbit

Set up Bleachbit
```bash
sudo apt install bleachbit -y
```
## Usage/Examples

```
python main.py
```


## Authors

- [@ReSo7200](https://www.github.com/ReSo7200)


## License

[MIT](https://choosealicense.com/licenses/mit/)

