def calculates_results_stats(results_dic):
    
    # Creats empty dictionary for results_stats_dic
    results_stats_dic = dict()
    
    # Sets all counters to initial values of zero so that they can 
    # be incremented while processing through the images in results_dic 
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0       

     # Process through the results dictionary
    for key in results_dic:
        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
           
        # Pet Image Label is a Dog AND Labels match - counts Correct Breed
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1
        
        # Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

            # Classifier classifies image as Dog (& pet image is a dog)
            # Counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
            #     results_stats_dic['tp'] += 1  # True Positive
            # else:
            #     results_stats_dic['fn'] += 1  # False Negative
        else:
            # Pet Image Label is NOT a Dog
            # Counts number of correct NOT dog classifications.
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
            #     results_stats_dic['tn'] += 1  # True Negative
            # else:
            #     results_stats_dic['fp'] += 1  # False Positive


    # Calculates run statistics (counts & percentages) below that are calculated
    # using the counters from above.
    
    # calculates number of total images
    results_stats_dic['n_images'] = len(results_dic)

    # calculates number of not-a-dog images using - images & dog images counts
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                      results_stats_dic['n_dogs_img']) 
     
    # Calculates % correct for matches
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0

    # Calculates % correct dogs
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0

    # Calculates % correct breed of dog
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_breed'] = 0.0

    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted 
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_img']) *100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    # # Accuracy
    # total = results_stats_dic['tp'] + results_stats_dic['fp'] + results_stats_dic['tn'] + results_stats_dic['fn']
    # if total > 0:
    #     results_stats_dic['accuracy'] = ((results_stats_dic['tp'] + results_stats_dic['tn']) / total) * 100.0
    # else:
    #     results_stats_dic['accuracy'] = 0.0

    # # Precision
    # if (results_stats_dic['tp'] + results_stats_dic['fp']) > 0:
    #     results_stats_dic['precision'] = (results_stats_dic['tp'] / (results_stats_dic['tp'] + results_stats_dic['fp'])) * 100.0
    # else:
    #     results_stats_dic['precision'] = 0.0

    # # Recall
    # if (results_stats_dic['tp'] + results_stats_dic['fn']) > 0:
    #     results_stats_dic['recall'] = (results_stats_dic['tp'] / (results_stats_dic['tp'] + results_stats_dic['fn'])) * 100.0
    # else:
    #     results_stats_dic['recall'] = 0.0

    # # F1 Score
    # if (results_stats_dic['precision'] + results_stats_dic['recall']) > 0:
    #     results_stats_dic['f1_score'] = (2 * results_stats_dic['precision'] * results_stats_dic['recall']) / \
    #                                     (results_stats_dic['precision'] + results_stats_dic['recall'])
    # else:
    #     results_stats_dic['f1_score'] = 0.0
    # Print debug information
    
    return results_stats_dic