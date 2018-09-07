from datetime import datetime
from aws_connect.models import FileHandler
from aws_connect.utils import s3

def save_file(bucket, folder, file_name, file_data):
    today = datetime.now()

    file_name, file_type = file_name.split('.')
    timestamped_file_name = '{}_{}.{}'.format(file_name, today.strftime('%m_%d_%Y_%H_%M_%S'), file_type)
    
    s3.save_file(bucket, folder + timestamped_file_name, file_data)

    s3_file = FileHandler(
            file_name = timestamped_file_name,
            file_type = file_type,
            s3_bucket = bucket,
            s3_folder = folder,
            uploaded_at = today)
    
    return s3_file.save()