import datetime

# Countries

germany = Country(name='Germany', flagURL='de.png')
uk = Country(name='United Kingdom', flagURL='uk.png')

# Cities

berlin = City(name='Berlin', timezone='Europe/Berlin', country=germany)
london = City(name='London', timezone='Europe/London', country=uk)

# Types

museum = Type(name='Museum', iconURL='museum.png')
artGallery = Type(name='Art Gallery', iconURL='artGallery.png')

# Museums

britishMuseum = Museum(name='The British Museum', description='Lorem Ipsum', longitude=-0.1265, latitude=51.5194, city=london, type=museum)
pergamonMuseum = Museum(name='Pergamon Museum', description='Lorem Ipsum', longitude=13.3974, latitude=52.5211, city=berlin, type=museum)

# Periods

bmPeriod = Period(openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 30, 0), free=True, museum=britishMuseum)
pmPeriod = Period(openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 30, 0), free=False, museum=pergamonMuseum)

db.session.add_all([germany, uk, berlin, london, museum, artGallery, britishMuseum, pergamonMuseum, bmPeriod, pmPeriod])
db.session.commit()
