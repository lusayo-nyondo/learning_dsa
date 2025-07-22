#include<stdio.h>

int main() {
    char str[20];

    printf("Enter your username: ");
    fgets(str, sizeof(str), stdin);
    printf("Your name is: %s\n", str);
    return 0;
}