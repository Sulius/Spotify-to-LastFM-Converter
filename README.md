# Spotify-to-LastFM-Converter
Let's you import your Spotify history .json-file into Universal Scrobbler to add it to your last.fm-profile

As a new Last.fm user it bothered me that I couldn't simply import my Spotify history. Here is how you can do it:

1. Request your personal Spotify data in the data rights and privacy settings. I don't know if this is available worldwide (at least it is in Germany)

2. Once received, put the .json-files in the same directory as this program.

3. In the python code select your input file and make sure that output.csv is there and empty.

4. Simply run the application. Now the output.csv file should contain the song title and artist. Only songs that were played at least 30 seconds are considered (changeable in the code).

5. Most of the time you will have several .json files. So rename the output file and create a new empty output.csv. Select the other .json file and repeat.

6. Now you can head over to https://universalscrobbler.com 

7. Choose "Scrobble manually in bulk". You'll need to connect your last.fm profile and buy a premium subscription for universal scrobbler (which costs $1 per Month). 1 Month should be sufficient.

8. Copy paste the songs from your .csv files into the bulk scrobbler. The daily limit is 2800 scrobbles. Now the songs should appear in last.fm. Of course, you don't have the time information (last.fm only supports scrobbles from the past 2 weeks anyways), but at least you have a part of your music history! :)

9. (optional): The imported songs aren't attributed to their respective albums. To solve this you can upgrade to a Last.fm pro subscription and follow the steps described here: https://github.com/RudeySH/lastfm-bulk-edit


