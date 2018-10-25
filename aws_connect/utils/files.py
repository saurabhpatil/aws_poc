from datetime import datetime
from aws_connect.utils import s3

def save_file(bucket, folder, file_name, file_data):
    today = datetime.now()

    file_name, file_type = file_name.split('.')
    timestamped_file_name = '{}_{}.{}'.format(file_name, today.strftime('%m_%d_%Y_%H_%M_%S'), file_type)
    
    return s3.save_file(bucket, folder + timestamped_file_name, file_data)