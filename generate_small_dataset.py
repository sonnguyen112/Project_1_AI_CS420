import random

def check_valid_class_label(class_label, num_of_class):
    for i in range(num_of_class):
        if str(i + 1) not in class_label:
            return False
    return True

def generate(num_of_testcase):

    for i in range(num_of_testcase):
        f = open(f"testcases/small_dataset/INPUT_{i + 1}.txt", "w")
        capacity = random.randint(1000, 2000)
        f.write(f"{capacity}\n")
        num_of_class = random.randint(2, 4)
        f.write(f"{num_of_class}\n")

        num_of_item = random.randint(10, 40)
        weights = [str(random.randint(1, capacity//num_of_class)) for _ in range(num_of_item)]
        values = [str(random.randint(1, 500)) for _ in range(num_of_item)]

        while 1:
            class_label = [str(random.randint(1, num_of_class)) for _ in range(num_of_item)]
            
            if check_valid_class_label(class_label, num_of_class):
                break

        f.write(f"{','.join(weights)}\n")
        f.write(f"{','.join(values)}\n")
        f.write(f"{','.join(class_label)}\n")
        f.close()

if __name__ == "__main__":
    generate(5)