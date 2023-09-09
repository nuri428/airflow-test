
def get_sftp():
    print("sfpt")
    return

def regist(name, sex, *args):
    print(f"이름:{name}")
    print(f"성별:{sex}")
    print(f"기타옵션들:{args}")

def regists(name, sex, *args, **kwargs):
    print(f"이름:{name}")
    print(f"성별:{sex}")
    print(f"기타옵션들:{args}")    
    print(f"기타옵션들2:{kwargs}")    
    email = kwargs.get('email', None)
    car = kwargs.get("car", None)
    if  email:
        print(f"email:{email}")
    if car:
        print(f"car:{car}")