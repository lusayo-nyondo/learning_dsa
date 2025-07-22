#include <stdio.h>

int main() {
    int age = 12;

    int* ptr = &age;
    printf("Pointer Address 1: %p\n", ptr);
    printf("Pointer Value 1: %d\n", *ptr);

    int *ptr2 = &age;
    printf("Pointer Address 2: %p\n", ptr2);
    printf("Pointer Value 2: %d\n", *ptr2);

    return 0;
}