#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// CONSTANTES
const int MEMORY_SIZE = 1024 / sizeof(int);


// ESTRUTURAS

typedef struct process
{
    int pid;
    int size;
    int base;
    int limit;
    int is_allocated;
    struct process *next;
} Process;

typedef struct memory {
    Process *head;
    int size;
    int len_processes;
} Memory;


// FUNÇÕES DE MEMORIA 

Memory * createMemory() {
    Memory * new_memory = (Memory*)malloc(sizeof(Memory));
    new_memory->head = NULL;
    new_memory->size = MEMORY_SIZE;
    new_memory->len_processes = 0;
}

int lenRunningProcesses(Memory *memory) {
    return memory->len_processes;
}

int memoryIsEmpty(Memory *memory) {
    return (lenRunningProcesses(memory) == 0) ? 1 : 0;
}

void delMemory(Memory *memory) {
    Process *aux_process = memory->head;

    while (aux_process != NULL) {
        memory->head = aux_process->next;
        free(aux_process);
        aux_process = memory->head;
    }

    free(memory);
}

void delProcessByPID(Memory *memory, int pid) {
    if (memory->head == NULL) {
        printf("PID não encontrado!\n");
        return;
    }

    Process *current = memory->head;
    Process *previous = NULL;

    while (current != NULL) {
        if (current->pid == pid) {
            if (previous == NULL) {
                memory->head = current->next;
            } else {
                previous->next = current->next;
            }
            free(current);
            memory->len_processes--;
            printf("Processo PID %d removido.\n", pid);
            return;
        }
        previous = current;
        current = current->next;
    }
    printf("PID não encontrado!\n");
}

void addProcess(Memory *memory, Process *process) {
    if (memory->head == NULL) {
        memory->head = process;
        process->base = 0;
        process->limit = process->size - 1;
    } else {
        Process *aux_process = memory->head;
        while (aux_process->next != NULL) {
            aux_process = aux_process->next;
        }

        aux_process->next = process;
        process->base = aux_process->limit + 1;
        process->limit = process->base + process->size;
    }

    process->is_allocated = 1;
    process->next = NULL;
}

int calPartitionMemory(Process *left_process, Process * right_process) {
    int partition_memory = right_process->base - left_process->limit - 1;

    return partition_memory;
}

void allocateFirstFit(Memory *memory, Process *process) {
    if (memoryIsEmpty(memory)) {
        addProcess(memory, process);

        return;
    }

    Process *aux_process = (Process*)malloc(sizeof(Process));
    aux_process = memory->head;

    int left = 0, right = 0;
    while (aux_process->next != NULL)
    {
        left = aux_process->limit;
        right = aux_process->next->base;
        
        int partition_memory = right - left;

        if (process->size <= partition_memory) {
            process->base = left + 1;
            process->limit = process->base + process->size;
            process->is_allocated = 1;
            process->next = aux_process->next;
            aux_process->next = process;
            return;
        } else {
            aux_process = aux_process->next;
        }
    }

    left = aux_process->limit;
    if (MEMORY_SIZE - left >= process->size) {
        process->base = left + 1;
        process->limit = process->base + process->size;
        aux_process->next = process;
        process->is_allocated = 1;
        process->next = NULL;
    } else {
        printf("\nNão há espaço suficiente na memória para o processo PID: %d, Size: %d\n", process->pid, process->size);
        free(process);
    }
}

// Process * getProcessByPID(Memory *memory, int pid) {
//     if (memoryIsEmpty(memory)) {
//         return NULL;
//     }

//     Process *aux_process = memory->head;

//     while (aux_process != NULL) {
//         if (aux_process->pid == pid) {
//             return aux_process;
//         }
//         aux_process = aux_process->next;
//     }

//     return NULL;
// }

void allocateBestFit(Memory *memory, Process *process) {
    if (memoryIsEmpty(memory)) {
        addProcess(memory, process);
        return;
    }

    Process *aux_process = memory->head;
    Process *best_partition = NULL;
    int best_partition_memory = MEMORY_SIZE + 1;

    // Loop para encontrar a melhor partição
    while (aux_process->next != NULL) {
        int partition_memory = calPartitionMemory(aux_process, aux_process->next);
        if (partition_memory >= process->size && partition_memory < best_partition_memory) {
            best_partition_memory = partition_memory;
            best_partition = aux_process;
        }
        aux_process = aux_process->next;
    }

    int remaining_memory = MEMORY_SIZE - aux_process->limit;
    printf("%d", aux_process->limit);
    printf("\n\n%d, %d", remaining_memory, best_partition_memory);
    if (remaining_memory >= process->size && remaining_memory < best_partition_memory) {
        best_partition = aux_process;
    }

    // Verifica se encontrou uma partição adequada
    if (best_partition != NULL) {
        process->next = best_partition->next;
        best_partition->next = process;
        process->base = best_partition->limit + 1;
        process->limit = process->base + process->size - 1;
        memory->len_processes++;
    } else {
        addProcess(memory, process);
    }
}

