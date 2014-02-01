from kivy.app import App

def b():
	# this doesn't work when called from another function
	# scope issue probably?
	import pdb;pdb.set_trace()
		
class DialerApp(App):
	title = "Dialer"
	icon = "icon.png"

	def switchPane(self, pane):
		print "switchPane() " + pane
	
	def appendNum(self, num):
		self.root.ids.phoneNum.insert_text(num)		

	def delNum(self):
		self.root.ids.phoneNum.do_backspace()

	def callNum(self):
		print "callNum(): " + self.root.ids.phoneNum.text 



if __name__ == '__main__':
    DialerApp().run()

