import hangman_helper


def update_word_pattern(word, pattern, letter):
    """Returns an updated word pattern after being matched to a letter.

    Parameters:
        word (str): the word to be guessed in hangman.
        pattern (str): the current pattern.
        letter (str): the guessed letter to be matched vs word.

    Returns:
        quadratic_equation(a, b, c): a tuple in length two that holds the solution.

    Example:
        update_word_pattern("apple", "___l_", "p") will return "_ppl_"
    """
    pattern_list = list(pattern)

    for i in range(len(word)):
        if word[i] == letter:
            pattern_list[i] = word[i]

    updated_pattern = "".join(pattern_list)

    return updated_pattern


help(update_word_pattern)
