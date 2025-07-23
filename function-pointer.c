#include <stdio.h>

void findValue(int* num) {
    *num = 49;
}

int main() {
    int num = 25;
    findValue(&num);
    printf("Value is: %d\n", num);

    return 0;
}
