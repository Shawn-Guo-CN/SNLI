from collections import OrderedDict
import Optimizers

options = OrderedDict(
    {
        'word_dim':100, # word embedding dimension
        'hidden_size':400,  # number of hidden units in single layer
        'patience':10,  # Number of epoch to wait before early stop if no progress
        'max_epochs':5000,  # The maximum number of epoch to run
        'dispFreq':10,  # Display to stdout the training progress every N updates
        'decay_c':0.,  # Weight decay for the classifier applied to the U weights.
        'lrate':0.0001,  # Learning rate for sgd (not used for adadelta and rmsprop)
        'n_words':37424,  # Vocabulary size
        'optimizer':Optimizers.adadelta,  # sgd, adadelta and rmsprop available, sgd very hard to use, not recommanded (probably need momentum and decaying learning rate).
        'encoder':'lstm',  # TODO: can be removed must be lstm.
        'saveto':'lstm_model.npz',  # The best model will be saved there
        'valid_freq':370,  # Compute the validation error after this number of update.
        'save_freq':1110,  # Save the parameters after every saveFreq updates
        'maxlen':100,  # Sequence longer then this get ignored
        'batch_size':16,  # The batch size during training.
        'valid_batch_size':64,  # The batch size used for validation/test set.
        'dataset':'imdb',
        ''# Parameter for extra option
        'noise_std':0.,
        'use_dropout':True,  # if False slightly faster, but worst test error
                             # This frequently need a bigger model.
        'reload_model':None,  # Path to a saved model we want to start from.
        'test_size':-1,  # If >0, we keep only this number of test example.
    }
)