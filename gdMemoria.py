#Link de referência: https://realpython.com/python-mmap/
import timeit
import mmap
import matplotlib.pyplot as plt

def mmap_io_read(filename):#Leitura mmap
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()

def regular_io_read(filename):#Leitura convencional
    with open(filename, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()

def mmap_io_write(filename):#Escrita mmap
    with open(filename, mode="r+") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            mmap_obj[0:50000] = b"a"*50000
            mmap_obj.close()

def regular_io_write(filename):#Escrita convencional
    with open(filename, mode="r+") as file_obj:
        file_obj.write("a"*50000)

files = ['8.txt','16.txt','32.txt','64.txt','128.txt','256.txt','512.txt']

print("Selecione alguma opção\n")
entrada = int(input('Leitura [1]\nEscrita [2]\n->'))
if(entrada == 1 or entrada ==2):
    print("\nProcessando gráfico...\nPor favor, espere.")

resultadosTradicional = []
resultadosMmap = []

for filename in files:

    if entrada == 1:#Leitura de arquivo
        k = timeit.repeat(
        "regular_io_read(filename)",
        repeat=3,
        number=2,
        setup="from __main__ import regular_io_read, filename")

        x = timeit.repeat(
        "mmap_io_read(filename)",
        repeat=3,
        number=2,
        setup="from __main__ import mmap_io_read, filename")

        #print(filename[:-4]+" MB")
        #print("Estratégia tradicional - Tempo médio:",sum(k)/len(k))
        #print("Estratégia com mmap: - Tempo médio:",sum(x)/len(x))
        #print()
        resultadosTradicional.append(sum(k)/len(k))
        resultadosMmap.append(sum(x)/len(x))
        
    elif entrada == 2:#Escrita de arquivo
        
        k = timeit.repeat(
        "regular_io_write(filename)",
        repeat=3,
        number=4000,
        setup="from __main__ import regular_io_write, filename")

        x = timeit.repeat(
        "mmap_io_write(filename)",
        repeat=3,
        number=4000,
        setup="from __main__ import mmap_io_write, filename")

        #print(filename[:-4]+" MB")
        #print("Estratégia tradicional - Tempo médio:",sum(k)/len(k))
        #print("Estratégia com mmap: - Tempo médio:",sum(x)/len(x))
        #print()
        resultadosTradicional.append(sum(k)/len(k))
        resultadosMmap.append(sum(x)/len(x))
if entrada == 1 or entrada ==2:
    fig, ax = plt.subplots()
    if (entrada == 1):
        ax.set_title('Leitura tradicional e Leitura mmap')
    else:
        ax.set_title('Escrita tradicional e Escrita mmap')
    ax.plot([i[:-4] for i in files],resultadosTradicional,label="tradicional")
    ax.plot([i[:-4] for i in files],resultadosMmap,label="mmap")
    ax.set_xlabel('Tamanho do arquivo(MB)')
    ax.set_ylabel('Tempo médio de execução(s)')
    ax.legend()
    plt.show()
