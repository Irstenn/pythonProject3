class Family:
    def __init__(self, user_name, email, password, job_title):
        self.name = user_name
        self.email = email
        self.password = password
        self.job_title = job_title

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def change_password(self, new_password):
        self.password = new_password

    def get_user_infos(self):
        print(f'user {self.name} is woking as a {self.job_title}. You can contact him by {self.email}')


