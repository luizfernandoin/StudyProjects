#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct fila {
    int *paginas;
    int capacidade;
    int primeiro;
    int ultimo;
    int nItens;
} Fila;

void limparFila(Fila *fila) {
    for (int i = 0; i <= fila->capacidade-1; i++) {
        fila->paginas[i] = -1;
    }
}

Fila * criarFila(int capacidade) {
    Fila *fila = (Fila*) malloc(sizeof(Fila));
    limparFila(fila);

    fila->capacidade = capacidade;
    fila->paginas = (int*) malloc(fila->capacidade * sizeof(int));
    fila->primeiro = 0;
    fila->ultimo = -1;
    fila->nItens = 0;

    return fila;
}

int estaNaFila(Fila *fila, int valor) {
    for (int i = 0; i <= fila->capacidade-1; i++) {
        if (fila->paginas[i] == valor) {
            return 1;
        }
    }

    return 0;
}

void organizarFila(Fila *fila) {
    for (int index = 0; index < fila->ultimo; index++) {
        fila->paginas[index] = fila->paginas[index+1];
    }

    fila->ultimo--;
    fila->nItens--;
}

void inserir(Fila * fila, int valor) {
    if (fila->ultimo == fila->capacidade-1) {
        organizarFila(fila);
    }

    fila->ultimo++;
    fila->paginas[fila->ultimo] = valor;
    fila->nItens++;
}

void exibirFila(Fila *fila) {
    printf("Memória: [");
    for (int i = 0; i < fila->nItens; i++) {
        int index = (fila->primeiro + i) % fila->capacidade;
        printf("%d", fila->paginas[index]);

        if (i < fila->nItens - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}

int* receberSequencia(char* input, int* numPaginas) {
    char* token;
    int* sequencia = NULL;
    *numPaginas = 0;

    input[strcspn(input, "\n")] = '\0';

    input[strcspn(input, "[")] = ' ';
    input[strcspn(input, "]")] = ' ';

    token = strtok(input, ", ");
    while (token != NULL) {
        sequencia = (int*) realloc(sequencia, (*numPaginas + 1) * sizeof(int));
        sequencia[*numPaginas] = atoi(token);
        (*numPaginas)++;
        token = strtok(NULL, ", ");
    }
    return sequencia;
}


int main() {
    int capacidade, numPaginas;
    char input[100];

    printf("Digite o número de molduras: ");
    scanf("%d", &capacidade);
    getchar();

    Fila *fila = criarFila(capacidade);

    printf("Digite a sequência de páginas no formato [1, 3, 0, 3, ...]: ");
    fgets(input, sizeof(input), stdin);

    int* sequenciaPaginas = receberSequencia(input, &numPaginas);

    int falhasDePagina = 0;
    for (int i = 0; i < numPaginas; i++) {
        int paginaAtual = sequenciaPaginas[i];
        int presenteNaMemoria = estaNaFila(fila, paginaAtual);

        if (!presenteNaMemoria) {
            inserir(fila, paginaAtual);
            falhasDePagina++;

            printf("Após inserir a página %d: ", paginaAtual);
            exibirFila(fila);
        }
    }

    printf("====================\n");
    printf("Total de falhas de página: %d\n", falhasDePagina);
    exibirFila(fila);

    free(fila->paginas);
    free(fila);
    free(sequenciaPaginas);

    return 0;
}