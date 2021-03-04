# tvtracker
Track tv shows and alert when new episodes are released.

## Installation
First, install [PyPushBullet](https://github.com/Azelphur/pyPushBullet) with `pip install git+https://github.com/Azelphur/pyPushBullet.git`

## Usage
First, install requirements with `pip install -r requirements.txt`

Add your tv shows to `series.txt`. The program will ignore those that are concluded, canceled or on hiatus.

Then, get your Pushbullet access token [here](https://www.pushbullet.com/#settings/account) and add it in `sendalert.py`

Run `python tvtracker.py` to check for new episodes and receive an alert containing the number and title the day the episode airs.

Works best if run daily with cron, like this: 

`0 10 * * * python3.7 ~/tvtracker/tvtracker.py`
