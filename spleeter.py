

# Install spleeter


#apt install ffmpeg

#pip install spleeter

from IPython.display import Audio

"""# Separate from command line"""



Audio('ganeshasuktham.mp3') #Enter Audio Path

spleeter separate -o output/ ganeshasuktham.mp3 #Output with path

#!ls output/ganeshasuktham

Audio('output/ganeshasuktham/vocals.wav') #Vocals 

Audio('output/ganeshasuktham/accompaniment.wav') #Accompaniment