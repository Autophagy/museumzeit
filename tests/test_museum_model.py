import unittest
from flask import current_app
from app import create_app, db
from app.models import Country, City, Type, Museum, Period
import datetime

class MuseumModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        uk = Country(name='United Kingdom', flagURL='uk.png')
        london = City(name='London', timezone='Europe/London', country=uk)
        museum = Type(name='Museum', iconURL='museum.png')
        artGallery = Type(name='Art Gallery', iconURL='artGallery.png')
        loremDesc = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus.'
        bm = Museum(name='British Museum', description=loremDesc, website='http://www.britishmuseum.org', latitude=51.5194, longitude=-0.1265, city=london, type=museum)
        Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(17, 30, 0), free=True, museum=bm)
        Period(open=True, openTime=datetime.time(10,0,0), closedTime=datetime.time(20, 30, 0), weekday=4, free=True, museum=bm)

        db.session.add(uk)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def testGetValidPeriods(self):
        date = datetime.datetime(2016, 4, 4)
        museum = Museum.query.first()
        periods = museum.getValidPeriods(date)
        self.assertTrue(len(periods) > 0)

    def testGeneralPeriod(self):
        # Test date is 4/4/2016 - a monday, which has a general opening time
        date = datetime.datetime(2016, 4, 4)
        museum = Museum.query.first()

        periods = museum.getValidPeriods(date)

        noWeekday = reduce(lambda a,b: a or b, map((lambda x: x.weekday is None), periods))

        self.assertTrue(noWeekday)

    def testSpecificPeriod(self):
        # Test date is 8/4/2016 - a friday, which has a specific opening time
        date = datetime.datetime(2016, 4, 8)
        museum = Museum.query.first()

        periods = museum.getValidPeriods(date)

        weekday = reduce(lambda a,b: a or b, map((lambda x: x.weekday is date.weekday()), periods))

        self.assertTrue(weekday)

    def testIsClosed(self):
        date = datetime.datetime(2016, 4, 4)
        museum = Museum.query.first()
        self.assertFalse(museum.isClosed(date))

    def testIsFree(self):
        date = datetime.datetime(2016, 4, 4)
        museum = Museum.query.first()
        self.assertTrue(museum.isFree(date))
