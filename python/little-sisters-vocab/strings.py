"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """
    return "un" + word

# print(add_prefix_un("hello"))


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.

    """
    #get prefix as index 0
    prefix = vocab_words[0]
    separator = ' :: ' +  prefix

    #add the dots seperator and join prefix to other words
    seperated_prefixed_words = separator.join(vocab_words)
    return seperated_prefixed_words



def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """

    #remove ness from word

    word_without_ness = word.replace("ness", "")

    #if word ends with i then change to Y
    if word_without_ness[-1] == "i":
        word_cleaned_out = word_without_ness[:-1] + "y"
        return word_cleaned_out
    return word_without_ness


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """

    adjective = sentence.split()[index]
    no_points_adj = adjective.strip(".")
    adjective_verbified = no_points_adj + "en"

    return adjective_verbified

print(adjective_to_verb('The ink stains her fingers black.', -1))
