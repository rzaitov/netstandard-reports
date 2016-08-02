#!/usr/bin/python

import subprocess

def prepare_commit_msg(file_path, content):
	with open(file_path, 'r+') as f:
		f.seek(0)
		f.write(content)
		f.truncate()

def get_framework_versions():
	bash_cmd = "ls -l /Library/Frameworks/Xamarin.{0}.framework/Versions/ | grep Current | sed -n 's/.*Current -> //p'"
	ios_version, error1 = subprocess.Popen(bash_cmd.format("iOS"), shell=True, stdout=subprocess.PIPE).communicate()
	mac_version, error2 = subprocess.Popen(bash_cmd.format("Mac"), shell=True, stdout=subprocess.PIPE).communicate()
	android_version, error2 = subprocess.Popen(bash_cmd.format("Android"), shell=True, stdout=subprocess.PIPE).communicate()

	ios_version = ios_version.strip().split("/")[-1]
	mac_version = mac_version.strip().split("/")[-1]
	android_version = android_version.strip().split("/")[-1]

	versions = "{ios_ver}\tXamarin.iOS.framework\n{mac_ver}\tXamarin.Mac.framework\n{android_version}\tXamarin.Android.framework".format(ios_ver=ios_version, mac_ver=mac_version, android_version=android_version)
	return versions

prepare_commit_msg("a-versions.txt", get_framework_versions())