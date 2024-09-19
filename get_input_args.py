import argparse

def get_input_args():
    
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type=str, default='pet_images', help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='text file that contains dognames')
    
    return parser.parse_args()