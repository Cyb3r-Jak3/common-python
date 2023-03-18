
def str2bool(v: str) -> bool:
    """str2bool Converts strings to booleans

    Function to convert strings to booleans.
    Any of `yes`, `y`, `true`, `t`, `1` return as true

    :param v: String to convert
    :type v: str
    :return: if converted
    :rtype: bool
    """
    return v.lower() in {"yes", "y", "true", "t", "1"}
