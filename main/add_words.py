from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, Word

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

words = ['11) their/them (их/им)', '12) his/him (его/ему)', '13) her (ее/ей)',
         '14) its/it (его, ее / ему, ей (о неодушевленном))', '15) a person/people (персона/человек)',
         '16) a man/men  (мужчина/мужчины)',
         '17) a woman/women (женщина/женщины)', '18) a child/children (ребенок/дети)',
         '19) a boy / boys (мальчик/мальчики)', '20) a girl/girls (девочка/девочки)']

for word in words:
    new_word = Word(word=word)
    session.add(new_word)

session.commit()