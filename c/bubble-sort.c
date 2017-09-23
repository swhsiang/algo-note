#include<stdio.h>

// Implement bubble sort

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// NOTE: In c language, it is impossible to get the length of array
// after you pass the array into a function.
// For example,
// void sort(int array) {
//   int i, j;
//   size_t len = sizeof(array) / sizeof(int);
//   the value of len would not fit our expectation
// }
void sort(int array[], size_t len) {
    int i, j;
    printf("len : %zu", len);
    for (i = 0; i < len - 1; i ++ ) {
        for (j = 0; j < len - i - 1; j ++) {
            if (array[j] > array[j + 1]) {
                swap(&array[j], &array[j+1]);
            }
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
    // 7
    int testArr[] = {2, 61, 23, 231, 51, 56, 66};
    printArr(testArr, sizeof(testArr) / sizeof(int));
    printf("\n");
    sort(testArr, sizeof(testArr) / sizeof(int));
    printf("\n");
    printArr(testArr, sizeof(testArr) / sizeof(int));
    return 0;
}
