import os
# Imports classifier function for using CNN to classify images 
from classifier import classifier 


def classify_images(images_dir, results_dic, model):
    
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in list(results_dic.keys()):       
              
       #  Runs classifier function to classify the images classifier function 
       # inputs: path + filename  and  model, returns model_label 
       # as classifier label
        model_label = classifier(os.path.join(images_dir, key), model)
       
       # Processes the results so they can be compared with pet image labels
       # set labels to lowercase (lower) and stripping off whitespace(strip)
        model_label = model_label.lower().strip()
              
       # defines truth as pet image label 
        truth = results_dic[key][0]

       # If the pet image label is found within the classifier label list of terms 
       # as an exact match to on of the terms in the list - then they are added to 
       # results_dic as an exact match(1) using extend list function
        if truth in model_label:
           results_dic[key].extend([model_label, 1])

        else:
       # if not found then added to results dictionary as NOT a match(0) using
       # the extend function 
            results_dic[key].extend([model_label, 0])