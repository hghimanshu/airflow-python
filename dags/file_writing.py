def filewriting(ds, *args):
    # ds = 3
    file_path = "/home/himanshu/Himanshu/apache-airflow/queues/" + str(ds) + '.txt'
    with open(file_path, 'w') as f:
        print("Now here")
        f.write("Hello file")
        return ds
