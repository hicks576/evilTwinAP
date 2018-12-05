# Evil Twin AP Attack
Usage: python attack.py <AP-name> <AP-MAC-address> <AP-channel-#> [-mac | -ip] <target-MAC/IP>

## Example
python attack.py osuwireless 94:B4:0F:AD:ED:00 1 -ip <IP-address>

## Description
Our project is a Evil Twin AP attack. We force a specific user (or everyone on a WiFi network) off of their current WiFi network and make them reconnect to our fake WiFi network with the same name. We ran into the following issues:


(1) Issues getting user to automatically connect to our fake WiFi network


(2) Issues routing target's traffic through DHCP server to give them internet access with our fake WiFi network


(3) Issues routing user to fake Carmen webpage


We tried to use MITMf to create a DHCP server that would direct the user to the fake Carmen webpage so that we could steal their password. Setting up the virtual environment for MITMf proved to be a challenge and we were not able to get it working. However, if this tool worked, it would allow us to direct the user to a fake Carmen webpage in order to steal their information.



Individual Contributions


Adam - Created the fake Carmen webpage, bought the wireless adapters, troubleshooted adapters frequently, aided in the script design and video making process, troubleshooted DHCP issues


Scott - Created the start up scripts, aided in video making process, troubleshooted DHCP issues


## YouTube Links
https://www.youtube.com/watch?v=iMn8QYv1_Hk

https://www.youtube.com/watch?v=jM_BtMD4M4k

https://www.youtube.com/watch?v=YI_Awuynnlc

