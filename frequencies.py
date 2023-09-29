"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for i in range(len(items)):
        items[i] = str(items[i])

    for j in items:
        frequencies[j] = frequencies.get(j,0) + 1
        
    
    return frequencies
