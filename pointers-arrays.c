#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++) {
        printf("%d = %p\n", numbers[i], &numbers[i]);
    }

    printf("Array Address of 1: %p\n", numbers);
    printf("Array Address of 2: %p\n", numbers + 1);
    printf("Array Address of 3: %p\n", numbers + 2);
    printf("Array Address of 4: %p\n", numbers + 3);
    printf("Array Address of 5: %p\n", numbers + 4);

    return 0;
}