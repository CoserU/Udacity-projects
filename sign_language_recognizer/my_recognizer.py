import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses
    for i in range(test_set.num_items):
        X, lengths = test_set.get_item_Xlengths(i)
        logLs = {}
        guess = None
        best_score = float('-inf')
        for word, model in models.items():
            try:
                score_cur = model.score(X, lengths)
                logLs[word] = score_cur

                if score_cur > best_score:
                    guess = word
                    best_score = score_cur
            except:
                logLs[word] = float('-inf')
        probabilities.append(logLs)
        guesses.append(guess)
    return probabilities, guesses
