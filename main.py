from kivy.app import App
from jnius import cast
from jnius import autoclass

def b():
	# this doesn't work when called from another function
	# scope issue probably?
	import pdb;pdb.set_trace()
		
class DialerApp(App):

	def on_pause(self):
		return True

	def appendNum(self, num):
		self.root.ids.phoneNum.insert_text(num)		

	def delNum(self):
		self.root.ids.phoneNum.do_backspace()

	def callNum(self):
		number =  self.root.ids.phoneNum.text

		print "callNum(): " + number 

		PythonActivity = autoclass('org.renpy.android.PythonActivity')
		Intent = autoclass('android.content.Intent')
		Uri = autoclass('android.net.Uri')

		intent = Intent(Intent.ACTION_CALL)
		intent.setData(Uri.parse("tel:" + number))
		currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
 		currentActivity.startActivity(intent)


if __name__ == '__main__':
    DialerApp().run()

