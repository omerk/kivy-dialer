
all:
	python /home/kivy/android/python-for-android/dist/default/build.py --dir `pwd` 
	--name "Dialer" \
	--package org.foo.dialer \
	--version 0.1 \
	--icon `pwd`/icon.png \
	--orientation portrait \
	--permission VIBRATE \
	debug installd \
