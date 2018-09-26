# TODO: takes a list of words, returns a dictionary mapping them to their vectors
def get_vectors(words):

    pass


def gender_direction(male_words, female_words, dictionary):
    # get the vectors for all the female words and male words
    # then, subtract all male from female (or all female from male)
    # save all those vectors to a set of vectors, and perform PCA on them
    her_vec = dictionary['she']
    he_vec = dictionary['he']
    new_vectors = []
    for i in range(100):
        new_dimension = her_vec[i] - he_vec
        new_vectors.append(new_dimension)
    # TODO: find PCA of the new vectors, take the first one, return it
    pass

def direct_bias(gender_direction,):
    # TODO: combine all elements of DirectBias statistic here
    pass

def main():
    word_to_vec_dict = {
        'she': [- 0.15525, 0.2895, 0.8429, -0.29431, 0.46418, - 0.08233, 0.33186, - 0.24247, - 0.47568, 0.15439,
                0.0026105, 0.20169, - 0.45813, - 0.088206, 0.32374, - 0.578, - 0.098162, - 0.057183, - 0.1891,
                - 0.018441, 0.52497, 0.17955, - 0.46307, 0.025253, 0.34856, 0.33119, - 0.087221, - 0.30248,
                - 0.071037, - 0.0016955, - 0.045113, - 0.34738, 0.043596, 0.11568, - 0.12196, - 0.020053,
                - 0.16266, - 0.10256, 0.27488, 0.4078, - 0.16358, 0.17791, 0.039274, - 0.030394, - 0.10268,
                - 0.051528, - 0.3732, - 0.14454, 0.11665, - 0.29964, 0.062405, - 0.045575, 0.10357, - 0.31, - 0.1365,
                0.12327, - 0.28107, 0.59528, 0.32677, 0.40369, - 0.041312, - 0.039232, - 0.51696, 0.020227, 0.33711,
                - 0.22344, 0.46815, - 0.38449, - 0.29527, 0.37244, - 0.034324, - 0.10385, 0.13054, - 0.047007,
                - 0.042703, - 0.36998, - 0.27287, 0.13901, 0.42516, - 0.081203, - 0.32371, - 0.17607, - 0.060554,
                0.03357, 0.28381, 0.043624, - 0.48022, - 0.31349, 0.23417, - 0.37702, 0.10811, 0.48112, - 0.068187,
                0.48216, - 0.041181, - 0.51345, - 0.063429, - 0.19725, - 0.12799, - 0.19352],

        'he': [- 0.1906, 0.4512,0.44799,0.073434,0.30254, - 0.10238,0.081755, - 0.14646 - 0.29934,0.1824, - 0.048731,
               0.23335, - 0.31721, - 0.12955,0.26512, - 0.47354,0.06438, - 0.085764, - 0.19598, - 0.20492, 0.43685,
               0.18893, - 0.31011, - 0.01425,0.43308,0.25495, - 0.14603, - 0.050958,0.10684, - 0.19127 ,- 0.066791 ,
               - 0.096637 ,- 0.19261 ,- 0.075819 ,- 0.15068,0.047335, - 0.15291, - 0.10966, 0.11853, 0.16899,0.061607,
               0.046249, - 0.099633, - 0.0361, - 0.079085, - 0.026234, - 0.030197,0.22743,0.054304, 0.057461, - 0.031113,
               0.12131, - 0.048866, - 0.046106, 0.066534,0.37198, - 0.38449,0.59631, - 0.083454, 0.13903,0.14272,
               - 0.10255, - 0.45912, - 0.0056143,0.23527 ,- 0.0034481, 0.37575, - 0.30211, - 0.34244,0.017378 ,- 0.02669,
               0.075334, - 0.029975, - 0.22502,0.003668 ,- 0.37263, - 0.15139, 0.37785, 0.15934, - 0.060076, - 0.16385,
               - 0.18882, - 0.0395,0.21919,0.43571, - 0.084233, - 0.1604, - 0.10842,0.29969 ,- 0.37247,0.07046, 0.29002,
               0.10951 ,- 0.0035761, - 0.27438 ,- 0.27606 ,- 0.011131, - 0.16639, 0.095491, - 0.00070512]

    }
    gender_direction(word_to_vec_dict)


if __name__ == '__main__':
    main()