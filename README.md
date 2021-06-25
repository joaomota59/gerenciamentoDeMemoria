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
Estratégia tradicional - Tempo médio: 1.2956128
Estratégia com mmap: - Tempo médio: 0.4085434666666667

16 MB
Estratégia tradicional - Tempo médio: 2.1846107666666668
Estratégia com mmap: - Tempo médio: 0.4701303999999998

32 MB
Estratégia tradicional - Tempo médio: 4.384367166666666
Estratégia com mmap: - Tempo médio: 0.5984439999999994

64 MB
Estratégia tradicional - Tempo médio: 7.899791233333333
Estratégia com mmap: - Tempo médio: 1.090882599999998

128 MB
Estratégia tradicional - Tempo médio: 15.272900666666665
Estratégia com mmap: - Tempo médio: 1.921779833333332

256 MB
Estratégia tradicional - Tempo médio: 30.460632
Estratégia com mmap: - Tempo médio: 3.4705263666666704

512 MB
Estratégia tradicional - Tempo médio: 59.91307493333334
Estratégia com mmap: - Tempo médio: 6.505290433333319
```
![Escrita com método tradicional e com mmap](https://imgur.com/AnBFHGY.png)

## Considerações adotadas

* Na leitura, cada tamanho foi executado individualmente 3 vezes e, em cada vez, foi executado o mesmo trecho de código 30 vezes.
* Na escrita, cada tamanho foi executado individualmente 3 vezes e, em cada vez, foi executado o mesmo trecho de código 1000 vezes.
* A média do tempo, para cada tamanho, é determinada pela a quantidade de vezes que o determinado trecho de código foi executado pelo o número de vezes que houve essa execução.
* Neste caso, a fórmula adotada para o tempo médio foi: Tempo_Medio = &#8721;(quant_de_Vezes_do_trecho_de_codigo)/3 .

## Conclusões
* A leitura com mmap em todos cenários, desde arquivos menores até arquivos maiores, é mais rápida que a leitura tradiconal.
* A leitura com mmap, como pode-se observar no gráfico de leitura, em cenários de arquivos maiores tamanhos compensa ainda mais que a leitura tradicional.
* A escrita com mmap, na maioria dos cenários, desde arquivo menores até arquivos maiores, apresentou um melhor desempenho, porém em alguns testes, seu desempenho chegava bem próximo do desempenho com o método de escrita tradicional e as vezes apresentava um desempenho inferior(isso geralmente ocorreu nos testes realizados em arquivos abaixo de 32MB, após isso, em todos ou arquivos maiores o desempenho ficava superior ao método tradicional).
* Levando em conta o tópico acima, a escrita com mmap, com forma semelhante a leitura, compensa ainda mais quando se tem arquivos grandes(pois seu desempenho fica bem melhor), em comparação com o método tradicional, podendo as vezes(para arquivos pequenos) não apresentar um desempenho tão relevante.
> Obs: Os testes foram realizados em diferentes máquinas e apesar de algumas variações no gráfico, todos testes chegaram a mesma conclusão.
