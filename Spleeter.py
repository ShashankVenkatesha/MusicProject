











from spleeter.separator import Separator

# Initialize a separator with the 4stems model - it splits the audio into vocals, drums, bass, and others
separator = Separator('spleeter:4stems')

# Provide the input audio file path and the output directory where the separated files will be saved
input_audio_file = 'your_audio_file.mp3'
output_directory = 'output_directory'

# Process the audio file
separator.separate_to_file(input_audio_file, output_directory)

# The separated audio files will be saved in the specified output directory with appropriate names like 'vocals.wav', 'drums.wav', etc.
