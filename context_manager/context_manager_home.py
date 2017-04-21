class Mycontext(object):
    def __init__(self,file_name, flag, username):
        self.file_obj = open(file_name, flag)
        self.user = username


    def __enter__(self):
            self.file_obj.write("File was modified by " + user + '\n')
            return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
            self.file_obj.close()

f_write = 'for_write'
user = 'gtkachenko'
with Mycontext(f_write, 'a', user ) as f:
    f.write('Hi \n')
