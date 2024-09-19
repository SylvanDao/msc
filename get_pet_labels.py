# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
 
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
   
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for filename in in_files:
       
           # Creates temporary label variable to hold pet label name extracted 
           pet_label = " ".join([word.lower() for word in filename.split('_') if word.isalpha()])

           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           if filename not in results_dic:
              results_dic[filename] = [pet_label]
              
           else:
               print("** Warning: Duplicate files exist in directory:", filename)

    # Returns the results_dic dictionary that you created with this function
    return results_dic
    