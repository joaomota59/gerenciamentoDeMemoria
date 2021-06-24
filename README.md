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
Estratégia tradicional - Tempo médio: 0.4177620666666666
Estratégia com mmap: - Tempo médio: 0.28859309999999994

16 MB
Estratégia tradicional - Tempo médio: 0.8374720333333334
Estratégia com mmap: - Tempo médio: 0.5762752999999998

32 MB
Estratégia tradicional - Tempo médio: 1.6836472999999998
Estratégia com mmap: - Tempo médio: 1.160039

64 MB
Estratégia tradicional - Tempo médio: 3.366888233333333
Estratégia com mmap: - Tempo médio: 2.2923849666666682

128 MB
Estratégia tradicional - Tempo médio: 6.7216032
Estratégia com mmap: - Tempo médio: 4.559189333333333

256 MB
Estratégia tradicional - Tempo médio: 13.428553066666666
Estratégia com mmap: - Tempo médio: 9.07283826666667

512 MB
Estratégia tradicional - Tempo médio: 26.760279500000006
Estratégia com mmap: - Tempo médio: 18.22266400000001
```
![Leitura com método tradicional e com mmap](https://imgur.com/0ZIzndD.png)

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
