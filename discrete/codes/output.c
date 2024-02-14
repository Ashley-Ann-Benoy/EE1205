#include <stdio.h>

int main() {
    FILE *file = fopen("sumval.dat", "w");  
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    
    for (int i = 0; i < 10; i++) {
        int x = i;
        float y =i+1 2.5*i*(i-1);
        fprintf(file, "%d %.2f\n", x, y);
    }

    fclose(file);  // Close the file


     FILE *file = fopen("sumap.dat", "w");  
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    
    for (int i = 0; i < 10; i++) {
        int x = i
        float y =i*(3.5+2.5*i);
        fprintf(file, "%d %.2f\n", x, y);
    }

    fclose(file);  // Close the file

    return 0;
}
