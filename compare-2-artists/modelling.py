def generate_class_weights(y):
    '''
    Get class weights to help manage slight class imbalance
    '''
    return dict(zip(list(np.unique(y)),
                    class_weight.compute_class_weight('balanced',
                     np.unique(y), y)))
