from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.id import ID
from appwrite.query import Query
from names_generator import generate_name
import random


client = Client()
client.set_endpoint('https://fra.cloud.appwrite.io/v1')
client.set_project('just-a-game')
client.set_key('standard_0c4f19e43f31930ef9768e31c3cb460ee33cfdefe4f165209cdd9eabf07da8a6a230ccefdf9c4668f7cf73800d333cc02ac76ce1550dc9ae8fd2c80357a594223745160eb87107d5bd592fabd1c57c1952231135f7f1acc27d2c0bd9a93c0befba6f007272e50f880238b51d73b77550ac15ef5c2fc2edf1186c30e8420c7634')

tablesDB = TablesDB(client)


scoreDatabase = None
scoreTable = None




def prepare_database():
  global scoreDatabase
  global scoreTable

  scoreDatabase = tablesDB.get(database_id='695ff9080035072e95c4')

  scoreTable = tablesDB.get_table(database_id='695ff9080035072e95c4', table_id='scores')


def create_score(new_score):
  
  tablesDB.create_row(
    database_id=scoreDatabase['$id'],
    table_id=scoreTable['$id'],
    row_id=ID.unique(),
    data=new_score
  )






if __name__ == "__main__":
  prepare_database()



def add_test_scores(count=10):

  for i in range(count):
    testScore = {
      'Name': f"{generate_name(seed=random.randint(0, 9999))}{random.randint(0, 9999)}",
      'Score': random.randint(0, 9999)
    }
    tablesDB.create_score(data=testScore)


def get_scores():

  scores = tablesDB.list_rows(
    database_id=scoreDatabase['$id'],
    table_id=scoreTable['$id'],
    queries=[
      Query.order_desc("Score")
    ])
  return scores


def get_top_scores(limit):

  scores = tablesDB.list_rows(
    database_id=scoreDatabase['$id'],
    table_id=scoreTable['$id'],
    queries=[
      Query.order_desc("Score"),
      Query.limit(limit)
      ])
  return scores
  

if __name__ == "__main__":
  scores = get_top_scores()

print("\nScores:\n\n\n")
for score in scores['rows']:
  print(f"{score['Name']}: {score['Score']}\n")

