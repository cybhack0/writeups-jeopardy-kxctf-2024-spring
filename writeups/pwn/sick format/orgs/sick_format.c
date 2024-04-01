#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void greeting() 
{
  char* hi = "hi, are you ready to lose or will you fight to the end?\n";
  printf(hi);
  fflush(stdout);
}

void lol(char *str)
{
  int shift = 3; 
    char tablo[256]; 
    for (int i = 0; i < 256; i++) {
        tablo[i] = (char)((i + 10) % 256);
    }

    for (int i = 0; str[i]; i++) {
        str[i] = str[i] + shift;
    }

    for (int i = 0; str[i]; i++) {
        str[i] = tablo[(int)str[i]];
    }
}
int changeme;

void havefun()
{
  char buff[512];

  fgets(buff, sizeof(buff), stdin);
  printf(buff);
  fflush(stdout);
 
  if(changeme == 69) {
      char* flag = getenv("FLAG");
      printf("Nice, you got this: %s\n", flag);
      fflush(stdout);
  } else {
      printf("No no no no, bruh... %d\n", changeme);
      fflush(stdout);
  }

  lol("chechik vispalsya, a ti?");
}

int main(int argc, char **argv)
{
  greeting();
  havefun();
}
