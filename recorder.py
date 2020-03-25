import sounddevice as sd
import soundfile as sf
import time
import numpy

def sync_record(filename, duration, fs, channels, textfile):
	text = open(textfile)
	print('Van ban can doc: ')
	print(text.read())
	try:
		print('Start recording...')
		myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
		print('Press Ctr + C to stop.')
		sd.wait()
	except KeyboardInterrupt :
		print('\nDone! Record file is saved to: ' + repr(filename))
		sf.write(filename, myrecording, fs)
	# print('recording')
	# myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
	# sd.wait()
	# sf.write(filename, myrecording, fs)
	# print('done recording') 

# playback file
textfile = 'thoi_su.txt'
sync_record('thoi_su_1', 30, 16000, 1, textfile)


	# try:
	# 	print('Start recording...')
	# 	myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
	# 	sd.wait()
	# except KeyboardInterrupt :
	# 	print('\nDone! Record file is saved to: ' + repr(filename))
	# 	sf.write(filename, myrecording, fs)
