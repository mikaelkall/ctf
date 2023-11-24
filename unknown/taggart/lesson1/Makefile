all:
	gcc vuln.c -o vuln_1 -fno-stack-protector -fcf-protection=none -no-pie -z execstack -Wl,-z,norelro
