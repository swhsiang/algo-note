#include<stdio.h>

// Implement selection sort

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sort(int *array, size_t len) {
    int i, j, min;
    for (i = 0; i < len - 1; i ++ ) {
        min = i;
        for (j = i + 1; j < len; j ++) {
            if (array[min] > array[j]) {
                min = j;
            }
            swap(&array[min], &array[i]);
        }
    }
}

void printArr(int array[], size_t len) {
    int i = 0;
    for (i = 0; i < len; i ++) {
        printf("%d ", array[i]);
    }
}

int main(void) {
    int testArr[] = {2, 61, 23, 231, 51, 56, 66};

    printArr(testArr, sizeof(testArr) / sizeof(int));
    printf("\n");
    sort(testArr, sizeof(testArr) / sizeof(int));
    printf("\n");
    printArr(testArr, sizeof(testArr) / sizeof(int));
    return 0;
}
