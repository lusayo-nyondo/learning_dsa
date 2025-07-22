#include <stdio.h>
#include <string.h>

int main() {
    char text[] = "Hey, ";
    char text2[] = "How are you.";

    strcat(text, text2);

    printf("%s\n", text);
}