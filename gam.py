import zlib
from pathlib import Path

def crc32(fileName):
	with open(fileName, 'rb') as fh:
		hash = 0
		while True:
			s = fh.read(65536)
			if not s:
				break
			hash = zlib.crc32(s, hash)
		return "%08X" % (hash & 0xFFFFFFFF)

hashes = []

def main():
	folder = input("enter folder: ")

	pathlist = Path(folder+"/apks/").glob("*.apk")
	for path in pathlist:
		crc = crc32(str(path))
		hashes.append([str(path), crc])
	
	with open(folder+"\\hashes.txt", "w+") as f:
		for hasch in hashes:
			f.write("%s - %s\n" % (hasch[0], hasch[1]))

if __name__ == "__main__":
	main()