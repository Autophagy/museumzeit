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

# Messy way of going about it, but it'll suffice for now
loremDesc = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus.'

britishMuseum = Museum(name='The British Museum', description=loremDesc, website="http://www.britishmuseum.org", latitude=51.5194, longitude=-0.1265, city=london, type=museum)
scienceMuseum = Museum(name='Science Museum', description=loremDesc, website="http://www.sciencemuseum.org.uk", latitude=51.4978, longitude=-0.1745, city=london, type=museum)
nationalGallery = Museum(name='National Gallery', description=loremDesc, website="https://www.nationalgallery.org.uk", latitude=51.5089, longitude=-0.1283, city=london, type=artGallery)
naturalHistoryMuseum = Museum(name='Natural History Museum', description=loremDesc, website="http://www.nhm.ac.uk", latitude=51.4967, longitude=-0.1764, city=london, type=museum)

pergamonMuseum = Museum(name='Pergamon Museum', description=loremDesc, website="http://www.smb.museum/museen-und-einrichtungen/pergamonmuseum/home.html", latitude=52.5211, longitude=13.3974, city=berlin, type=museum)

museums = [britishMuseum, scienceMuseum, nationalGallery, naturalHistoryMuseum, pergamonMuseum]

# Periods

bmPeriod = Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 30, 0), free=True, museum=britishMuseum)
smPeriod = Period(open=True, openTime=datetime.time(8,0,0), closedTime=datetime.time(20, 0, 0), free=False, museum=scienceMuseum)
ngPeriod = Period(open=True, openTime=datetime.time(9,30,0), closedTime=datetime.time(14, 30, 0), free=True, museum=nationalGallery)
nhmPeriod = Period(open=True, openTime=datetime.time(11,0,0), closedTime=datetime.time(19, 0, 0), free=True, museum=naturalHistoryMuseum)

pmPeriod = Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 30, 0), free=False, museum=pergamonMuseum)

periods = [bmPeriod, pmPeriod]

db.session.add_all(countries)
db.session.add_all(cities)
db.session.add_all(types)
db.session.add_all(museums)
db.session.add_all(periods)
db.session.commit()
