#include <errno.h>   // for errno
#include <limits.h>  // for INT_MAX
#include <stdlib.h>  // for strtol
#include<iostream>
#include<stdio.h>
using namespace std;

int main(int argc, char** argv )
{

int  a = atoi(argv[1]);
int  b = atoi(argv[2]);
printf("%d\n",a+b*b);
return 0;
}
