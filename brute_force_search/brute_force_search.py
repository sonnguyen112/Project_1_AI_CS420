ans = []
def run(dataset,output_file):
    # dataset_file = open("large_dataset.txt", "r")
    dataset_file = open(f"{dataset}", "r")

    lines = dataset_file.readlines()
    
    index_line = 0

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
    BFS(capacity,num_of_class,weights,values,class_label,output_file)
    

def BFS(capacity,num_of_class,weights,values,class_label,output_file):
    output_file = open(f"{output_file}", "w")
    def cal_val(arr):
        sum = 0
        for i in range(len(values)):
            sum += values[i]*arr[i]
        return sum

    def cal_weights(arr):
        sum = 0
        for i in range(len(weights)):
            sum += weights[i]*arr[i]
        return sum

    global ans
    make_Binary_N(len(weights))
    pop_list = []
    for i in range(len(ans)):
        if  check_cap_class(capacity,num_of_class,weights,values,class_label,ans[i]) == False:
            pop_list.append(i)
    for i in range(len(pop_list)):
        ans.pop(pop_list[i] -i)
    max_Value = max(ans,key=cal_val)
    print(max_Value, cal_val(max_Value))
    output_file.write(f"{cal_val(max_Value)}\n")
    output_file.write(f"{max_Value}".replace('[', '').replace(']', '') + "\n")
    ans=[]
    output_file.close()    

def check_cap_class(capacity,num_of_class,weights,values,class_label,i):
    sum_weights = 0;
    arr_class = []
    for j in range(len(weights)):
        if i[j] == 1:
            sum_weights += weights[j]
            arr_class.append(class_label[j])
    if( sum_weights > capacity ) :
        return False
    else:
        for j in range(num_of_class):
            if j +1 not in arr_class:
                return False
    return True




def make_Binary_N( size):
    arr = [0 for _ in range(size)]
    BT(0,arr,size)

def BT(index,array,size):
    global ans
    for i in range(2):
        array[index] =i
        if index == size-1:
            other =[]
            for j in array:
                other.append(j)
            ans.append(other)

        else:
            BT(index+1,array,size)


if __name__ == "__main__":
    run( dataset="testcases/small_dataset/INPUT_1.txt",
                output_file="brute_force_search/output/small_dataset/OUTPUT_1.txt")
    run( dataset="testcases/small_dataset/INPUT_2.txt",
                output_file="brute_force_search/output/small_dataset/OUTPUT_2.txt")
    run( dataset="testcases/small_dataset/INPUT_3.txt",
                output_file="brute_force_search/output/small_dataset/OUTPUT_3.txt")
    run( dataset="testcases/small_dataset/INPUT_4.txt",
                output_file="brute_force_search/output/small_dataset/OUTPUT_4.txt")
    run( dataset="testcases/small_dataset/INPUT_5.txt",
                output_file="brute_force_search/output/small_dataset/OUTPUT_5.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brute_force_search/output/large_dataset/OUTPUT_1.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brute_force_search/output/large_dataset/OUTPUT_2.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brute_force_search/output/large_dataset/OUTPUT_3.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brute_force_search/output/large_dataset/OUTPUT_4.txt")
    run( dataset="testcases/large_dataset/INPUT_1.txt",
                output_file="brute_force_search/output/large_dataset/OUTPUT_5.txt")
