# APSystems alerting
## Purpose
Since the HTTP API is not working anymore for APSystems (http://api.apsystemsema.com:8073/apsema/v1/ecu/getPowerInfo), it's not easy to be alerted if your installation is not working anymore.

This project is a simple alerting system using a HTTP wrapper on APSystem dashboard and PushSafer software.

If your installation doesn't produce power, you receive an alert on mobile, desktop, etc.
## Setup
You need a Linux environment.

Create an account on PushSafer: https://www.pushsafer.com/

Clone the project.

Edit `export-vars.sh.template` and rename it by `export-vars.sh` and set your APSystems login and password and also put your PushSafer API Key.

## Run
Run the command `./check-aps.sh`

You will receive an PushSafer alert on your devices if the daily production is 0.
