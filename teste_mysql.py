import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testdb"
)

mycursor = mydb.cursor()

"""
# INSERT

sql_formula = "insert into students(name, age) values(%s, %s)"  # fórmula sql que será executada (note que os '%s' serão
# substituídos pelas variáveis

students = [("Rachel", 22),
            ("Amanda", 32),
            ("Jacob", 21),
            ("Avi", 28),
            ("Michelle", 17),]

# mycursor.execute(sql_formula,student1)  # usado para executar apenas 1 linha
mycursor.executemany(sql_formula, students)  # usado para executar várias linhas
mydb.commit()  # usado para salvar as alterações na tabela
"""


"""
# SELECT

mycursor.execute("select * from students")
myresult = mycursor.fetchall()

for row in myresult:
  print(row)
"""
