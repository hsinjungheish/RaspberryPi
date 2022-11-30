"""
copyright WMMKSLab Gbanyan

modified by wwolfyTC 2019/1/24
"""
import time
import threading
import socket
import struct
import re
import os
import sys
from subprocess import call
from enum import Enum, unique
from traceback import print_exc


from aiy.board import Board
from aiy.voice.audio import AudioFormat, play_wav, record_file, Recorder

Lab = AudioFormat(sample_rate_hz=16000, num_channels=1, bytes_per_sample=2)


def record():
	with Board() as board:
		print('請按下按鈕開始錄音.')
		board.button.wait_for_press()
		done = threading.Event()
		board.button.when_pressed = done.set
		
		def wait():
			start = time.monotonic()
			while not done.is_set():
				duration = time.monotonic() - start
				print('錄音中: %.02f 秒 [按下按鈕停止錄音]' % duration)
				time.sleep(0.5)
		
		record_file(Lab, filename='recording.wav', wait=wait, filetype='wav')


def main():
	while True:
		record()
		print("播放音檔...")
		play_wav("recording.wav")


if __name__ == '__main__':
	main()
