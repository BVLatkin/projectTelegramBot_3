from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, Word

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

words = ['1) I (я)', '2) you (ты, вы)', '3) we (мы)', '4) they (они)', '5) he (он)', '6) she (она)',
         '7) it (оно (о неодушевленном в единственном числе))', '8) my/me (мой/мне)',
         '9) your/you (твой, ваш / тебе, вам)', '10) our/us (наш/нам)']

for word in words:
    new_word = Word(word=word)
    session.add(new_word)

session.commit()