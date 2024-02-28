#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void flag() {
    char *flag = getenv("FLAG");
    printf("Winner winner chicken dinner:  %s\n", flag);
    fflush(stdout);
}

int main (int argc, char **argv)
{
    char buffer[64];
    
    gets(buffer);

}
