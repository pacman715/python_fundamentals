# Password generator
import random

# Traditional password
lc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']      
char = ['!','@','#','$','%','^','&','*','(',')','?']
num = ['1','2','3','4','5','6','7','8','9','0']




#XKCD Model
# nouns, verbs, & adjs are lists of words to choose from
nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 'isolation', 'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 'spread', 'shot', 'direction', 'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass', 'dot', 'final', 'chair', 'picture', 'wish', 'transfer', 'profession', 'suggestion', 'purse', 'rabbit', 'disaster', 'evil', 'shorts', 'tip', 'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition', 'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice', 'border', 'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 'puzzle', 'poll', 'wind', 'shelter', 'limit', 'talent']
verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 'complain', 'offer', 'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude', 'transform', 'add', 'boast', 'gather', 'manage', 'escape', 'handle', 'transfer', 'tune', 'born', 'decrease', 'impose', 'adopt', 'suppose', 'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep', 'invest', 'weaken', 'speed', 'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate', 'advise', 'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back', 'waste', 'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 'expensive', 'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud', 'key', 'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK', 'gray', 'little', 'religious', 'municipal', 'just', 'psychological', 'essential', 'perfect', 'intense', 'blue', 'following', 'Asian', 'shared', 'rare', 'developmental', 'uncomfortable', 'interesting', 'environmental', 'amazing', 'unhappy', 'horrible', 'philosophical', 'American']

# Concatonate the 4 randomly chosen words
pwd = random.choice(adjs) + random.choice(nouns) + random.choice(verbs) + random.choice(nouns)
print (pwd)
