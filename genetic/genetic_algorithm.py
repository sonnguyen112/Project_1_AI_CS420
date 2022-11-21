import random
import sys
import copy
import numpy as np

GENS = [0, 1]
POPULATION_SIZE = 100

class GeneticAlgo():
    def __init__(self, capacity, nums_of_class, weights, values, class_label):
        self.capacity = capacity
        self.nums_of_class = nums_of_class
        self.weights = weights
        self.values = values
        self.class_label = class_label
        self.target_size = len(weights)

    def make_gens_mutation(self):
        global GENS
        return random.choice(GENS)

    def make_new_gnorm(self):
        global GENS
        new_gnorm = []

        for _ in range(self.target_size):
            new_gnorm.append(self.make_gens_mutation())

        return new_gnorm

    def check_gnorm_valid(self, gnorm):
        total_weight = 0
        for index, weight in enumerate(self.weights):
            total_weight += weight * gnorm[index]
            if total_weight > self.capacity:
                return False
        check_label = [False for _ in range(self.nums_of_class + 1)]
        for index,label in enumerate(self.class_label):
            if gnorm[index] == 1:
                check_label[label] = True
        for i in range(1, len(check_label)):
            if check_label[i] == False:
                return False
        return True


    def cal_score(self, gnorm):
        total_weight = 0
        total_value = 0
        for index, weight in enumerate(self.weights):
            total_weight += weight * gnorm[index]

        for index, value in enumerate(self.values):
            total_value += value * gnorm[index]
        
        #Num Of label have
        check_label = [False for _ in range(self.nums_of_class + 1)]
        for index,label in enumerate(self.class_label):
            if gnorm[index] == 1:
                check_label[label] = True

        total_class_include = check_label.count(True)

        score = self.capacity*len(self.weights)*(total_class_include - self.nums_of_class) + self.capacity*len(self.weights)
        
        if score >= self.capacity*len(self.weights):
            score = min(self.capacity - total_weight, 0) + self.capacity*len(self.weights)

        if score >= self.capacity*len(self.weights):
            score = total_value + self.capacity*len(self.weights)

        return score

    def mate(self, gnorm1, gnorm2):
        c = random.randint(1, len(gnorm1) - 2)
        
        child_1 = gnorm1[:c] + gnorm2[c:]
        child_2 = gnorm2[:c] + gnorm1[c:]
        
        return child_1, child_2


    def cal_weight(self, gnorm):
        total_weight = 0
            
        for index, weight in enumerate(self.weights):
            total_weight += weight * gnorm[index]

        return total_weight

    def cal_val(self, item):
        total_val = 0
            
        for index, val in enumerate(self.values):
            total_val += val * item[index]

        return total_val
    
    def select_parent(self, population):
        arr = []
        total_score = sum(list(map(lambda x: x["score"], population)))
        for item in population:
            select_prob = int((item["score"] * 100) / total_score)
            # print(select_prob)
            arr += [item["gnorm"] for _ in range(select_prob)]
        
        if len(arr) != 0:
            return random.choice(arr)
        else:
            return random.choice(population)

        max_score = max(list(map(lambda x: x["score"], population)))
        total_exp_score = sum(list(map(lambda x: np.exp(x["score"] - max_score), population)))
        prob_arr = list(map(lambda x: (np.exp(x["score"] - max_score)/total_exp_score), population))
        # print(sum(prob_arr))
        selected = np.random.choice(population, 1, p = prob_arr)
        # print(selected[0]["score"] / total_score)
        return selected[0]["gnorm"]

    def mutation(self, item):
        global GENS
        item_copy = copy.deepcopy(item)
        c = random.randint(0, len(item) - 1)
        while 1:
            gen_mutaion = random.choice(GENS)
            if gen_mutaion != item[c]:
                break
        item_copy[c] = gen_mutaion

        return item_copy

    def mate_2(self, item1, items):
        child = []
        for gen1, gen2 in zip(item1, items):
            prob = random.random()

            if prob < 0.45:
                child.append(gen1)
            elif prob < 0.9:
                child.append(gen2)
            else:
                child.append(self.make_gens_mutation())
        return child
        
def run_genetic(epoch, dataset, output_file):

    # dataset_file = open("large_dataset.txt", "r")
    dataset_file = open(f"{dataset}", "r")
    lines = dataset_file.readlines()
    output_file = open(f"{output_file}", "w")
    

    capacity = int(lines[index_line])
    num_of_class = int(lines[index_line])
    weights = list(map(int,lines[index_line].replace("\n", "").split(",")))
    values = list(map(int,lines[index_line].replace("\n", "").split(",")))
    class_label = list(map(int,lines[index_line].replace("\n", "").split(",")))
    # print(capacity, num_of_class, weights, values, class_label)
    epoch = epoch
    population = []
    genetic = GeneticAlgo(capacity, num_of_class, weights, values, class_label)
    best_score = 0
    
    for _ in range(POPULATION_SIZE):
        gnorm = genetic.make_new_gnorm()
        population.append({
            "gnorm" : gnorm,
            "score" : genetic.cal_score(gnorm)
        })

    best_item = population[0]["gnorm"]
    index = 0
    while index < epoch:
        new_generation = []

        for _ in range(0, POPULATION_SIZE, 2):
            parent_1 = genetic.select_parent(population)
            parent_2 = genetic.select_parent(population)
            child_1, child_2 = genetic.mate(parent_1, parent_2)
            mutaion_prob_1 = random.random()
            mutaion_prob_2 = random.random()
            if mutaion_prob_1 > 0.9:
                child_1 = genetic.mutation(child_1)
            if mutaion_prob_2 > 0.9:
                child_2 = genetic.mutation(child_2)
            
            score_child_1 = genetic.cal_score(child_1)
            score_child_2 = genetic.cal_score(child_2)

            if max(score_child_1, score_child_2) > best_score:
                best_score = max(score_child_1, score_child_2)
                if score_child_1 > score_child_2:
                    best_item = child_1
                else:
                    best_item = child_2
            new_generation.append({
                "gnorm" : child_1,
                "score" : score_child_1
            })
            new_generation.append({
                "gnorm" : child_2,
                "score" : score_child_2
            })

        population = new_generation

        index += 1
        print(f"epoch: {index} {best_score} {genetic.cal_weight(best_item)} {genetic.cal_val(best_item)}")
    print(f"{genetic.cal_val(best_item)}")
    output_file.write(f"{genetic.cal_val(best_item)}\n")
    print(f"{best_item}")
    output_file.write(f"{best_item}".replace('[','').replace(']','') + "\n")

        
if __name__ == "__main__":
    run_genetic(epoch=5000, dataset="testcases")
