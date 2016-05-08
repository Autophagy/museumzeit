import datetime

# Countries

uk = Country(name='United Kingdom', flagURL='uk.png')

countries = [uk]

# Cities

london = City(name='London', timezone='Europe/London', country=uk)

# Types

museum = Type(name='Museum', iconURL='museum.png')
artGallery = Type(name='Art Gallery', iconURL='artGallery.png')

# Museums

# Messy way of going about it, but it'll suffice for now
loremDesc = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus.'

bm = Museum(name='British Museum', description=loremDesc, website='http://www.britishmuseum.org', latitude=51.5194, longitude=-0.1265, city=london, type=museum)
dm = Museum(name='Design Museum', description=loremDesc, website='https://designmuseum.org/', latitude=51.50261, longitude=-0.072006, city=london, type=museum)
dpg = Museum(name='Dulwich Picture Gallery', description=loremDesc, website='http://www.dulwichpicturegallery.org.uk/', latitude=51.44632, longitude=-0.085962, city=london, type=artGallery)
hm = Museum(name='Horniman Museum', description=loremDesc, website='http://www.horniman.ac.uk/', latitude=51.441034, longitude=-0.061013, city=london, type=museum)
iwm = Museum(name='Imperial War Museum', description=loremDesc, website='http://www.iwm.org.uk', latitude=51.495794, longitude=-0.108653, city=london, type=museum)
jml = Museum(name='Jewish Museum London', description=loremDesc, website='http://www.jewishmuseum.org.uk/', latitude=51.53734, longitude=-0.144584, city=london, type=museum)
ltm = Museum(name='London Transport Museum', description=loremDesc, website='http://www.ltmuseum.co.uk/', latitude=51.511926, longitude=-0.121429, city=london, type=museum)
mol = Museum(name='Museum of London', description=loremDesc, website='http://www.museumoflondon.org.uk/museum-london', latitude=51.517617, longitude=-0.096776, city=london, type=museum)
ng = Museum(name='National Gallery', description=loremDesc, website='https://www.nationalgallery.org.uk', latitude=51.5089, longitude=-0.1283, city=london, type=artGallery)
nmm = Museum(name='National Maritime Museum', description=loremDesc, website='http://www.rmg.co.uk/national-maritime-museum', latitude=51.480874, longitude=-0.005288, city=london, type=museum)
npg = Museum(name='National Portrait Gallery', description=loremDesc, website='http://www.npg.org.uk/', latitude=51.509425, longitude=-0.128124, city=london, type=artGallery)
nhm = Museum(name='Natural History Museum', description=loremDesc, website='http://www.nhm.ac.uk', latitude=51.4967, longitude=-0.1764, city=london, type=museum)
sm = Museum(name='Science Museum', description=loremDesc, website='http://www.sciencemuseum.org.uk', latitude=51.4978, longitude=-0.1745, city=london, type=museum)
tb = Museum(name='Tate Britain', description=loremDesc, website='http://www.tate.org.uk/visit/tate-britain', latitude=51.491063, longitude=-0.127788-0.1745, city=london, type=museum)
tm = Museum(name='Tate Modern', description=loremDesc, website='http://www.tate.org.uk/visit/tate-modern', latitude=51.507595, longitude=-0.127788, city=london, type=museum)
va = Museum(name='V&A', description=loremDesc, website='https://www.vam.ac.uk/', latitude=51.496639, longitude=-0.172181, city=london, type=museum)
wc = Museum(name='Wallace Collection', description=loremDesc, website='http://www.wallacecollection.org/', latitude=51.517462, longitude=-0.15297, city=london, type=artGallery)

# Periods

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 30, 0), free=True, museum=bm)
Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(20, 30, 0), weekday=4, free=True, museum=bm)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 45, 0), free=False, museum=dm)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 00, 0), free=False, museum=dpg)
Period(open=False, openTime=datetime.time(12,0,0), closedTime=datetime.time(12, 30, 0), weekday=0, free=False, museum=dpg)

Period(open=True, openTime=datetime.time(10,30,0), closedTime=datetime.time(17, 30, 0), free=True, museum=hm)

Period(open=True, openTime=datetime.time(10,00,0), closedTime=datetime.time(18, 00, 0), free=True, museum=iwm)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 00, 0), free=False, museum=jml)
Period(open=False, openTime=datetime.time(12,0,0), closedTime=datetime.time(12, 30, 0), weekday=4, free=False, museum=jml)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 00, 0), free=False, museum=ltm)
Period(open=True, openTime=datetime.time(11,0,0), closedTime=datetime.time(18, 00, 0), weekday=4, free=False, museum=ltm)

Period(open=True, openTime=datetime.time(10,00,0), closedTime=datetime.time(18, 00, 0), free=True, museum=mol)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 00, 0), free=True, museum=ng)
Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(21, 00, 0), weekday=4, free=True, museum=ng)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 00, 0), free=True, museum=nmm)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 00, 0), free=True, museum=npg)
Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(21, 00, 0), weekday=3, free=True, museum=npg)
Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(21, 00, 0), weekday=4, free=True, museum=npg)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 50, 0), free=True, museum=nhm)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 00, 0), free=True, museum=sm)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 00, 0), free=True, museum=tb)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(18, 00, 0), free=True, museum=tm)
Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(22, 00, 0), weekday=4, free=True, museum=tm)
Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(22, 00, 0), weekday=5, free=True, museum=tm)

Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 45, 0), free=True, museum=va)
Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(22, 00, 0), weekday=4, free=True, museum=va)

Period(open=True, openTime=datetime.time(10,00,0), closedTime=datetime.time(17, 00, 0), free=True, museum=wc)

db.session.add_all(countries)
db.session.commit()
