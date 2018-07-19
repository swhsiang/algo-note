#include<stdio.h>

// Implement selection sort

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sort(int *array, size_t len) {
    printf("%zu\n", len);
    int i, j, min = 0;
    for (i = 0; i < len - 1; i++ ) {
        min = i;
        for (j = i + 1; j < len; j++) {
            if (array[j] < array[min]) {
                min = j;
            }
        }
        swap(&array[min], &array[i]);
    }
}

void printArr(int array[], size_t len) {
    int i = 0;
    for (i = 0; i < len; i ++) {
        printf("%4d ", array[i]);
    }
    printf("\n");
}

int main(void) {
    int testArr[] = {2, 2, 61, 23, 231, 51, 56, 66, 66};

    printf("%lu\n", sizeof(testArr) / sizeof(int));
    printArr(testArr, sizeof(testArr) / sizeof(int));
    sort(testArr, sizeof(testArr) / sizeof(int));
    printArr(testArr, sizeof(testArr) / sizeof(int));
    return 0;
}
