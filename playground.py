# Hi Toni!
# Let's do some coding!

import json
import random

with open('spells.json', 'rb') as file:
    spells = json.load(file)


# print(spells["Magic Missile"]["description"])

spellDescriptionDictionary = {}

for spell in spells:
    spell_Description = spells[spell]["description"]
    spellDescriptionDictionary[spell] = spell_Description


nextWordDictionary = {}

for spell in spellDescriptionDictionary:
    spellDescription = spellDescriptionDictionary[spell]
    spellDescWordArray = spellDescription.split(' ')
    spellDescWordArray.append("end_of_spell")
    spellDescWordArray.insert(0, "start_of_spell")

    for i, word in enumerate(spellDescWordArray):

        if word != "end_of_spell":
            nextWord = spellDescWordArray[i+1]
            if word not in nextWordDictionary:
                nextWordDictionary[word] = []
            nextWordDictionary[word].append(nextWord)



def MakeUpSpellDescription(maxSentences=1):            # We decide that default number of maximum sentences is one

    currentNumberOfSentencesGenerated = 0

    myCrazySpell = ''
    currentWord = random.choice(nextWordDictionary["start_of_spell"])
    myCrazySpell += currentWord + ' '

    while currentWord != "end_of_spell":
        nextWord = random.choice(nextWordDictionary[currentWord])

        if '.' in currentWord or '(' in currentWord or ')' in currentWord:
            if(currentNumberOfSentencesGenerated < maxSentences-1):
                currentNumberOfSentencesGenerated += 1
            else:
                nextWord = "end_of_spell"

        if nextWord != "end_of_spell":
            myCrazySpell += nextWord + ' '

        currentWord = nextWord


    return myCrazySpell

print(MakeUpSpellDescription(2))
