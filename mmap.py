import timeit
import mmap

print("Selecione alguma opção\n")
entrada = int(input('Leitura mmap [1]\nEscrita mmap [2]\n->'))

###Leitura mmap###

if entrada == 1:
    SETUP_CODE = '''import mmap'''


    TEST_CODE = '''
def mmap_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()
            
mmap_io('996-0.txt')
'''
    resultadoMmapLeitura = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat=3, number = 1)
    print(resultadoMmapLeitura)
    
###Escrita mmap###

#TEST_CODE2 =
elif entrada == 2:
    def mmap_io_write(filename, text):
        with open(filename, mode="a", encoding="utf-8") as file_obj:
            with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
                mmap_obj.write(text)


    mmap_io_write('996-0.txt','1')


    resultadoMmapEscrita = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE2, repeat=3, number = 1)
