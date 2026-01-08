from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.id import ID

client = Client()
client.set_endpoint('https://fra.cloud.appwrite.io/v1')
client.set_project('just-a-game')
client.set_key('standard_0c4f19e43f31930ef9768e31c3cb460ee33cfdefe4f165209cdd9eabf07da8a6a230ccefdf9c4668f7cf73800d333cc02ac76ce1550dc9ae8fd2c80357a594223745160eb87107d5bd592fabd1c57c1952231135f7f1acc27d2c0bd9a93c0befba6f007272e50f880238b51d73b77550ac15ef5c2fc2edf1186c30e8420c7634')


tablesDB = TablesDB(client)

todoDatabase = None
todoTable = None

def prepare_database():
  global todoDatabase
  global todoTable

  # todoDatabase = tablesDB.create(
  #   database_id=ID.unique(),
  #   name='TodosDB'
  # )
  todoDatabase = tablesDB.get(database_id='695ff9080035072e95c4')

  # todoTable = tablesDB.create_table(
  #   database_id=todoDatabase['$id'],
  #   table_id=ID.unique(),
  #   name='Todos'
  # )

  todoTable = tablesDB.get_table(database_id='695ff9080035072e95c4', table_id='scores')

  # tablesDB.create_string_column(
  #   database_id=todoDatabase['$id'],
  #   table_id=todoTable['$id'],
  #   key='title',
  #   size=255,
  #   required=True
  # )

  # tablesDB.create_string_column(
  #   database_id=todoDatabase['$id'],
  #   table_id=todoTable['$id'],
  #   key='description',
  #   size=255,
  #   required=False,
  #   default='This is a test description.'
  # )

  # tablesDB.create_boolean_column(
  #   database_id=todoDatabase['$id'],
  #   table_id=todoTable['$id'],
  #   key='isComplete',
  #   required=True
  # )





def seed_database():
  testTodo1 = {
    'title': "Buy apples",
    'description': "At least 2KGs",
    'isComplete': True
  }

  testTodo2 = {
    'title': "Wash the apples",
    'isComplete': True
  }

  testTodo3 = {
    'title': "Cut the apples",
    'description': "Don\'t forget to pack them in a box",
    'isComplete': False
  }

  tablesDB.create_row(
    database_id=todoDatabase['$id'],
    table_id=todoTable['$id'],
    row_id=ID.unique(),
    data=testTodo1
  )

  tablesDB.create_row(
    database_id=todoDatabase['$id'],
    table_id=todoTable['$id'],
    row_id=ID.unique(),
    data=testTodo2
  )

  tablesDB.create_row(
    database_id=todoDatabase['$id'],
    table_id=todoTable['$id'],
    row_id=ID.unique(),
    data=testTodo3
  )



print("Seeding database with test todos...")



from appwrite.query import Query

def get_todos():
  # Retrieve rows (default limit is 25)
  todos = tablesDB.list_rows(
    database_id=todoDatabase['$id'],
    table_id=todoTable['$id']
  )
  print("Todos:")
  for todo in todos['rows']:
    print(f"Name: {todo['Name']}\nScore: {todo['Score']}\n\n")

def get_completed_todos():
  # Use queries to filter completed todos with pagination
  todos = tablesDB.list_rows(
    database_id=todoDatabase['$id'],
    table_id=todoTable['$id'],
    queries=[
      Query.equal("isComplete", True),
      Query.order_desc("$createdAt"),
      Query.limit(5)
    ]
  )
  print("Completed todos (limited to 5):")
  for todo in todos['rows']:
    print(f"\nDescription: {todo['description']}\nIs Todo Complete: {todo['isComplete']}\n\n")

def get_incomplete_todos():
  # Query for incomplete todos
  todos = tablesDB.list_rows(
    database_id=todoDatabase['$id'],
    table_id=todoTable['$id'],
    queries=[
      Query.equal("isComplete", False),
      Query.order_asc("title")
    ]
  )
  print("Incomplete todos (ordered by title):")
  for todo in todos['rows']:
    print(f"Title: {todo['title']}\nDescription: {todo['description']}\nIs Todo Complete: {todo['isComplete']}\n\n")

if __name__ == "__main__":
  prepare_database()
  # seed_database()
  get_todos()
  # get_completed_todos()
  # get_incomplete_todos()




