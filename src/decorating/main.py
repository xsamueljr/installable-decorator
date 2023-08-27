def validate_types(*arg_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, arg_types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Argument {arg} must be of type {arg_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator