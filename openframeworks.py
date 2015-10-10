import sublime, sublime_plugin
import subprocess
import os

print("plugin loaded")

class Compile(sublime_plugin.WindowCommand):
	def run(self):
		absolute = self.window.active_view().file_name()
		rootFolder = absolute.split('/src')
		makeCmd = "cd "+str(rootFolder[0])+" && make"
		proc = os.popen(makeCmd)
		print proc.read() 

class Runapp(sublime_plugin.WindowCommand):
	def run(self):
		absolute = self.window.active_view().file_name()
		rootFolder = absolute.split('/src')
		makeRunCmd = "cd "+str(rootFolder[0])+" && make run"
		proc = os.popen(makeRunCmd)
		print proc.read() 