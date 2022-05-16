from random import choice

ghost_types = {
    'Banshee':	{'evidence': ['D.O.T.S Projector', 'Ghost Orb', 'Fingerprints'], 'aggresion': 5, 'sadness': 0},
    'Demon': {'evidence': ['Ghost Writing', 'Fingerprints', 'Freezing Temperatures'], 'aggresion': 10, 'sadness': 0},
    'Goryo': {'evidence': ['D.O.T.S Projector', 'EMF Level 5', 'Fingerprints'], 'aggresion': 0, 'sadness': 10},
    'Hantu': {'evidence': ['Ghost Orb', 'Fingerprints', 'Freezing Temperatures'], 'aggresion': 5, 'sadness': 5},
}

names = {
    'male': ['John', 'Paul', 'George', 'Ringo'],
    'female': ['Katie', 'Regina', 'Karen', 'Gretchen']
}

def ghost_generator():
    type = choice(list(ghost_types))
    gender = choice(['male', 'female'])
    return ghost(type = type,
                 gender = gender,
                 name = choice(names[gender]),
                 age = choice(range(100)),
                 evidence = ghost_types[type]['evidence'],
                 aggresion = ghost_types[type]['aggresion'],
                 sadness = ghost_types[type]['sadness'])

class ghost:
    def __init__(self,
                 type = 'demon',
                 gender = 'male',
                 name = 'John',
                 age = 69,
                 evidence = ['Ghost Writing', 'Fingerprints', 'Freezing Temperatures'],
                 aggresion = 0,
                 sadness = 0):
        self.type = type
        self.gender = gender
        self.name = name
        self.age = age
        self.evidence = evidence
        self.aggresion = aggresion
        self.sadness = sadness

if __name__ == '__main__':
    ghost = ghost_generator()
    print('type:', ghost.type)
    print('name:', ghost.name)
    print('evidence:', ghost.evidence)