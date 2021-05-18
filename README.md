## Bin2Mem

Bin2Mem is a Tiny tools to convert MIPS assembly instructions into machine code in character form. Just for the convenience of filling COE files for Vivado.

### How to use

#### 1. Generate Hex

Put your file `your_file_name.s` and conver.py in the same directory

```she
python convert.py your_file_name.s
```

Then you will see a directory with the same name of your file.

#### 2. Clean

```shell
python convert.py clean
```

#### 3. Save processing files

```shell
python convert.py your_file_name.s -s
```

It will save files like *.o

#### 4. bin

You can see the file `Bin2Mem.c`. I set the buffer to 1024. If your program is lager, change it.

### More ?

Just keep simple for convenience.

Hope u enjoy it.