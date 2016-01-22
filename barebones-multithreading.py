#!/usr/bin/python3

##--Michael duPont
##--michael@mdupont.com
##--Demoed at OPUG 2016-01-21
##--Barebones example of implementing multithreading

##--The code will create three threads which will each print digits
##--0 through 4 and the thread's name. Each thread will sleep for
##--different intervals between printing. The threads are managed by
##--a controller which allows the main process to create and keep
##--tabs on the threads. Once all three threads exit, so does main.

import threading
from time import sleep

class MyThread(threading.Thread):
	'''Our thread class extends the threading.Thread class'''
	
	def __init__(self, inter):
		'''Initialize the thread object with the sleep interval'''
		#We must init the parent class. Both methods below will do this
		#super().__init__(self)
		threading.Thread.__init__(self)
		self.sleepInt = inter
	
	def run(self):
		'''The thread's "main" function. This will be run once thread.start() is used'''
		#Print 0-4 with the name and sleep for the thread's given interval
		for i in range(5):
			print('{}: {}'.format(self.name, i))
			sleep(self.sleepInt)

class ThreadController():
	'''This class controls and corrals our thread class'''
	#Each thread can be accessed by its list index
	threads = []
	
	def addThread(self, inter):
		'''Add and start a new thread'''
		newThread = MyThread(inter)
		newThread.start()
		self.threads.append(newThread)
		print('Thread Added')
	
	def cleanThreads(self):
		'''Remove any threads that have finished running'''
		#Because we pop finished threads, we must iterate from the last list element
		for i in reversed(range(len(self.threads))):
			#We access each thread by index. .is_alive() tells us if thread finished
			if not self.threads[i].is_alive():
				self.threads.pop(i)
				print('Thread Cleaned')

#This line tells the interpreter to only run this code if file is main
#   python3 myclass.py -> code will run
#   import myclass     -> code won't run
if __name__ == '__main__':
	#Create our thread controller class
	TC = ThreadController()
	#Add three threads where sleep interval will be 1, 2, and 3
	print('Adding Threads')
	for i in range(1,4):
		TC.addThread(i)
	#While there are still active threads, remove any finished threads
	while TC.threads:
		TC.cleanThreads()
		sleep(.2)
	print('No More Threads')
