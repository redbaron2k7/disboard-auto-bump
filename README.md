# Disboard-Auto-Bump

This is a [Python](https://www.python.org)-based Discord selfbot using the `discord.py-self` library. The selfbot automatically bumps your Discord server every 2 hours, currently this only supports [Disboard](https://disboard.org)

### <strong> I take no responsibility for any actions taken against your account for using these selfbots, or how users use my open source code.</strong>

### <strong>Using this on a user account is prohibited by the [Discord TOS](https://discord.com/terms) and can lead to your account getting banned in very rare cases.</strong>

<p float="left">
  <img style="vertical-align: top;" src="https://discord.c99.nl/widget/theme-4/1121106153682784321.png"/>
  <img src="https://lanyard.cnrad.dev/api/1121106153682784321?theme=dark&bg=171515&borderRadius=5px&animated=true&idleMessage=16%20year%20old%20solo%20dev" al/> 
</p>

# Features

- [x] Discord Selfbot: Runs on a genuine Discord account, allowing you to use it without even needing to invite a bot.
- [x] Fully Automatic: Just configure it, run it, and sit back and enjoy your server being boosted for you!

## Commands

- $add (Channel ID) - Adds a channel ID to the list of monitored channels
- $join (Invite Link) - Joins a server from invite link. !PROBABLY WONT WORK DUE TO CAPTCHAS!

# Steps to install and run:

### Step 1: Git clone repository

```
git clone https://github.com/redbaron2k7/Disboard-Auto-Bump
```

### Step 2: Changing directory to cloned directory

```
cd Disboard-Auto-Bump
```

### Step 3: Getting your Discord token

- Go to [Discord](https://canary.discord.com) and login to the account you want the token of
- Press `Ctrl + Shift + I` (If you are on Windows) or `Cmd + Opt + I` (If you are on a Mac).
- Go to the `Network` tab
- Type a message in any chat, or change server
- Find one of the following headers: `"messages?limit=50"`, `"science"` or `"preview"` under `"Name"` and click on it
- Scroll down until you find `"Authorization"` under `"Request Headers"`
- Copy the value which is your token

### Step 4: Rename `example.env` to `.env` and put the discord token and the bump channel IDs (you will get rate limited at over 5 channels). It'll look like this:

```
DISCORD_TOKEN=DISCORD_TOKEN_GOES_HERE
BOT_PREFIX=$
CHANNEL_IDS=channel1,channel2,channel3
```

### Step 5: Install all the dependencies and run the bot

Windows:

- Simply open `run.bat` if you're on Windows. This will install all pre-requisites and run the bot as well.

Linux:

- If you're on Linux, then run `cd the\bot\files\directory` to change directory to the bot files directory
- Run `pip install -r requirements.txt` to install all the dependencies
- Install discord.py-self using `pip install -U discord.py-self`
- Run the bot using `python3 main.py`