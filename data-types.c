#include<stdio.h>

/**
 * int  4 bytes - %d
 * float 4 bytes - %f
 * char 1 byte - %c
 * double 8 bytes - %lf
 */

int main() {
    int age = 10;
    double height = 100.4;
    printf("Age: %d, Height: %.2lf\n", age, height);
}
