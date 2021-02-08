import random
import copy

gene_length = 100
population = 100
offspring_n = 100
generation = 100
mutation_rate = 1.0 / 100.0

#初期個体群生成
def initialize():
    gene = [[random.randint(0, 1) for i in range(gene_length)] for j in range(population)]
    return gene

# 個体評価
def evaluate(gene):
    fitness = []
    for i in range(population):
        fitness.append(sum(gene[i]) / gene_length)
    return fitness

#print(evaluate(initialize()))

# 最小値
def find_min(fitness):
    min = 10
    for i in range(population):
        if fitness[i] < min:
            min = fitness[i]
    return min

# 最大値
def find_max(fitness):
    max = 0
    for i in range(population):
        if fitness[i] > max:
            max = fitness[i]
    return max

# 親選択
def choice_parents(gene, fitness):
    father_index = random.randint(0, population-1)
    mother_index = randome.randint(0, population-1)
    if fitness[father_index] > fitness[mother_index]:
        parent = gene[father_index]
    else:
        parent = gene[mother_index]
    return parent

# 交叉
def crossover(father, mother):
    offspring = []
    for i in range(gene_length):
        p = random.random()
        if p < 0.5:
            offspring.append(father[i])
        else:
            offspring.append(mother[i])
    return offspring

# 突然変異
def mutation(offspring):
    