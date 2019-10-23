## Estudar os geradores de números pseudoaleatório que o Linux utiliza: rand, rand_r, srand e verificar de onde o Linux obtém entropia.

### rand
O rand() retorna um número inteiro pseudo-aleatório no intervalo de 0 a RAND_MAX, inclusive (isto é, o intervalo matemático.

### rand-r
O retorna um número inteiro pseudo-aleatório no intervalo [0, RAND_MAX ]. O argumento seedp é um ponteiro para um int sem sinal usado para armazenar o estado entre as chamadas. Se rand_r () for chamado com o mesmo valor inicial para o número inteiro apontado por seedp , e esse valor não for modificado entre as chamadas, a mesma sequência pseudo-aleatória resultará.

### srand
O srand () define seu argumento como a semente de uma nova sequência de números inteiros pseudo-aleatórios a serem retornados por rand (). Essas seqüências são repetíveis se for chamado o srand () com o mesmo valor inicial.

### Entropia do Linux

O sistema permite acesso aos ruídos do ambiente coletados de controladores de dispositivos e outras fontes, desta forma acessam funções de hardware sem precisar saber detalhes precisos sobre o hardware que está sendo usado  e obtem valores para gerar os valores pseudoaleatorio. Em sistemas linux o ```/dev/random``` normalmente bloqueia se houver menos entropia disponível do que o solicitado.

## Exemplos
 
o exemplo a seguir de uma implementação de rand () e srand (), possivelmente útil quando se precisa da mesma sequência em duas máquinas diferentes.

```c
static unsigned long next = 1;

/* RAND_MAX assumed to be 32767 */
int myrand(void) {
    next = next * 1103515245 + 12345;
    return((unsigned)(next/65536) % 32768);
}

void mysrand(unsigned int seed) {
    next = seed;
}

``` 
O proximo exemplo pode ser usado para exibir a sequência pseudo-aleatória produzida por rand() quando recebe uma semente específica. 

```c
#include <stdlib.h>
#include <stdio.h>

int
main(int argc, char *argv[])
{
    int j, r, nloops;
    unsigned int seed;

    if (argc != 3) {
        fprintf(stderr, "Usage: %s <seed> <nloops>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    seed = atoi(argv[1]);
    nloops = atoi(argv[2]);

    srand(seed);
    for (j = 0; j < nloops; j++) {
        r =  rand();
        printf("%d\n", r);
    }

    exit(EXIT_SUCCESS);
}
``` 
