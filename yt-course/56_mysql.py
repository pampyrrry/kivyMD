# https://www.youtube.com/watch?v=uswyR2qwxzc&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=56

from kivy.lang import Builder
from kivymd.app import MDApp
#import sqlite3
import mysql.connector

class MainApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database Or Connect To One
        #connect = sqlite3.connect('first_db.db')

        #Define DB stuff
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = #"your password",
            database = "second_db"
        )

        # Create A Coursor
        #cursor = connect.cursor()
        cursor = mydb.cursor()

        # Creata an actual database
        cursor.execute("CREATE DATABASE IF NOT EXISTS second_db")

        # Chceck to see  if databse  was created
        #cursor.execute("SHOW DATABASES")
        #for db in cursor:
        #    print(db)

        # Create A Table
        cursor.execute("""CREATE TABLE if not exists customers (
        name VARCHAR(50)) """)

        #Check to see if table was created
        #cursor.execute("SELECT * FROM customers")
        #print (cursor.description)

        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()

        return Builder.load_file('56_mysql.kv')

    def submit(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd = #"your password",
            database="second_db"
        )
        # Create A Coursor
        cursor = mydb.cursor()

        # Add A Record
        sql_command = "INSERT INTO customers (name) VALUES (%s)"
        values = (self.root.ids.word_input.text,)

        # Execute SQL Command
        cursor.execute(sql_command, values)

        # Add a little message
        self.root.ids.word_label.text = f"{self.root.ids.word_input.text} was added"

        # Clear input field
        self.root.ids.word_input.text = ""

        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()

    def show_records(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd = #"your password",
            database="second_db"
        )

        # Create A Coursor
        # cursor = connect.cursor()

        cursor = mydb.cursor()

        # Show

        cursor.execute("SELECT * FROM customers")
        records = cursor.fetchall()

        word = ""
        # Loop
        for record in records:
            word = f"{word}\n{record[0]}"
            self.root.ids.word_label.text = f"{word}"
        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()

MainApp().run()
