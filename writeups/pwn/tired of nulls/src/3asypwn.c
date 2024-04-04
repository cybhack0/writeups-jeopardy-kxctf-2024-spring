#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void dont_call_me() {
    char *flag = getenv("FLAG");
    printf("Ohhh, close ur eyes... U shouldn't see this %s\n", flag);
    fflush(stdout);
}

int main (int argc, char **argv)
{
    char buffer[64];
    
    gets(buffer);
}
