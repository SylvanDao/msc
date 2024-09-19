def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
     # 6a. Print the number of NOT-dog images
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    print("{:20}: {:3d}".format('Correct Dog Images', results_stats_dic['n_correct_dogs']))
    # print("{:20}: {:3d}".format('Correct Not Dog Images', results_stats_dic['n_correct_notdogs']))
    print("{:20}: {:3d}".format('Correct Dog Breed', results_stats_dic['n_correct_breed']))

    # Prints summary statistics (percentages) on Model Run
    print(" ")
    for key in results_stats_dic:
        # 6b. Print all percentage statistics
        if key.startswith('pct'):
            print("{:20}: {:.2f}".format(key, results_stats_dic[key]))
    # # Print additional metrics
    # print("\n*** Additional Metrics ***")
    # if 'accuracy' in results_stats_dic:
    #     print("{:20}: {:.2f}".format('Accuracy', results_stats_dic['accuracy']))
    # if 'precision' in results_stats_dic:
    #     print("{:20}: {:.2f}".format('Precision', results_stats_dic['precision']))
    # if 'recall' in results_stats_dic:
    #     print("{:20}: {:.2f}".format('Recall', results_stats_dic['recall']))
    # if 'f1_score' in results_stats_dic:
    #     print("{:20}: {:.2f}".format('F1 Score', results_stats_dic['f1_score']))

    # IF print_incorrect_dogs is True AND there were images incorrectly 
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and 
        ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # process through results dict, printing incorrectly classified dogs
        for key in results_dic:
            # 6c. Print misclassified dogs
            if ((results_dic[key][3] == 1 and results_dic[key][4] == 0) or 
                (results_dic[key][3] == 0 and results_dic[key][4] == 1)):
                 print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))
    
    # IF print_incorrect_breed is True AND there were dogs whose breeds 
    # were incorrectly classified - print out these cases                    
    if (print_incorrect_dogs and 
        ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images'])):
        
        print("\nINCORRECT Dog Breed Assignment:")
        # process through results dict, printing incorrectly classified breeds
        for key in results_dic:
            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if (sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))
                
