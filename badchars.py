badchars = ""
for x in range(1, 256):
	badchars += ("\\x" + "{:02x}".format(x))

excludes = input("Enter badchars to exclude (csv format): ")

for exclude in excludes.split(","):
	badchars = badchars.replace(exclude, "")

print(badchars)
