from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel():
    
    @classmethod
    def get_usuarios(self):
        try:
            connection =  get_connection()
            usuarios =[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, age FROM usuarios ORDER BY name ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    usuario = Usuario(row[0],row[1],row[2])
                    usuarios.append(usuario.to_Json())
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_promedio(self):
        try:   
            connection =  get_connection()
            edad = 0
            n = 0

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, age FROM usuarios ORDER BY name ASC")
                resultset = cursor.fetchall()

            for row in resultset:
                edad = row[2] +edad
                #edad = int(resultset[0][2])+edad
                n = n + 1    
            edad = edad/n
            connection.close()
            return edad    
        except Exception as ex:
            raise Exception(ex)   

    @classmethod
    def add_usuario(self, usuario):
        try:   
            connection =  get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios (id,name,age)
                    VALUES(%s,%s,%s)""",(usuario.id,usuario.name,usuario.age))
                afected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return afected_rows    
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                print(id)
                cursor.execute("""UPDATE usuarios SET name = %s, age = %s
                    WHERE id = %s""", (usuario.name, usuario.age,usuario.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)