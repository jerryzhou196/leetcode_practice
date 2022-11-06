# NOTE: running make without a target will literally run the first one 


# [target file name]: [dependencies]
# 		[insert commmands here]

# when we run blah, we first check if blah.c has change relative to last time we ran make 

# if it has, then we run the "blah" target


# NOTE: blah will only run if either:
# 		"blah" doesnt exist 
# 		"blah.c" is newer than "blah" in terms of time last modified

blah: blah.o
	cc blah.o -o blah 

blah.o: blah.c
	cc -c blah.c -o blah.o
blah.c:
	echo "int main() { return 0; }" > blah.c

# if your commmad returns an error, we don't consider it run

hello:
	echo "im a failure :("

clean:
	rm -f blah.c
