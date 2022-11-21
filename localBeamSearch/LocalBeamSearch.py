import random
import numpy as np

def getValue(state, values):
    sum =0
    for i in range(len(state)):
        if state[i] == 1:
            sum = sum + values[i]
    return sum

def generateNewStates(open_list_k,open_list):
    open_list.clear()
    for i in range(len(open_list_k)):
        for j in range(len(open_list_k[i])):
            if open_list_k[i][j] == 0:
                open_list_k[i][j]=1
                open_list.append(np.copy(open_list_k[i]))
                open_list_k[i][j]=0


def getHeuristicCost(state,classes,values,weights,maxOfValue):
    HeuristicCost=0
    holdClass=[]
    for i in range(len(state)):
        if state[i] ==1 :
            if classes[i] in holdClass:
                HeuristicCost+=(values[i]/weights[i]) - maxOfValue
            else :
                HeuristicCost+=(values[i]/weights[i])
                holdClass.append(classes[i])
    return HeuristicCost
def getWeight(state,weights):
    weight=0
    for i in range(len(state)):
        if state[i] == 1:
            weight +=weights[i]
    return weight

def generateRandomState(open_list_k,open_list,W,k,maxOfValue,classes,values,weights):
    ScoreList=[]
    open_list_k.clear()
    for i in range(len(open_list)):
        ScoreList.append(getHeuristicCost(open_list[i],classes,values,weights,maxOfValue),)
    top_k_idx = np.argsort(ScoreList)[-k:]
    for i in top_k_idx:
        if getWeight(open_list[i],weights)<=W:
            open_list_k.append(open_list[i])
def localBeam(input_file, output_file):
    output_file=open(f"{output_file}","w")
    dataset_file = open(f"{input_file}", "r")
    lines = dataset_file.readlines()
    W = int(lines[0])
    numberOfTypes = int(lines[1])
    weights = list(map(int,lines[2].replace("\n", "").split(",")))
    values = list(map(int,lines[3].replace("\n", "").split(",")))
    classes = list(map(int,lines[4].replace("\n", "").split(",")))
    maxOfValue=max(values)
    k = random.randint(1,len(weights))
    open_list = []
    open_list_k = [[0]*len(classes)]
    new_array=[]
    while open_list_k != []:
        generateNewStates(open_list_k,open_list)
        generateRandomState(open_list_k,open_list,W,k,maxOfValue,classes,values,weights)
        if open_list_k != []:
            for i in range(len(open_list_k)):
                new_array.append(np.copy(open_list_k[i]))
    ScoreGoalList = []
    for i in range(len(new_array)):
            ScoreGoalList.append(getValue(new_array[i],values))
    max_value=max(ScoreGoalList)
    max_index = ScoreGoalList.index(max_value)
    print(getValue(new_array[max_index],values))
    print(new_array[max_index])
    print(f"{getValue(new_array[max_index],values)}")
    output_file.write(f"{getValue(new_array[max_index],values)}\n")
    print(f"{new_array[max_index]}")
    output_file.write(f"{new_array[max_index].tolist()}".replace('[','').replace(']','') + "\n")
    output_file.close()
    dataset_file.close()

if __name__ == "__main__":
    localBeam(input_file="testcases/small_dataset/INPUT_1.txt", output_file="localBeamSearch/output/small_dataset/OUTPUT_1.txt")
    localBeam(input_file="testcases/small_dataset/INPUT_2.txt", output_file="localBeamSearch/output/small_dataset/OUTPUT_2.txt")
    localBeam(input_file="testcases/small_dataset/INPUT_3.txt", output_file="localBeamSearch/output/small_dataset/OUTPUT_3.txt")
    localBeam( input_file="testcases/small_dataset/INPUT_4.txt", output_file="localBeamSearch/output/small_dataset/OUTPUT_4.txt")
    localBeam( input_file="testcases/small_dataset/INPUT_5.txt", output_file="localBeamSearch/output/small_dataset/OUTPUT_5.txt")
    localBeam( input_file="testcases/large_dataset/INPUT_1.txt", output_file="localBeamSearch/output/large_dataset/OUTPUT_1.txt")
    localBeam( input_file="testcases/large_dataset/INPUT_2.txt", output_file="localBeamSearch/output/large_dataset/OUTPUT_2.txt")
    localBeam( input_file="testcases/large_dataset/INPUT_3.txt", output_file="localBeamSearch/output/large_dataset/OUTPUT_3.txt")
    localBeam( input_file="testcases/large_dataset/INPUT_4.txt", output_file="localBeamSearch/output/large_dataset/OUTPUT_4.txt")
    localBeam( input_file="testcases/large_dataset/INPUT_5.txt", output_file="localBeamSearch/output/large_dataset/OUTPUT_5.txt")

             






