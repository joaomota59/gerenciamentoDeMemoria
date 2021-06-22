# Gerenciamento De Memória

## Downloads necessários:
* Arquivos de entrada utilizados: https://drive.google.com/drive/u/1/folders/1mrjKXamBoXfU5X-7loa0xInKnZqo8Pqi
> Obs: coloque todos arquivos no mesmo diretório do arquivo gdMemoria.py

## Comandos no shell
```shell
sudo apt install python3-pip
pip install matplotlib
python3 gdMemoria.py
```



## Resultados

### Leitura

```java

8 MB
Estratégia tradicional - Tempo médio: 0.014212866666666546
Estratégia com mmap: - Tempo médio: 0.00968333333333334

16 MB
Estratégia tradicional - Tempo médio: 0.02773693333333327
Estratégia com mmap: - Tempo médio: 0.018899533333333347

32 MB
Estratégia tradicional - Tempo médio: 0.05511379999999999
Estratégia com mmap: - Tempo médio: 0.04004603333333323

64 MB
Estratégia tradicional - Tempo médio: 0.1106994999999998
Estratégia com mmap: - Tempo médio: 0.07480633333333353

128 MB
Estratégia tradicional - Tempo médio: 0.2255226
Estratégia com mmap: - Tempo médio: 0.14911273333333316

256 MB
Estratégia tradicional - Tempo médio: 0.44676449999999984
Estratégia com mmap: - Tempo médio: 0.3040315000000004

512 MB
Estratégia tradicional - Tempo médio: 0.8843036666666672
Estratégia com mmap: - Tempo médio: 0.6022681000000004
```
![Leitura com método tradicional e com mmap](https://imgur.com/VLRKThA.png)

### Escrita

```java
8 MB
Estratégia tradicional - Tempo médio: 0.0005479000000000825
Estratégia com mmap: - Tempo médio: 0.001445566666666694

16 MB
Estratégia tradicional - Tempo médio: 0.0005335000000001126
Estratégia com mmap: - Tempo médio: 0.00099536666666659

32 MB
Estratégia tradicional - Tempo médio: 0.000552466666666677
Estratégia com mmap: - Tempo médio: 0.0009035999999998564

64 MB
Estratégia tradicional - Tempo médio: 0.0005083666666666117
Estratégia com mmap: - Tempo médio: 0.0009968333333333728

128 MB
Estratégia tradicional - Tempo médio: 0.0005588999999999918
Estratégia com mmap: - Tempo médio: 0.0008254666666666447

256 MB
Estratégia tradicional - Tempo médio: 0.000642533333333232
Estratégia com mmap: - Tempo médio: 0.0009515333333333468

512 MB
Estratégia tradicional - Tempo médio: 0.0005237333333332946
Estratégia com mmap: - Tempo médio: 0.0009439666666664811
```
![Escrita com método tradicional e com mmap](https://imgur.com/MdR4JJW.png)

> Obs: Cada tamanho foi executado individualmente 3 vezes e em seguida foi tirado o tempo médio correspondente.

## Conclusões
* A leitura com mmap em todos cenários, desde arquivos menores até arquivos maiores, é mais rápida que a leitura tradiconal.
* A leitura com mmap, como pode-se observar no gráfico de leitura, em cenários de arquivos maiores tamanhos compensa ainda mais que a leitura convencional.
* A escrita com mmap, têm-se uma grande variação, porém em comparação com a escrita tradicional, em todos cenários, é pior que a escrita tradicional.
> Obs: Os testes foram realizados em diferentes máquinas e apesar de algumas variações no gráfico, todos testes chegaram a mesma conclusão.
