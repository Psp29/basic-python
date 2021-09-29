# Playsound is an external module used to play music using python code.
from playsound import playsound
song = input('Please enter the song name: ')

print('playing song: ' + song + '...')

playsound(
    'E:\\STUDIES\\python\\chapter 1\\' + song + '.mp3')  # location of music file, here '\\' are used beacuse it is an windows OS. Also change the location.
# Enter the song name as 'megalovania'.
