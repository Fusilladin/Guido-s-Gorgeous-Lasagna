EXPECTED_BAKE_TIME = 40
def bake_time_remaining(bake_time):
    """Shows the total bake time
    bake time = how long the lasagna has been cooking for
    """
    return EXPECTED_BAKE_TIME - bake_time
def preparation_time_in_minutes(number_of_layers, make_time=2 ):
    """Shows the entire length of time it will take to prepare this dish
    number_of_layers = how many layers the lasagna will have
    make_time = 2 because it takes 2 minutes to prepare a single layer of lasagna
    """
    return make_time * number_of_layers
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Shows the total amount of time that has been spent making this dish including preparation time.
    number_of_layers = how many layers the lasagna has and is multiplied by the amount of time each layer
    takes to make
    elapsed_bake_time = how long it has cooking
    """
    return (2*number_of_layers) + elapsed_bake_time
