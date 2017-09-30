#include<stdio.h>

void SWAP(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int array[], int head, int end) {
    int i = head - 1;
    for (int j = head; j < end; j ++ ) {
        if (array[j] <= array[end]) {
            i++;
            SWAP(&array[j], &array[i]);
        }
    }
    SWAP(&array[i + 1], &array[end]);
    return i + 1;
}


void quickSort(int array[], int head, int end) {
    if (head < end) {
        int p = partition(array, head, end);
        quickSort(array, head, p - 1);
        quickSort(array, p + 1, end);
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
    int testArr[] = {1,24, 5, 5, 63, 62, 100};
    printArr(testArr, sizeof(testArr) / sizeof(int));
    quickSort(testArr, 0, sizeof(testArr) / sizeof(int) - 1);
    printArr(testArr, sizeof(testArr) / sizeof(int));
    return 0;
}
