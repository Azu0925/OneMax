import random
import copy

gene_length = 100
population = 100
offspring_n = 100
generation = 100
mutation_rate = 1.0 / 100.0

def initialize():
    gene = [[random.randint(0, 1) for i in range(gene_length)] for j in range(population)]
    return gene

def evaluate(gene):
    fitness = []
    for i in range(population):
        fitness.append(sum(gene[i]) / gene_length)
    return fitness

#print(evaluate(initialize()))

def find_min(fitness):
    min = 10
    for i in range(population):
        if fitness[i] < min:
            min = fitness[i]
    return min

def find_max(fitness):
    max = 0
    for i in range(population):
        if fitness[i] > max:
            max = fitness[i]
    return max

def choice_parents(gene, fitness):
    father_index = random.randint(0, population-1)
    mother_index = randome.randint(0, population-1)
    if fitness[father_index] > fitness[mother_index]:
        parent = gene[father_index]
    else:
        parent = gene[mother_index]
    return parent

def crossover(father, mother):
    offspring = []
    for i in range(gene_length):
        p = random.random()
        if p < 
