import pandas as pd
from sqlalchemy import create_engine
import datetime
import pexpect
import os

DB = create_engine('mysql+pymysql://superset:superset@localhost/superset')
CSV_USER = '/home/samo/Desktop/superset/tired/students_data.json'
# CSV_PASSWORD = 'secrets/email_password.csv'
DOCKER_PATH = '/usr/local/bin'  # Useful for Mac


def main():
    create_missing_users()
    # reset_all_passwords()


def create_missing_users():
    """ Create users present in csv file but missing in Superset"""
    print("== Creating users from csv file, if they do not exist in Superset")
    # df_existing_users = pd.read_sql_table('ab_user', DB)
    # df_password_users = pd.read_csv(CSV_PASSWORD, sep=';')

    df_csv_users = pd.read_csv(CSV_USER, sep=';')
    df_csv_users['username'] = concat_username(df_csv_users['first_name'], df_csv_users['last_name'])
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df_csv_users['now'] = "TIMESTAMP '{}'".format(now)

    for user_row in df_csv_users.iterrows():
        user_dict = user_row[1].to_dict()

        # Skip existing users
        to_insert = True
        # for key in ['username', 'email']:
        #     if user_dict[key] in df_existing_users[key].values:
        #         print("{} {} already exists in Superset.".format(key, user_dict[key]))
        #         to_insert = False
        #         break

        # Insert others
        if to_insert:
            print("Creating user : {first_name}, {last_name}, {username}, {email}".format(**user_dict))
            query = """
            INSERT INTO ab_user (first_name, last_name, username, active, email, created_on, changed_on, created_by_fk, changed_by_fk, login_count, fail_login_count)
            VALUES ('{first_name}', '{last_name}', '{username}', 1, '{email}', {now}, {now}, 1, 1, 0, 0);
            """.format(**user_dict)
            connection = DB.connect()
            connection.execute(query)
            connection.close()

            password = get_corresponding_value(df_password_users, 'email', user_dict['email'], 'password')
            if password is None:
                print("No password defined for user with email '{email}'. You will have to reset it manually".format(**user_dict))
            # else:
                # print("Reset password of user '{username}' with email '{email}'".format(**user_dict))
                # reset_password(username=user_dict['username'], password=password)

def concat_username(first_name, last_name):
    return first_name + '.' + last_name

def get_corresponding_value(df, column_to_equal, value, column_to_get='id'):
    """ Get corresponding value in column_to_get, for column_to_equal == value
    
    Suppose that only one row match column_to_equal == value
    """
    ids = list(df[df[column_to_equal] == value][column_to_get])
    if ids:
        if len(ids) > 1:
            raise ValueError("Value {} is present multiple times in columns {}".format(value, column_to_equal))
        return ids[0]
    else:
        return None

if __name__ == "__main__":
    main()