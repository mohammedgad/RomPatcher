#TP-Link Rom-0 Patcher

TP-Link Rom-0 Patcher is a python script that keep changing your router's DNS to Google Public DNS every 15 minutes through a loop of three steps

1. Download Rom-0 file 
2. Extract router's password from Rom-0 file using rom-0 PasswordExtractor [View Source Code](https://github.com/rootkick/Rom-0-Decoder)
3. Make a POST request to change the Primary and Secondary DNS to Google Public DNS 8.8.8.8
4. GOTO Step 1

#Why to use TP-Link Rom-0 Patcher

TP-Link didn't release any updates or patch till now regards rom-0 vulnerability and all our tries to patch this vulnerability led to nothing which put a lot of people at risk and there are many attackers Exploit Rom-0 Vulnerability 
and updates our router's DNS to their Server IP using automated server so you need to check your DNS every 15 minutes to make sure that you are safe from their attacks
here comes **RomPatcher** role which change the DNS to Google Public DNS every 15 minutes so you don't need to keep track of your DNS

#How to use TP-Link Rom-0 Patcher

Make sure that you have python 2.7 

`python --version`


You can run RomPatcher script simply

`python rompatcher.py`


You can run RomPatcher script in background

`pythonw rompatcher.py`


You can change the default time interval the `15 minutes` by using `-i` argument

To make the script change your DNS every 30 seconds

`python rompatcher.py -i 30`


You can change the targeted **gateway IP** to your own IP in casse you want to run the script on your **remote server** by using `-g` argument

`python rompatcher.py -g <your-ip>`


You can Change the **DNS** to any DNS you want by using `-d` argument

`python rompatcher.py -d 8.8.4.4`

