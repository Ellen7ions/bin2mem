#include <stdio.h>

#define MAXN_SIZE 1024
#define BYTE unsigned char

int main(int argc, char* argv[]) {
    char *fileName = argv[1];
    FILE* file = fopen(fileName, "rb");

    if (file == NULL) return -1;
    
    fseek(file, 0, SEEK_END);
    int len = ftell(file);
    fseek(file, 0, SEEK_SET);
    
    BYTE byteBuffer[MAXN_SIZE];
    fread(byteBuffer, sizeof(BYTE), MAXN_SIZE, file);
    int cnt = 0;
    for (int i = 0; i < len; i++) {
        printf("%02x", byteBuffer[i]);
        cnt += 1;
        if (cnt % 4 == 0) printf(",\n");
    }
    return 0;
}