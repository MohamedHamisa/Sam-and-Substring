def substrings(n):
    sub_prev_sum = int(n[0])
    prev_sum =  int(n[0])
    for i, curr_char in enumerate(n[1:]):
        new_sum = prev_sum+(sub_prev_sum*10)+((i+2)*int(curr_char))
        sub_prev_sum = new_sum-prev_sum
        prev_sum =  new_sum
    return prev_sum%(pow(10, 9)+7)
