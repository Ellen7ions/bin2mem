#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define FILE_MAX_SIZE   9830400
#define BUFFER_SIZE     2048
#define BYTE            unsigned char

BYTE bytes_buffer[BUFFER_SIZE];

int get_file_len(FILE *file) {
    if (file == NULL) return 0;
    fseek(file, 0, SEEK_END);
    int len = ftell(file);
    fseek(file, 0, SEEK_SET);
    return len;
}

void output_bin(FILE *file, BYTE buffer[], int count) {
    if (file == NULL) return;
    for (int i = 0; i < count; i++) {
        fprintf(file, "%02x", buffer[i]);
        if ((i + 1)% 4 == 0)
            fprintf(file, ",\n");
    }
}

int main(int argc, char *argv[]) {
    FILE *bin_file      = fopen(argv[1], "rb");
    FILE *target_file   = fopen(argv[2], "w");
    int bin_file_size       = get_file_len(bin_file);
    int cur_rp = 0;
    while (cur_rp < bin_file_size) {
        int r_cnt = fread(bytes_buffer, sizeof(BYTE), BUFFER_SIZE, bin_file);
        cur_rp += r_cnt;
        output_bin(target_file, bytes_buffer, r_cnt);
    }
    return 0;
}