from deap import base, creator, tools, algorithms
import random
import numpy as np

items = ((8,10),(7,13),(6,7),(5,4),(4,9),(3,3,),(2,3),(1,2))

creator.create("Fitness", base.Fitness, weights=(1.0,))
creator.create("Individual",list,fitness=creator.Fitness)

toolbox = base.Toolbox()
toolbox.register("attribute",random.randint, 0, 1)
toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attribute, len(items))
toolbox.register("population",tools.initRepeat,list,toolbox.individual)

MAX_WEIGHT=10
def evalKnapsack(individual):
    weight = 0.0
    value = 0.0
    for i in range(len(items)):
        s = individual[i]
        if s==1:
            weight += items[i][0]
            value += items[i][1]
    if weight > MAX_WEIGHT:
        return 0,

    return value,

toolbox.register("evaluate",evalKnapsack)
toolbox.register("select",tools.selTournament,tournsize=3)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate",tools.mutFlipBit, indpb=0.05)

hof = tools.ParetoFront()
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg",np.mean, axis=0)
stats.register("std",np.std, axis=0)
stats.register("min",np.min, axis=0)
stats.register("max",np.max, axis=0)

pop = toolbox.population(n=50)
algorithms.eaSimple(pop, toolbox, cxpb=0.8,mutpb=0.5,ngen=100,stats=stats,halloffame=hof, verbose=True)

best_ind = tools.selBest(pop,1)[0]
print(best_ind)
print(evalKnapsack(best_ind))
