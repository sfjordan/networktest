NetworkTest
----------------------
A short set of a couple of python scripts to test the basics of the currently connected network's quality.
It displays and color codes according to quality:
- packet loss
- average ping
- upload and download speeds

**REQUIRES THE SPEEDTEST CLIENT SCRIPT:**
you can get it [here](https://github.com/sivel/speedtest-cli).

Usage
=======
Run networktest as a shell script, `$ sh networktest`.
This script includes a `-v` option if you wish to view the results as they come back.

Alfred Workflow
=======
Also included is an Alfred workflow, which you can import to invoke the script more easily. To use it, you must have an alias set up: add the line `alias networktest='sh YOUR_PATH/networktest' to your .bash_profile or .bash_rc file.