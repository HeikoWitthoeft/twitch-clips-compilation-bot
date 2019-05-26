# twitch-clip-compilation-creator
Bot that can create compilation videos of:
    - Most popular clips of the day
    - Most popular clips of the week
    - Most popular clips of the month
    - Popular clips of a channel (Will create compilation when there are enough clips collected from a specific Twitch channel)

This bot is currently being used for this YouTube channel: 
- Fortnite: https://www.youtube.com/channel/UCxavrT2r-9tsliwOsmRVZ7w
- Global Twitch: https://www.youtube.com/channel/UCyID9pf6qVvSXQfupMPza2A

## Setup

- ```sudo apt-get update```
- ```apt install python3.6```
- ```apt install python3-pip```
- ```pip3 install -r requirements.txt```
- ```pip3 install --upgrade google-auth-oauthlib```
- ```apt-get install imagemagick```
- ```sudo add-apt-repository ppa:kirillshkrogalev/ffmpeg-next```
- ```sudo apt-get install ffmpeg```
- ```sudo apt install libmagick++-dev```
https://askubuntu.com/questions/873112/imagemagick-cannot-be-detected-by-moviepy

## Fonts
Install fonts in `/usr/local/share/fonts` and reboot.

### Secrets

- Create secrets directory in root.
- Create `secrets/youtube_client_credentials.json` with your Installed App credentials from the [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
- Create `secrets/twitch_secret.json` file with contents:
```
{
    "client_id": "YOUR_ID"
}
``` 

### Cron job example
Make sure the path matches the ROOT_LOCATION in the constants.py
```
# Fortnite Highlights Creator channel (fhc)
0 18 * * * python3 /root/twitch-clip-publisher/bot.py fhc day fortnite 6 1
0 1 * * 0 python3 /root/twitch-clip-publisher/bot.py fhc week fortnite 6 1
0 7 * * * python3 /root/twitch-clip-publisher/compilations.py fhc fortnite 6 1

# Global Twitch Highlights Creator channel (rlhc)
0 19 * * * python3 /root/twitch-clip-publisher/bot.py rlhc day twitch 6 1
0 2 * * 0 python3 /root/twitch-clip-publisher/bot.py rlhc week twitch 6 1
0 8 * * * python3 /root/twitch-clip-publisher/compilations.py rlhc twitch 6 1

# Apex Legends Highlights Creator channel (jchc)
0 17 * * * python3 /root/twitch-clip-publisher/bot.py jchc day apexlegends 6 0

# Super Smash Bros. Ultimate Highlights Creator channel (hhc)
0 16 * * * python3 /root/twitch-clip-publisher/bot.py hhc day supersmashbrosultimate 6 0
```

### Common issues
https://github.com/Zulko/moviepy/issues/401#issuecomment-278679961
https://github.com/Zulko/moviepy/issues/378#issuecomment-274163535

### Assets
#### YouTube Client
https://developers.google.com/api-client-library/python/samples/samples
