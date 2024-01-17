import random
import time
import datetime
from faker import Faker
import pandas as pd
import numpy as np

from enum import Enum

class FileAction(Enum):
    READ = 1 # most 
    RENAME = 2 # 2 sd away
    WRITE = 3 # 1 sd away
    DELETE = 4 # 1 sd away
    MOVE = 5 # 2 sd away

class UserTypeLabel(Enum):
    # NORMAL_ACTIVE = 1
    # NORMAL_PASSIVE = 2
    # ANOMALY_ACTIVE_SHORT_TERM = 3
    # ANOMALY_DORMANT_LONG_TERM = 4
    NORMAL = 1
    ANOMALY = 2


class SimulateUserActivity():
    ANOMALY_RATIO = 0.05
    DAYS_RANGE = 90
    DURATION = 10
    MAX_NUM_FILES_PER_USER_DAY = 1000
    MAX_ACTIONS_PER_USER = 10
    def __init__(self, num_user):
        self.num_user = num_user

    def generate_user_data(self):
        df = pd.DataFrame(columns=['timestamp', 'user_role', 'file_action'])
        # count=0
        for i in range(self.num_user):
            # sample the user type
            user_role = self.sample_user_role()
            # sample the start date of activity for active short term
            # start_date, end_date, num_days = self.sample_activity_start_end_time(user_type)
            for j in range(self.MAX_ACTIONS_PER_USER):
                row = []
                random_date = self.generate_time()
                file_action = self.sample_file_action()
                row.append(random_date)
                row.append(user_role)
                row.append(file_action)
                df = df.append(pd.DataFrame([row], columns=['timestamp', 'user_role', 'file_action']))
                # df.iloc[count] = row
                # count = count+1
        return df







            # for day in range(num_days):
            #     # current_date = start_date + day
            #     num_files = random.randint(0,self.MAX_NUM_FILES_PER_USER_DAY)
            #     for file in range(num_files):
            #         # sample the user file action
            #         file_action = random.choice([action.name for action in FileAction])
            #         # sample the file extension and entropy of the file
            #         # populate the user activity
            # pass

    def sample_file_action(self):
        # READ = 1 # most 
        # RENAME = 2 # 2 sd away
        # WRITE = 3 # 1 sd away
        # DELETE = 4 # 1 sd away
        # MOVE = 5 # 2 sd away
        integers = [1, 2, 3, 4, 5]
        probabilities = [0.4, 0.1, 0.3, 0.1, 0.1]
        generated_integer = random.choices(integers, probabilities)[0]
        return generated_integer



    def sample_user_role(self):
        if random.random() < 0.5:
            # admin
            user_role = "ADMIN"
        else:
            # user
            user_role = "USER"
        return user_role

    def generate_time(self):
        start_date = datetime.datetime(2022, 1, 1)
        end_date = datetime.datetime(2022, 3, 1)
        fake = Faker()
        random_datetime = fake.date_time_between(start_date, end_date)
        while random_datetime.hour < 9 or random_datetime.hour > 17 or random_datetime.weekday() in [5,6]:
            random_datetime = fake.date_time_between(start_date, end_date)
        return random_datetime


    # def sample_activity_start_end_time(self, user_type):
        # if user_type == UserType.ANOMALY_ACTIVE_SHORT_TERM or user_type == UserType.NORMAL_PASSIVE:
        #     start = int(random.random() * self.DAYS_RANGE)
        #     duration = int(random.random() * self.DURATION)
        #     start_date = datetime.timedelta(days=start)
        #     end_date = datetime.timedelta(days=start+duration)
        #     num_days = duration
        # else:
        #     start_date = datetime.timedelta(days=self.DAYS_RANGE)
        #     end_date = datetime.datetime.now()
        #     num_days = self.DAYS_RANGE

        # return start_date, end_date, num_days

    def sample_file_activity(self, start_date, end_date):
        # sample the user file action
        file_action = random.choice([action.name for action in FileAction])
        # sample the file extension and entropy of the file

    # def sample_user_type(self):
    #     if random.random() < self.ANOMALY_RATIO:
    #         if random.random() < 0.5:
    #             user_type = UserType.ANOMALY_ACTIVE_SHORT_TERM
    #         else:
    #             user_type = UserType.ANOMALY_DORMANT_LONG_TERM
    #     else:
    #         if random.random() < 0.5:
    #             user_type = UserType.NORMAL_ACTIVE
    #         else:
    #             user_type = UserType.NORMAL_PASSIVE
    #     return user_type

    # def populate_data_to_rds(self):
    #     # push the data to database
    #     pass

    # def build_user_anomaly_model(self):
    #     pass

    # def assess_detection_quality(self):
    #     # use the UserType as the ground truth
    #     # check of the top K anomalous detection, what proportion satisfied the condition
    #     pass

sim = SimulateUserActivity(5)
a = sim.generate_user_data()
print(a)








