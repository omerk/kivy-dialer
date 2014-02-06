build:
	buildozer android debug

install: push

push: build
	adb install -r  bin/*.apk

debug:
	adb logcat

clean:
	buildozer clean
	rm -r bin/*
