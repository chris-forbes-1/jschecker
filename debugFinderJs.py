import sys, os, glob

	

for root, dirs, files in os.walk(sys.argv[1]):
	for file in files:
		if file.endswith(".js"):
			if "bootstrap" not in file:
				count = 0
				x = open(root+"/"+file, "r")
				for line in x:
					count += 1
					if "debugger" in line:
						print "debugger in "+ str(file) +" on line " + str(count)
						print "full line" + str(line)
					if "alert" in line:
						if "bootbox" not in line:
							if "//" not in line:
								print "alert in like "+ str(file) +" on line " + str(count)
								print "full line" + str(line)
				x.close()