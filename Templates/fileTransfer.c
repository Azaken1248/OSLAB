#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(){
	int fd1 = open("A.txt", O_RDONLY);
	int fd2 = open("B.txt", O_WRONLY);
	char buff;
	
	while(read(fd1, &buff, 1)){
		write(fd2, &buff, 1);
	}

	return 0;
}
