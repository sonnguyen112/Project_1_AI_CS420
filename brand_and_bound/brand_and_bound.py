
import sys

        
ans = []
maxVal = 0

def run(dataset,output_file):
    global ans,maxVal
    # dataset_file = open("large_dataset.txt", "r")
    dataset_file = open(f"{dataset}", "r")
    output_file = open(f"{output_file}", "w")
    lines = dataset_file.readlines()
    
    index_line = 0
    for i_testcase in range(len(lines)//5):

        capacity = int(lines[index_line])
        index_line += 1
        num_of_class = int(lines[index_line])
        index_line += 1
        weights = list(map(int,lines[index_line].replace("\n", "").split(",")))
        index_line += 1
        values = list(map(int,lines[index_line].replace("\n", "").split(",")))
        index_line += 1
        class_label = list(map(int,lines[index_line].replace("\n", "").split(",")))
        index_line += 1
        total_val = sum(values)
        
        make_Binary_N(len(weights),capacity,num_of_class,weights,values,class_label,total_val)
        
        output_file.write(f"{maxVal}\n")
        output_file.write(f"{ans}".replace('[', '').replace(']', '') + "\n")
        output_file.close()
        maxVal = 0
        ans = []

def make_Binary_N(size,capacity,num_of_class,weights,values,class_label,total_val):
    arr = [0 for _ in range(size)]
    BT(0,arr,size,0,0,total_val,capacity,num_of_class,weights,values,class_label,total_val)

def checkClass(array,class_label,num_of_class):
    class_num = []
    for i in range(len(array)):
        if array[i] == 1:
            class_num.append(class_label[i])
    for i in range(num_of_class):
        if i + 1 not in class_num:
            return False
    return True

def BT(index,array,size,curWeight,curValue,ableVal,capacity,num_of_class,weights,values,class_label,total_val):
    global ans,maxVal
    # print ( array,curValue,curWeight,ableVal)
    for i in range(2):
        array[index] = i
        if index == size-1:
            if i == 1:
                curW = curWeight + weights[index]
                curV = curValue + values[index]
                if ( curW < capacity and curV > maxVal and checkClass(array,class_label,num_of_class) ):
                    maxVal = curV
                    other = []
                    for i in array:
                        other.append(i)
                    ans = other
            if i == 0 :
                curW = curWeight 
                curV = curValue 
                if(curV > maxVal and checkClass(array,class_label,num_of_class)):
                    maxVal = curV
                    other = []
                    for i in array:
                        other.append(i)
                    ans = other    
        else:                       
            if i == 1:
                curW = curWeight + weights[index]
                curV = curValue + values[index]
                if ( curW < capacity):
                    BT(index+1,array,size,curW,curV,ableVal,capacity,num_of_class,weights,values,class_label,total_val)
            if i == 0 :
                curW = curWeight 
                curV = curValue 
                ableV = ableVal - values[index]
                if ( ableV > maxVal):
                    BT(index+1,array,size,curW,curV,ableV,capacity,num_of_class,weights,values,class_label,total_val)


if __name__ == "__main__":
    run( dataset="testcases/small_dataset/INPUT_1.txt",
                output_file="brand_and_bound/output/small_dataset/OUTPUT_1.txt")
    run( dataset="testcases/small_dataset/INPUT_2.txt",
                output_file="brand_and_bound/output/small_dataset/OUTPUT_2.txt")
    run( dataset="testcases/small_dataset/INPUT_3.txt",
                output_file="brand_and_bound/output/small_dataset/OUTPUT_3.txt")
    run( dataset="testcases/small_dataset/INPUT_4.txt",
                output_file="brand_and_bound/output/small_dataset/OUTPUT_4.txt")
    run( dataset="testcases/small_dataset/INPUT_5.txt",
                output_file="brand_and_bound/output/small_dataset/OUTPUT_5.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brand_and_bound/output/large_dataset/OUTPUT_1.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brand_and_bound/output/large_dataset/OUTPUT_2.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brand_and_bound/output/large_dataset/OUTPUT_3.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brand_and_bound/output/large_dataset/OUTPUT_4.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brand_and_bound/output/large_dataset/OUTPUT_5.txt")