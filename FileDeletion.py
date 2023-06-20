import math


# Count taken manually from Kaggle numbers of files _to_delete = Total_files - average_number
training_files_to_delete_A = 2193 # 2359 - 166
training_files_to_delete_L = 1106 # 1272 - 166

validation_files_to_delete_A = 274 #294 - 20
validation_files_to_delete_L = 139 #159 - 20

testing_files_to_delete_A = 275 #296-21
testing_files_to_delete_L = 139 #160-21

import os 
import random

def remove_files(folder_path, num_files, output_file):
    file_list = os.listdir(folder_path)
    files_to_remove = random.sample(file_list, num_files)
    
    with open(output_file, 'w') as f:
        for file_name in files_to_remove:
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
            f.write(f"File '{file_name}' removed from '{folder_path}'.\n")
    
    print(f"{num_files} files removed from '{folder_path}'.")
    print(f"Deleted file names saved to '{output_file}'.") 



remove_files('train/Allaple.A', training_files_to_delete_A, 'Training-Allaple.A-deletion.txt')
remove_files('train/Allaple.L', training_files_to_delete_L, 'Training-Allaple.L-deletion.txt')

remove_files('val/Allaple.A', validation_files_to_delete_A, 'Validation-Allaple.A-deletion.txt')
remove_files('val/Allaple.L', validation_files_to_delete_L, 'Validation-Allaple.L-deletion.txt')

remove_files('test/Allaple.A', testing_files_to_delete_A, 'Testing-Allaple.A-deletion.txt')
remove_files('test/Allaple.L', testing_files_to_delete_L, 'Testing-Allaple.L-deletion.txt')

