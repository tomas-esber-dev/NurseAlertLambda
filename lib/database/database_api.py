import mysql.connector;
import yaml

CONFIG_FILE = './lib/database/config.yml'
with open(CONFIG_FILE, 'r') as file:
    config = yaml.safe_load(file)

class DatabaseApi:
    def __init__(self):
        # Initialize the database connection
        self.db_connection = mysql.connector.connect(
            host=config["database"]["host"],
            user=config["database"]["user"],
            password=config["database"]["password"],
            database=config["database"]["name"]
        )
    def __del__(self):
        # Ensure the database connection is closed when the instance is destroyed
        self.db_connection.close()

    # get list of hospital info
    def get_hospitals(self):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute("SELECT * FROM {}".format(config["database"]["hospitalTable"]))
            results = cursor.fetchall()
        except Exception as e:
            # Handle exceptions
            print(e)
        finally:
            cursor.close()
            return results
    
    # get the rooms in a certain hospital
    def get_rooms_for_hospital(self, hospital_id):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute("SELECT * FROM {} WHERE hospital_id = {}".format(config["database"]["roomTable"], hospital_id))
            results = cursor.fetchall()
        except Exception as e:
            # Handle exceptions\
            print(e)
        finally:
            cursor.close()
            return results

    # get number of employees assigned to each room (set of room ids provided)
    # returns a dictionary of the room ids to the number of employees in that room
    def get_num_employees_per_room(self, hospital_id, room_ids):
        cursor = self.db_connection.cursor()
        dict = {}
        try:
            for room_id in room_ids:
                cursor.execute("SELECT COUNT(*) FROM {} WHERE room_id={} and hospital_id={}".format(config["database"]["assignmentTable"], room_id, hospital_id))
                numEmployees = cursor.fetchall()[0][0]
                dict[room_id] = numEmployees
        except Exception as e:
            # Handle exceptions\
            print(e)
        finally:
            cursor.close()
            return dict
    
    # get list of employees corresponding to ids provided
    def get_employees_by_ids(self, employee_ids):
        cursor = self.db_connection.cursor()
        try:
            ids = ', '.join(map(str, employee_ids))
            where_clause = "(" + ids + ")"
            cursor.execute("SELECT * FROM {} WHERE id IN {}".format(config["database"]["employeeTable"], where_clause))
            results = cursor.fetchall()
        except Exception as e:
            # Handle exceptions\
            print(e)
        finally:
            cursor.close()
            return results

    # get the ids of employees assigned to a certain room in a hospital 
    def get_employee_ids_in_room(self, hospital_id, room_id):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute("SELECT employee_id FROM {} WHERE room_id={} and hospital_id={}".format(config["database"]["assignmentTable"], room_id, hospital_id))
            results = cursor.fetchall()
            flat_list = [item for tup in results for item in tup]
        except Exception as e:
            # Handle exceptions\
            print(e)
        finally:
            cursor.close()
            return flat_list

