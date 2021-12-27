import password as password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from login_functions import validators
from Model import User
import hashlib
# import bcrypt


def return_session():
    USER = 'root'
    PASSWORD = ''
    HOST = 'localhost'
    BD = 'sistemaLogin'
    PORT = '3306'

    URL_CONNECTION = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{BD}'

    ENGINE = create_engine(URL_CONNECTION, echo=True)
    Session = sessionmaker(bind=ENGINE)
    return Session()

class Cadastrar_controller:

    @classmethod
    def validate_data(cls, nome, email, senha):
        valid = validators.Validator()
        validate_email = valid.email_with_regex(email)
        if not validate_email:
            return 2

        validate_senha = valid.password_with_regex(senha)
        if not validate_senha:
            return 3

        if len(nome) > 50 or len(nome) < 3:
            return 4

        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = return_session()
        user = session.query(User).filter(User.email == email).all()

        if len(user) > 0:
            return 5

        data_validate = cls.validate_data(nome, email, senha)

        if data_validate != 1:
            return data_validate

        try:
            hashed_password = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            print(f'password: {password}')
            # hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            print(f"Hashed password: {hashed_password}")
            p1 = User(name=nome, email=email, password=hashed_password)
            session.add(p1)
            session.commit()
            return 1
        except Exception as e:
            print(e)

class Login_controller:
    @classmethod
    def login(cls, email, senha):
        session = return_session()
        senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        user = session.query(User).filter(User.email == email).filter( User.password == senha).all()
        print(f'username: {user}')
        if len(user) == 1:
            print("if")
            return {'authenticated':True, 'user': user[0].name}
        else:
            print("else")
            return False


    # def login(cls, email, senha, ):
    #     session = return_session()
    #     user = session.query(User).filter(User.email == email).one()
    #     hashed_password = user.password
    #     encoded_password  = senha.encode("utf-8")
    #     print(encoded_password)
    #     print(hashed_password)
    #     hashed_2 = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    #     print(hashed_2)
    #     if bcrypt.checkpw(encoded_password, hashed_2):
    #         print("You are loged in")




a = Cadastrar_controller()
a.cadastrar(nome="Jeferson Peter",
            email="jefersonpeter32@gmail.com",
            senha="LUCID@air201922")
b = Login_controller()
b.login("jefersonpeter32@gmail.com","LUCID@air201922")












