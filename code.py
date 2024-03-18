import psycopg2
from psycopg2 import Error

# Function to establish a connection to the PostgreSQL database
def create_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="7741",
            host="localhost",
            port="5433",
            database="University"
        )
        return connection
    except Error as e:
        print("Error while connecting to PostgreSQL", e)
        return None

# Function to retrieve and display all records from the students table
def get_all_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            print(student)
    except Error as e:
        print("Error while fetching data from PostgreSQL", e)

# Function to insert a new student record into the students table
def add_student(connection, first_name, last_name, email, enrollment_date):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, enrollment_date))
        connection.commit()
        print("Student added successfully")
    except Error as e:
        print("Error while adding student to PostgreSQL", e)

# Function to update the email address for a student with the specified student_id
def update_student_email(connection, student_id, new_email):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        connection.commit()
        print("Email updated successfully")
    except Error as e:
        print("Error while updating email in PostgreSQL", e)

# Function to delete the record of the student with the specified student_id
def delete_student(connection, student_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        connection.commit()
        print("Student deleted successfully")
    except Error as e:
        print("Error while deleting student from PostgreSQL", e)

# Main function
def main():
    connection = create_connection()
    if connection:
        # Perform operations
        # Display all the students in the University
        print("All the students in this University: ")
        get_all_students(connection)

         # Add a student to the school
        print("\n Adding student Simran to the university:")
        add_student(connection, 'Simran', 'Datta', 'simran@carleton.ca', '2024-03-18')
        print("\n All the students in this university after adding Simran: ")
        get_all_students(connection)

        #  # Update the email for student with student_id 1
        print("\n Updating the email for student with student_id 1")
        update_student_email(connection, 1, 'john.new@example.com')
        print("\n All the students in this university after updating the email for student with student_id 1: ")
        get_all_students(connection)

        # # Delete the student with student_id 3
        print("\n Deleting the student with student_id 3")
        delete_student(connection, 3)
        print("\n All the students in this univeristy after deleting the student with student_id 3: ")
        get_all_students(connection)

       

        # Close connection
        connection.close()
    else:
        print("Connection to database failed.")

if __name__ == "__main__":
    main()