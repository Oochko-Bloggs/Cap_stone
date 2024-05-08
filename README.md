## CAPSTONE project 1
***
## This project was created for educational purpose only\!\!\!
***

### Leveraging python for cyber security
This project purpose is \: 
* Develop an understanding of cybersecurity concepts
* Enhance our python skillsssss
* Gain practical experience

### Script and Tools
- [ ] SSH login brute force
- [ ] ftp login brute force
- [ ] Subdomain enumerator 
- [ ] Port Scanner
- [ ] Password hash craker
- [ ] File encryptor
- [x] ARM MITM attack script
- [x] DOS script 
- [x] Syn flood attack script

### Preparations
### Linux \(Debian\/Ubuntu\)\:
1. First\, ensure you have Python installed\. If not install it\:
```warp-runnable-command
sudo apt-get update
sudo apt-get install python3
```
2. Next install the python development headers\:
```warp-runnable-command
sudo apt-get install python3-dev
```
### Linux\(Red Hat\/Fedora\)\:
1. Install Python and Development tools\:
```warp-runnable-command
sudo dnf install python3 python3-devel
```
### macOS\:
1. Ensure you have Xcode Command Line Tools installed\. If not\, open Terminal and run\:
```warp-runnable-command
xcode-select --install
```
2. Install Python \(if needed\)\:
```warp-runnable-command
brew install python
```
***
### Activate a Virtual Enviroment \(Optional\)\:
```warp-runnable-command
python -m venv myenv
```
* Activate the virtual environment \:
On Windows \(PowerShell\)\:
```warp-runnable-command
.\myenv\Scripts\Activate
```
on macOS\/Linux \: 
```warp-runnable-command
source myenv/bin/activate
```
***
Before running scripts run this command \:
```warp-runnable-command
pip3 install -r requirement.txt

```
When executing code use root user privilege to avoid any permission error\!

### When running ARP MITM attack script 
you have to enable ip\_forward or use Dual\-Interface setup to one for the attack and another for internet access 

Enabling IP forwarding by modifying the \/etc\/sysctl\.conf file\.
```warp-runnable-command
net.ipv4.ip_forward = 1
```
Then reload the configuration using \: 
```warp-runnable-command
sudo sysctl -p
```
