from sqlalchemy import create_engine
from sqlalchemy.sql import text
import random
import string
import os

database_url = os.environ['DATABASE_URL'].replace("postgres://", "postgresql://")
engine = create_engine(database_url)

user_insert_sql = text("""INSERT INTO users(username, email, salt, bio, hashed_password) VALUES(:username, :email, :salt, :bio, :hashed_password)""")
select_last_user_id_sql = text("""SELECT ID FROM users ORDER BY id DESC LIMIT 1""")
item_insert_sql = text("""INSERT INTO items(slug, title, description, seller_id) VALUES(:slug, :title, :description, :seller_id)""")
select_last_item_id_sql = text("""SELECT ID FROM items ORDER BY id DESC LIMIT 1""")
comment_statement_sql = text("""INSERT INTO comments(body, seller_id, item_id) VALUES(:body, :seller_id, :item_id)""")

letters = string.ascii_lowercase

with engine.connect() as conn:
    for i in range(100):
      username = 'user-' + ''.join(random.choice(letters) for i in range(8))
      
      user = {'username': username, 'email':f'{username}@mail.com', 'salt': 'abc', 'bio': 'bio', 'hashed_password':username}
      print(user)
      conn.execute(user_insert_sql, **user)

      result = conn.execute(select_last_user_id_sql)
      row = result.first()
      generated_user_id = row['id']

      item = {'slug':f'slug-{username}', 'title':f'title{i}','description':f'desc{i}', 'seller_id':generated_user_id}
      conn.execute(item_insert_sql, **item)

      item_result = conn.execute(select_last_item_id_sql)
      row = item_result.first()
      generated_item_id = row['id']
      print(generated_item_id)
          
      comment = {'body': f'comment{i}', 'seller_id': generated_user_id, 'item_id': generated_item_id}
      conn.execute(comment_statement_sql, **comment)