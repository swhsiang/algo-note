#include<stdio.h>

// Implement insertion sort

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
    int i, j, temp;
    for (i = 1; i < len; i ++) {
        temp = array[i];
        for (j = i - 1; j >= 0 && array[j] > temp; j --) {
                array[j+1] = array[j];
        }

        array[j + 1] = temp;
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
