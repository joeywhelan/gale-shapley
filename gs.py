# Author Joey Whelan
""" Gale-Shapley algorithm implementation
"""
import random
import pprint



def generate_prefs(class1, class2):
    """ Random preferences generator.
            
        Parameters
        ----------
        class1, class2 :  lists of members for each class

        Returns
        -------
        Random list of preferences for member of the two classes
    """
    if len(class1) != len(class2):
        raise Exception("Invalid input: unequal list sizes")

    prefs = {}
    for item in class1:
        random.shuffle(class2)
        prefs[item] = class2.copy()
    
    for item in class2:
        random.shuffle(class1)
        prefs[item] = class1.copy()

    return dict(sorted(prefs.items()))

def gale_shapley(prefs, proposers):
    """ Random preferences generator.  Given the input objects are passed by ref, the function does have 
        the side effect of modifying those objects
            
        Parameters
        ----------
        prefs :  list preferences for each member of the two classes
        proposers:  list of the members of the class that will play the 'proposer' role

        Returns
        -------
        List of stable matches
    """
    matches = []
    while len(proposers) > 0:  #terminating condition - all proposers are matched
        proposer = proposers.pop(0)  #Each round - proposer is popped from the free list
        proposee = prefs[proposer].pop(0)  #Each round - the proposer's top preference is popped
        matchLen= len(matches)
        found = False
        
        for index in range(matchLen):  
            match = matches[index]
            if proposee in match:  #proposee is already matched
                found = True
                temp = match.copy()
                temp.remove(proposee)
                matchee = temp.pop()
                if prefs[proposee].index(proposer) < prefs[proposee].index(matchee):  #proposer is a higher preference 
                    matches.remove(match)  #remove old match
                    matches.append([proposer, proposee])  #create new match with proposer
                    proposers.append(matchee)  #add the previous proposer to the free list of proposers
                else:
                    proposers.append(proposer)  #proposer wasn't a higher prefence, so gets put back on free list
                break
            else:
                continue
        if not found:  #proposee was not previously matched so is automatically matched to proposer
            matches.append([proposer, proposee])
        else:
            continue
    return matches

class1 = ['a1', 'a2', 'a3']
class2 = ['b1', 'b2', 'b3']

prefs = generate_prefs(class1, class2)
print(f'\nPreferences')
pprint.pprint(prefs)
matches = gale_shapley(prefs, class1)
print(f'\nMatches\n{matches}')