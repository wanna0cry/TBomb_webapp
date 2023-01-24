<h1 align="center">
  <br>
  <a href="https://github.com/wanna0cry"><img src="https://i.ibb.co/F4HBKqm/TBomb.png" alt="TBomb WebAPP"></a>

</h1>


<p align="center">A free and open-source SMS/Call bombing application</p>

## NOTES:


> **Due to the overuse of script, a bunch of APIs have been taken offline. It is okay if you do not receive all the messages.**


- The application requires active internet connection to contact the APIs
- You would not be charged for any SMS/calls dispatched as a consequence of this script
- For best performance, use single thread with considerable delay time
- Always ensure that you are using the latest version of TBomb and have Python 3
- This application must not be used to cause harm/discomfort/trouble to others
- By using this, you agree that you cannot hold the contributors responsible for any misuse

## Compatibility
Check your Python version by typing in
```shell script
$ python --version
```
If you get the following
```shell script
Python 3.8.3
```
or any version greater than or equal to 3.4, this script has been tested and confirmed to be supported. For obsolete versions of Python (eg 2.7), use discretion while executing the script as it has not been tested there.

## Features

- Over 15 integrated messaging and calling APIs included with JSON
- Unlimited (with abuse protection) and super-fast bombing with multithreading
- Possibility of international API support (APIs are offline)
- Flexible with addition of newer APIs with the help of JSON documents
- Modular codebase and snippets can be easily embedded in other program


## Usage:

### Install from GIT

#### NOTE 

Git installation methods are not universal and are likely to differ between distributions so installing Git as per the given instructions below may not work. Please check out how to install Git for your Linux distribution [here](https://git-scm.com/). Commands below provide instructions for Debian-based systems.

>Running `TBomb.sh` as sudo miscofigures files ownership. It is recommended not to run it as sudo

Run these commands to clone and run TBomb WebAPP.

Installation Steps
```shell script
git clone https://github.com/wanna0cry/TBomb_webapp.git
```
```shell script
cd TBomb_webapp
```
```shell script
pip3 install -r requirements.txt
```
```shell script
pip3 install streamlit
```
```shell script
streamlit run app.py
```
## Contributors

This is a WebApp version of [Tbomb Script](https://github.com/TheSpeedX/TBomb)
- [wanna0cry](https://github.com/wanna0cry)



### TODO:

- [x] Make Code More Readable and Extensible
- [ ] Add More Mail Spam APIs
- [ ] Add More SMS Spam APIs
- [ ] Add More Call Spam APIs
- [ ] Resolve threading issue in some devices

## FAQ

##
**Q:** Do you support "X" Country?

**A:** Most Countries are supported for SMS and only India for calls. The SMS delivery rate might be different for different countries.
##
**Q:** Can you add support for "X" Country?

**A:** We do what we can, but we cannot promise. Please stay tuned for future support. If you are ready to help then maybe we can do faster.
##
**Q:** Why is the limit so low?

**A:** Due the amount of requests, the APIs can die. To prevent a bigger outtake of TBomb, it has been limited. 

**Q:** Should I use VPN? 

**A:** No, If you are facing high fail rate as TBomb can fail due the high response time or API restrictions.
##
**Q:** How to get protection ?

**A:** Use OTP blockers and activate DND.
##
**Q:** Why does it fail?

**A:** Due to the overuse of script, a bunch of APIs have been taken offline. It is okay if you do not receive all the messages.
##
### Support

Contributions, issues, and feature requests are welcome!  
Give a ★ if you like this project!

<p align="right"> Last FAQ Update: 25.01.2023 </p>
