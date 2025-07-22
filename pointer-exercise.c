#include <stdio.h>

int main() {
    double salary;
    printf("Enter a salary: ");
    scanf("%lf", &salary);
    printf("Salary scanned: %.2lf\n", salary);

    double* ptr = &salary;
    *ptr = (double)100.3;

    printf("Salary changed to: %.2lf\n", salary);
    return 0;
}