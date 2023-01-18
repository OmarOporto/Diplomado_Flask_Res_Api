class Usuario():

    def __init__(self, id, name=None, age=None) -> None:
        self.id = id
        self.name = name
        self.age = age

    def to_Json(self):
        return {
            'id':self.id,
            'Name':self.name,
            'Age':self.age
        }