class User:
    def __init__(self,user_id,username):
        """
        Args:
            user_id (String): String ,Id 
            username (String): String , Name
        """
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0
        
    def follow(self,User):
        User.followers += 1
        self.following += 1
        
        


user_1 = User("001","Priyanshu Naredi")

user_admin  = User("000","Admin")

user_2 = User("002","aa")
user_2.followers = 44

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)

