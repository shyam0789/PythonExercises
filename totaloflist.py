shyam_list = [5,1,5,3,2,3,4]
mowni_list = [4,2,3,2,1,3,4]

def total_list(list):
    total = 0
    for i in list:
        total+=i
    return total

print(f"Total of Shyam is : {total_list(shyam_list)}")
print(f"Total of Mowni is : {total_list(mowni_list)}")
