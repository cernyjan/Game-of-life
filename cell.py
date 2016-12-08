class Cell(object):
        def __init__(self, alive):
                self.set_life(alive)
                self.neighbors = 0
                
        def validate_type(self, var, varType):
                if isinstance(var, varType):
                        return True
                else:
                        return False
        
        def set_life(self, life):
                if self.validate_type(life, int):
                        self.alive = life
                else:
                      self.alive = False  

        def get_life(self):
                return self.alive

        def set_neighbors(self, neighbors):
                if isinstance(neighbors, int):
                        if neighbors >= 0:
                                self.neighbors = neighbors
                        else:
                                raise ValueError('Value has to be >= 0')
                else:
                        raise ValueError('Value has to be >= 0')

        def get_neighbors(self):
                return self.neighbors
                
