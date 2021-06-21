#Link de referência: https://realpython.com/python-mmap/
import timeit
import mmap

def mmap_io_read(filename):#Leitura mmap
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()

def regular_io_read(filename):#Leitura convencional
    with open(filename, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()

def mmap_io_write(filename):#Escrita mmap
    with open(filename, mode="r+", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            mmap_obj[0:6] = b"python"
            mmap_obj.flush()

def regular_io_write(filename):#Escrita convencional
    with open(filename, mode="r+", encoding="utf8") as file_obj:
        file_obj.write("python")

files = ['8.txt','16.txt','32.txt','64.txt','128.txt','256.txt','512.txt']

print("Selecione alguma opção\n")
entrada = int(input('Leitura [1]\nEscrita [2]\n->'))

for filename in files:

    if entrada == 1:#Leitura de arquivo
        k = timeit.repeat(
        "regular_io_read(filename)",
        repeat=3,
        number=1,
        setup="from __main__ import regular_io_read, filename")

        x = timeit.repeat(
        "mmap_io_read(filename)",
        repeat=3,
        number=1,
        setup="from __main__ import mmap_io_read, filename")

        print(filename[:-4]+" MB")
        print("Estratégia tradicional - Tempo médio:",sum(k)/len(k))
        print("Estratégia com mmap: - Tempo médio:",sum(x)/len(x))
        print()
        
    elif entrada == 2:#Escrita de arquivo
        
        k = timeit.repeat(
        "regular_io_write(filename)",
        repeat=3,
        number=1,
        setup="from __main__ import regular_io_write, filename")

        x = timeit.repeat(
        "mmap_io_write(filename)",
        repeat=3,
        number=1,
        setup="from __main__ import mmap_io_write, filename")

        print(filename[:-4]+" MB")
        print("Estratégia tradicional - Tempo médio:",sum(k)/len(k))
        print("Estratégia com mmap: - Tempo médio:",sum(x)/len(x))
        print()
