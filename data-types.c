#include<stdio.h>

/**
 * int  4 bytes - %d
 * float 4 bytes - %f
 * char 1 byte - %c
 * double 8 bytes - %lf - has 6 digits after decimal point.
 */

int main() {
    int age = 10;
    double height = 100.4;
    float epoch = 200.3;
    double epochDouble = 200.3;

    printf("Age: %d, Height: %.2lf\n", age, height);
    printf("Height: %f\n", height);
    printf("Float: %f\n", epoch);
    printf("Double: %lf\n", epochDouble);
}
