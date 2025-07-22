#include <stdio.h>

int main() {
    int age = 25;
    int* ptr = &age;

    printf("Old address: %p\n", ptr);
    printf("Old value: %d\n", *ptr);

    *ptr = 31;

    printf("New address: %p\n", ptr);
    printf("New value: %d\n", *ptr);

    return 0;
}