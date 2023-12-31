def make_car(manufacturer, model, **kwargs):
    """Build a dictionary containing everything we know about a user."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car_profile = make_car('Honda', 'Civic', trim='Type-R', color='Gray', forced_induction='Turbo')

print(car_profile)