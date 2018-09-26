"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(sys.argv[1]) as file:
        text = file.read()

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    chains = {}

    for i in range(len(words)-1):
        if i < (len(words) - chain_length):
            new_key = tuple(words[i:(i+chain_length)])
            chains[new_key] = chains.get(new_key, []) + [words[i+chain_length]]


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    key_list = list(chains)
    key = choice(key_list)
    value = choice(chains[key])

    while key in chains:

        value = choice(chains[key])
        link = " ".join(key) + " " + value
        words.append(link)
        print(link)
        key = key[1:] + (value,)
        print(key)
    

    return " ".join(words)


input_path = sys.argv[1]
chain_length = int(input("Input the number of words to use in your key: "))

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = print(make_text(chains))