void allocateWorstFit(Memory *memory, Process *process) {
    if (memoryIsEmpty(memory)) {
        addProcess(memory, process);
        return;
    }

    Process *aux_process = memory->head;
    Process *worst_partition = NULL;
    int worst_partition_memory = 0;

    // Loop para encontrar a melhor partição
    while (aux_process->next != NULL) {
        int partition_memory = calPartitionMemory(aux_process, aux_process->next);
        if (partition_memory >= process->size && partition_memory > worst_partition_memory) {
            worst_partition_memory = partition_memory;
            worst_partition = aux_process;
        }
        aux_process = aux_process->next;
    }

    int remaining_memory = MEMORY_SIZE - aux_process->limit;
    if (remaining_memory >= process->size && remaining_memory > worst_partition_memory) {
        worst_partition = aux_process;
    }

    // Verifica se encontrou uma partição adequada
    if (worst_partition != NULL) {
        process->next = worst_partition->next;
        worst_partition->next = process;
        process->base = worst_partition->limit + 1;
        process->limit = process->base + process->size - 1;
        memory->len_processes++;
    } else {
        addProcess(memory, process);
    }
}


/* Alocação de Processos
- First Fit
- Best Fit
- Worst Fit
*/

void printMemory(Memory *memory) {
    Process *aux_process = (Process*)malloc(sizeof(Process));
    aux_process = memory->head;

    printf("\npid | size | base | limit | allocated");
    while (aux_process != NULL)
    {
        printProcess(aux_process);
        aux_process = aux_process->next;
    }
}


// FUNÇÕES DE PROCESSOS

int generateRandomProcessSize() {
    return 1 + (rand() % (MEMORY_SIZE + 1));
}

Process * createProcess(int pid) {
    Process *new_process = (Process *)malloc(sizeof(Process));
    if (new_process == NULL) {
        printf("Erro na alocação de memória para o processo.\n");
        exit(1);
    }

    new_process->pid = pid;
    new_process->size = generateRandomProcessSize();
    new_process->base = -1; // Base não alocada
    new_process->limit = -1; // Limit não alocada
    new_process->is_allocated = 0; // Não alocado inicialmente
    new_process->next = NULL;

    return new_process;
}

void printProcess(Process *process) {
    printf("\n%d | %d | %d | %d | %d", process->pid, process->size, process->base, process->limit, process->is_allocated);
}

void main() {
    int pid = 0;
    srand(time(NULL));
    
    Memory * memory = createMemory();
    
    Process *p1 = (Process *)malloc(sizeof(Process));
    p1->pid = 1;
    p1->size = 20;
    p1->next = NULL;
    allocateBestFit(memory, p1);

    Process *p2 = (Process *)malloc(sizeof(Process));
    p2->pid = 2;
    p2->size = 15;
    p2->next = NULL;
    allocateBestFit(memory, p2);

    Process *p3 = (Process *)malloc(sizeof(Process));
    p3->pid = 3;
    p3->size = 25;
    p3->next = NULL;
    allocateBestFit(memory, p3);

    Process *p4 = (Process *)malloc(sizeof(Process));
    p4->pid = 4;
    p4->size = 10;
    p4->next = NULL;
    allocateBestFit(memory, p4);

    Process *p5 = (Process *)malloc(sizeof(Process));
    p5->pid = 5;
    p5->size = 936;
    p5->next = NULL;
    allocateBestFit(memory, p5);

    printf("Estado da memória após alocação:\n");
    printMemory(memory);

    // Remover alguns processos
    delProcessByPID(memory, 2);
    delProcessByPID(memory, 4);

    printf("Estado da memória após remoção de processos:\n");
    printMemory(memory);

    // Adicionar novos processos
    Process *p6 = (Process *)malloc(sizeof(Process));
    p6->pid = 6;
    p6->size = 12;
    p6->next = NULL;
    allocateBestFit(memory, p6);

    Process *p7 = (Process *)malloc(sizeof(Process));
    p7->pid = 7;
    p7->size = 8;
    p7->next = NULL;
    allocateBestFit(memory, p7);

    printf("Estado da memória após novas alocações:\n");
    printMemory(memory);

    // Liberar memória alocada
    Process *temp;
    while (memory->head != NULL) {
        temp = memory->head;
        memory->head = memory->head->next;
        free(temp);
    }


}