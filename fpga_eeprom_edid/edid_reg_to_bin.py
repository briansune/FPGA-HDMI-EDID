
out_f = open("edid_bin.bin", "w+b")

cc = 0
dd = 0

with open("ssssss.txt", "r") as f:
	while True:
		c = f.read(1)
		
		if c == ',':
			continue
		elif c >= '0' and c <= '9':
			cc = ord(c) - ord('0')
		elif c >= 'a' and c <= 'f':
			cc = ord(c) - ord('a') + 10
		elif not c:
			break
		
		d = f.read(1)
		
		if c == ',':
			continue
		elif d < 'a':
			dd = ord(d) - ord('0')
		elif d > '9':
			dd = ord(d) - ord('a') + 10
		elif not d:
			break
		
		out_f.write( (cc*16+dd).to_bytes(1, byteorder='big') )


f.close()
out_f.close()
