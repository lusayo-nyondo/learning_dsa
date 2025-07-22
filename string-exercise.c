#include <stdio.h>
#include <string.h>

int main() {
    char first[20];
    char second[20];

    printf("Enter first string: ");
    fgets(first, sizeof(first), stdin);

    printf("Enter second string: ");
    fgets(second, sizeof(second), stdin);

    int result = strcmp(first, second);

    printf("Result is: %d\n", result);
    return 0;
}