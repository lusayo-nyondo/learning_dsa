#include <stdio.h>

int main() {
    // This is a regular variable.
    int age = 25;

    // The ampersand refers to its address in memory.
    printf("%p\n", &age);

    // ptr is a pointer.
    int* ptr = &age;

    printf("Address: %p\n", ptr);
    printf("Value: %d\n", *ptr);

    return 0;
}