import os

LogFile = "daily_log.log"
DivToken = "\n#### WDNMD ####\n"

def reset_log_file(fileName = "daily_log.log"):
	if fileName == LogFile:
		return
	# TODO:
	os.system("mv {} {}".format(LogFile, fileName))
	LogFile = fileName

def append_daily(text):
	cur = load_logs()
	os.system("touch {}".format(LogFile))
	with open(LogFile, "a") as f:
		if len(cur) != 0:
			f.write('\n')
		f.write(text)
		f.close()

def load_logs():
	os.system("touch {}".format(LogFile))
	with open(LogFile, "r") as f:
		res = f.read()
		f.close()
		return res.split(DivToken)
	return []

def store_logs(logs):
	text = ""
	for i in range(len(logs)):
		if i != 0:
			text = text + DivToken
		text = text + str(logs[i])

	os.system("touch {}".format(LogFile))
	with open(LogFile, "w") as f:
		f.write(text)
		f.close()

###################

def interaction_through_vim(text = "", tmpFile = "temp"):
	os.system("touch {}".format(tmpFile))
	with open(tmpFile, "w") as f:
		f.write(text)
		f.close()
	os.system("vim {}".format(tmpFile))
	with open(tmpFile, "r") as f:
		res = f.read()
		f.close()
	os.system("rm {}".format(tmpFile))
	return res

def load_log_file():
	os.system("touch {}".format(LogFile))
	with open(LogFile, "r") as f:
		res = f.read()
		f.close()
		return res

def edit_log():
	text = load_log_file()
	res = interaction_through_vim(text)
	print(res)

logs = ["123", "456", "789\n123"]
store_logs(logs)
append_daily("wdnmd")
edit_log()
