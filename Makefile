all: build install

build:
	buildozer android debug

install:
	adb install -r  bin/*.apk

debug:
	adb logcat

run:
	python main.py

clean:
	buildozer clean
	rm -r bin/*
