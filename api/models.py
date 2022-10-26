from django.db import models
users=[

    {"id":1,"username":"akhil","email":"akhil@gmail.com","password":"password@123","following":[2,3],"followers":[1,4]},
    {"id": 2, "username": "asha", "email": "asha@gmail.com", "password": "password@123", "following": [1,2, 3],"followers": [1, 4,6]},
    {"id": 3, "username": "vignesh", "email": "vignesh@gmail.com", "password": "password@123", "following": [2, 3,4,6],"followers": [1, 4]},
    {"id": 4, "username": "tijo", "email": "tijo@gmail.com", "password": "password@123", "following": [1, 3,5],"followers": [1, 4,8]},
    {"id": 5, "username": "salu", "email": "salu@gmail.com", "password": "password@123", "following": [1,2, 3],"followers": [1, 5]}
]

blogs=[
    {"postId": 1, "userId": 1,"title":"hey good morning","content": "content","liked_by":[1,2]},
    {"postId": 2, "userId": 1, "title": "good morning", "content": "content", "liked_by": [2,3]},
    {"postId": 3, "userId": 4, "title": "whatsup?", "content": "content", "liked_by": [1, 4]},
    {"postId": 4, "userId": 1, "title": "have a nice day", "content": "content", "liked_by": [2, 5]},
    {"postId": 5, "userId": 3, "title": "happy holiday", "content": "content", "liked_by": [1, 2]},

]