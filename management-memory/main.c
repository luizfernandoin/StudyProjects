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
        printf("Não há espaço suficiente na memória para o processo PID: %d, Size: %d\n", process->pid, process->size);
        free(process);
    }
}

Process * getProcessByPID(Memory *memory, int pid) {
    if (memoryIsEmpty(memory)) {
        return;
    }
    
    Process *aux_process = (Process*)malloc(sizeof(Process));
    aux_process = memory->head;


    while (aux_process != NULL)
    {
        if (aux_process->pid == pid) {
            return aux_process;
        }

        aux_process = aux_process->next;
    }
}

void allocateBestFit(Memory *memory, Process *process) {
    if (memoryIsEmpty(memory)) {
        addProcess(memory, process);

        return;
    }

    Process *aux_process = (Process*)malloc(sizeof(Process));
    aux_process = memory->head;

    int left = 0, right = 0;
    int aux_pid = -1;
    while (aux_process->next != NULL)
    {
        left = aux_process->limit;
        right = aux_process->next->base;
        
        int partition_memory = right - left;

        if (process->size <= partition_memory) {
            
        }
    }
    
}

// void allocateWorstFit() {
    
// }


/* Alocação de Processos
- First Fit
- Best Fit
- Worst Fit
*/

void printMemory(Memory *memory) {
    Process *aux_process = (Process*)malloc(sizeof(Process));
    aux_process = memory->head;

    printf("pid | size | base | limit | allocated");
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
    for (int c = 0; c < 5; c++) {
        Process * process = createProcess(pid);
        addProcess(memory, process);

        pid++;
    }

    printMemory(memory);
}