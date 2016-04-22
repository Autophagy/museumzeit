import datetime

# Countries

germany = Country(name='Germany', flagURL='de.png')
uk = Country(name='United Kingdom', flagURL='uk.png')

countries = [germany, uk]

# Cities

berlin = City(name='Berlin', timezone='Europe/Berlin', country=germany)
london = City(name='London', timezone='Europe/London', country=uk)

cities = [berlin, london]

# Types

museum = Type(name='Museum', iconURL='museum.png')
artGallery = Type(name='Art Gallery', iconURL='artGallery.png')

types = [museum, artGallery]

# Museums

britishMuseum = Museum(name='The British Museum', description='Lorem Ipsum', longitude=-0.1265, latitude=51.5194, city=london, type=museum)
scienceMuseum = Museum(name='Science Museum', description='Lorem Ipsum', longitude=-0.1745, latitude=51.4978, city=london, type=museum)
nationalGallery = Museum(name='National Gallery', description='Lorem Ipsum', longitude=-0.1283, latitude=51.5089, city=london, type=artGallery)
naturalHistoryMuseum = Museum(name='Natural History Museum', description='Lorem Ipsum', longitude=-0.1764, latitude=51.4967, city=london, type=museum)

pergamonMuseum = Museum(name='Pergamon Museum', description='Lorem Ipsum', longitude=13.3974, latitude=52.5211, city=berlin, type=museum)

museums = [britishMuseum, scienceMuseum, nationalGallery, naturalHistoryMuseum, pergamonMuseum]

# Periods

bmPeriod = Period(openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 30, 0), free=True, museum=britishMuseum)
pmPeriod = Period(openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 30, 0), free=False, museum=pergamonMuseum)

periods = [bmPeriod, pmPeriod]

db.session.add_all(countries)
db.session.add_all(cities)
db.session.add_all(types)
db.session.add_all(museums)
db.session.add_all(periods)
db.session.commit()
