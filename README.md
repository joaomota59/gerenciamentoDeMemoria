# Gerenciamento De Memória

## Downloads necessários:
* Arquivos de entrada utilizados: https://drive.google.com/drive/u/1/folders/1mrjKXamBoXfU5X-7loa0xInKnZqo8Pqi
> Obs: coloque todos arquivos no mesmo diretório do arquivo mmap.py

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

