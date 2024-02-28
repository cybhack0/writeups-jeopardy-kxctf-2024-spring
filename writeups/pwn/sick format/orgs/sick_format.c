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

int changeme;

void havefun()
{
  char buff[512];

  fgets(buff, sizeof(buff), stdin);
  printf(buff);
  fflush(stdout);

  if(changeme == 228) {
      char* flag = getenv("FLAG");
      printf("Good... really good... %s\n",flag);
      fflush(stdout);
  } else {
      printf("No way... %d\n", changeme);
      fflush(stdout);
  }
}

int main(int argc, char **argv)
{
  greeting();
  havefun();
}
