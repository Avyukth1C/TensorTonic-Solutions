def get_median(arr):
    n = len(arr)
    mid = (n - 1) // 2
    if n % 2 != 0:
        return float(arr[mid])
    else:
        return (arr[mid] + arr[mid + 1]) / 2

def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    length = len(values)
    if length == 1:
        return [0.0]

    sorted_values = sorted(values)
    mid = length // 2
    median = get_median(sorted_values)
    
    lower_half = sorted_values[:mid]
    upper_half = sorted_values[mid + (length % 2):]

    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    iqr = q3 - q1

    if iqr != 0:
        return [(v - median) / iqr for v in values]
    else:
        return [float(v - median) for v in values]