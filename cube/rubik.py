class Cube:

    def __init__(self, pieces=None):
        if not pieces:
            self.pieces = [
                    {
                        "edges" : [
                            ('g', 'w'), ('g','r'), ('g','y'), ('g','o')
                            ],
                        "corners" : [
                            ('g', 'w', 'r'), ('g','r','y'), ('g','y','o'), ('g','o','w')
                            ]
                        },
                    {
                        "edges" : [
                            ('w', 'r'), ('r','y'), ('y','o'), ('o','g')
                            ],
                        },
                    {
                        "edges" : [
                            ('b', 'w'), ('b','r'), ('b','y'), ('b','o')
                            ],
                        "corners" : [
                            ('b', 'w', 'r'), ('b','r','y'), ('b','y','o'), ('b','o','w')
                            ]
                        },
                    ]
        else:
            self.pieces = pieces

    def u(self, prime=False):
        pieces = self.pieces[:]
        edges = pieces[0]['edges']
        corners = pieces[0]['corners']
        if prime:
            pieces[0]['edges'] = [edges[1],edges[2],edges[3],edges[0]]
            pieces[0]['corners'] = [corners[1],corners[2],corners[3],corners[0]]
        else:
            pieces[0]['edges'] = [edges[3],edges[0],edges[1],edges[2]]
            pieces[0]['corners'] = [corners[3],corners[0],corners[1],corners[2]]
        return Cube(pieces)

    def u2(self):
        return self.u().u()

    def d(self, prime=False):
        pieces = self.pieces[:]
        edges = pieces[2]['edges']
        corners = pieces[2]['corners']
        if prime:
            pieces[2]['edges'] = [edges[3],edges[0],edges[1],edges[2]]
            pieces[2]['corners'] = [corners[3],corners[0],corners[1],corners[2]]
        else:
            pieces[2]['edges'] = [edges[1],edges[2],edges[3],edges[0]]
            pieces[2]['corners'] = [corners[1],corners[2],corners[3],corners[0]]
        return Cube(pieces)

    def d2(self):
        return self.d().d()

    def r(self, prime=False):

    def l(self, prime=False):
        pass
    def f(self, prime=False):
        pass
    def b(self, prime=False):
        pass

def main():
    cube = Cube()
    print(cube.d2().pieces)

if __name__ == '__main__':
    main()
