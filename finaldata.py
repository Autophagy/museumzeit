import datetime

# Countries

def getCountries():

    countries = {
        'United Kingdom': ('uk.png')
    }

    return countries

# Cities

def getCities():

    cities = {
        'London': ('Europe/London', 'United Kingdom')
    }

    return cities

# Types

def getTypes():

    types = {
        'Museum': ('museum.png'),
        'Art Gallery': ('artGallery.png')
    }

    return types

# Museums

def getMuseums():

    museums = {
        'British Museum': ("The British Museum is a museum dedicated to human history, art, and culture, located in the Bloomsbury area of London. Its permanent collection, numbering some 8 million works, is among the largest and most comprehensive in existence and originates from all continents, illustrating and documenting the story of human culture from its beginnings to the present.", 'http://www.britishmuseum.org', 51.5194, -0.1265, 'London', 'Museum'),
        'Design Museum': ("Design Museum is a museum founded in 1989, located by the River Thames near Tower Bridge in central London, England. The museum covers product, industrial, graphic, fashion and architectural design. In 2007 the museum was listed by The Times newspaper as number two in their top five museums of the year.", 'https://designmuseum.org/', 51.50261, -0.072006, 'London', 'Museum'),
        'Dulwich Picture Gallery': ("Dulwich Picture Gallery is an art gallery in Dulwich, South London. The gallery, designed by Regency architect Sir John Soane using an innovative and influential method of illumination, was opened to the public in 1817. It is the oldest public art gallery in England and was made an independent charitable trust in 1994. Until this time the gallery was part of Alleyn's College of God's Gift, a charitable foundation established by the actor, entrepreneur and philanthropist Edward Alleyn in the early-17th century. The acquisition of artworks by its founders and bequests from its many patrons resulted in Dulwich Picture Gallery housing one of the country's finest collections of Old Masters, especially rich in French, Italian and Spanish Baroque paintings and in British portraits from Tudor times to the 19th century.", 'http://www.dulwichpicturegallery.org.uk/', 51.44632, -0.085962, 'London', 'Art Gallery'),
        'Horniman Museum': ("The Horniman Museum is a British museum in Forest Hill, London, England. Commissioned in 1898, it opened in 1901 and was designed by Charles Harrison Townsend in the Arts and Crafts style.", 'http://www.horniman.ac.uk/', 51.441034, -0.061013, 'London', 'Museum'),
        'Imperial War Museum': ("Located in building of the Bethlem Royal Hospital, the museum's collections include archives of personal and official documents, photographs, film and video material, and oral history recordings; an extensive library, a large art collection, and examples of military vehicles and aircraft, equipment and other artefacts - much of from conflicts during the twentieth century.", 'http://www.iwm.org.uk', 51.495794, -0.108653, 'London', 'Museum'),
        'Jewish Museum London': ("The Jewish Museum London is a museum of British Jewish life, history and identity. The museum is situated in the London Borough of Camden, North London. It is a place for people of all ages, faiths and background to explore Jewish history, culture, and heritage. The museum has a dedicated education team, with an extensive programme for schools, community groups and families alike. The events, programmes and activities at the museum aim to provoke questions, challenge prejudice, and encourage understanding.", 'http://www.jewishmuseum.org.uk/', 51.53734, -0.144584, 'London', 'Museum'),
        'London Transport Museum': ("The London Transport Museum, or LT Museum based in Covent Garden, London, seeks to conserve and explain the transport heritage of Britain's capital city. The majority of the museum's exhibits originated in the collection of London Transport, but, since the creation of Transport for London (TfL) in 2000, the remit of the museum has expanded to cover all aspects of transportation in the city.", 'http://www.ltmuseum.co.uk/', 51.511926, -0.121429, 'London', 'Museum'),
        'Museum of London': ("The Museum of London documents the history of London from prehistoric to modern times. The museum is located on London Wall, close to the Barbican Centre as part of the striking Barbican complex of buildings created in the 1960s and 1970s as an innovative approach to re-development within a bomb-damaged area of the City of London. It is a few minutes' walk north of St Paul's Cathedral, overlooking the remains of the Roman city wall and on the edge of the oldest part of London, now its main financial district. It is primarily concerned with the social history of London and its inhabitants throughout time. The museum is jointly controlled and funded by the City of London Corporation and the Greater London Authority.", 'http://www.museumoflondon.org.uk/museum-london', 51.517617, -0.096776, 'London', 'Museum'),
        'National Gallery': ("The National Gallery is an art museum in Trafalgar Square in the City of Westminster, in Central London. Founded in 1824, it houses a collection of over 2,300 paintings dating from the mid-13th century to 1900. The Gallery is an exempt charity, and a non-departmental public body of the Department for Culture, Media and Sport. Its collection belongs to the public of the United Kingdom and entry to the main collection is free of charge. It is among the most visited art museums in the world, after the Mus&eacute;e du Louvre, the British Museum, and the Metropolitan Museum of Art.", 'https://www.nationalgallery.org.uk', 51.5089, -0.1283, 'London', 'Art Gallery'),
        'National Maritime Museum': ("The National Maritime Museum (NMM) in Greenwich, London, is the leading maritime museum of the United Kingdom and may be the largest museum of its kind in the world. The historic buildings form part of the Maritime Greenwich World Heritage Site, and it also incorporates the Royal Observatory, and 17th-century Queen's House. In 2012, Her Majesty The Queen formally approved Royal Museums Greenwich as the new overall title for the National Maritime Museum, Queen's House, the Royal Observatory, Greenwich and the Cutty Sark. The museum is a non-departmental public body sponsored by the Department for Culture, Media and Sport. Like other publicly funded national museums in the United Kingdom, the National Maritime Museum does not levy an admission charge although most temporary exhibitions do incur admission charges.", 'http://www.rmg.co.uk/national-maritime-museum', 51.480874, -0.005288, 'London', 'Museum'),
        'National Portrait Gallery': ("The National Portrait Gallery (NPG) is an art gallery in London housing a collection of portraits of historically important and famous British people. It was the first portrait gallery in the world when it opened in 1856. The gallery moved in 1896 to its current site at St Martin's Place, off Trafalgar Square, and adjoining the National Gallery. It has been expanded twice since then. The National Portrait Gallery also has three regional outposts at Beningbrough Hall, Bodelwyddan Castle and Montacute House. It is unconnected to the Scottish National Portrait Gallery in Edinburgh, with which its remit overlaps. The gallery is a non-departmental public body sponsored by the Department for Culture, Media and Sport.", 'http://www.npg.org.uk/', 51.509425, -0.128124, 'London', 'Art Gallery'),
        'Natural History Museum': ("The Natural History Museum in London is home to life and earth science specimens comprising some 80 million items within five main collections: botany, entomology, mineralogy, paleontology and zoology. The museum is a world-renowned centre of research specialising in taxonomy, identification and conservation. Given the age of the institution, many of the collections have great historical as well as scientific value, such as specimens collected by Charles Darwin. The museum is particularly famous for its exhibition of dinosaur skeletons and ornate architecture - sometimes dubbed a cathedral of nature - both exemplified by the large Diplodocus cast which dominates the vaulted central hall. The Natural History Museum Library contains extensive books, journals, manuscripts, and artwork collections linked to the work and research of the scientific departments; access to the library is by appointment only. The museum is recognised as the pre-eminent centre of natural history and research of related fields in the world.", 'http://www.nhm.ac.uk', 51.4967, -0.1764, 'London', 'Museum'),
        'Science Museum': ("The Science Museum holds a collection of over 300,000 items, including such famous items as Stephenson's Rocket, Puffing Billy (the oldest surviving steam locomotive), the first jet engine, a reconstruction of Francis Crick and James Watson's model of DNA, some of the earliest remaining steam engines, a working example of Charles Babbage's Difference engine, the first prototype of the 10,000-year Clock of the Long Now, and documentation of the first typewriter. It also contains hundreds of interactive exhibits. A recent addition is the IMAX 3D Cinema showing science and nature documentaries, most of them in 3-D, and the Wellcome Wing which focuses on digital technology.", 'http://www.sciencemuseum.org.uk', 51.4978, -0.1745, 'London', 'Museum'),
        'Tate Britain': ("Tate Britain (known from 1897 to 1932 as the National Gallery of British Art and from 1932 to 2000 as the Tate Gallery) is an art museum on Millbank in London. It is part of the Tate network of galleries in England, with Tate Modern, Tate Liverpool and Tate St Ives. It is the oldest gallery in the network, having opened in 1897. It houses a substantial collection of the art of the United Kingdom since Tudor times, and in particular has large holdings of the works of J. M. W. Turner, who bequeathed all his own collection to the nation.", 'http://www.tate.org.uk/visit/tate-britain', 51.491055, -0.127795, 'London', 'Museum'),
        'Tate Modern': ("Tate Modern is a modern art gallery located in London. It is Britain's national gallery of international modern art and forms part of the Tate group (together with Tate Britain, Tate Liverpool, Tate St Ives and Tate Online). It is based in the former Bankside Power Station, in the Bankside area of the London Borough of Southwark. Tate holds the national collection of British art from 1900 to the present day and international modern and contemporary art. It is one of the largest museums of modern and contemporary art in the world.", 'http://www.tate.org.uk/visit/tate-modern', 51.507593, -0.099353, 'London', 'Museum'),
        'V&A': ("The V&A covers 12.5 acres (5.1 ha) and 145 galleries. Its collection spans 5,000 years of art, from ancient times to the present day, from the cultures of Europe, North America, Asia and North Africa. The holdings of ceramics, glass, textiles, costumes, silver, ironwork, jewellery, furniture, medieval objects, sculpture, prints and printmaking, drawings and photographs are among the largest and most comprehensive in the world. The museum owns the world's largest collection of post-classical sculpture, with the holdings of Italian Renaissance items being the largest outside Italy. The departments of Asia include art from South Asia, China, Japan, Korea and the Islamic world. The East Asian collections are among the best in Europe, with particular strengths in ceramics and metalwork, while the Islamic collection is amongst the largest in the Western world.", 'https://www.vam.ac.uk/', 51.496639, -0.172181, 'London', 'Museum'),
        'Wallace Collection': ("The Wallace Collection is an art collection in London open to the public, housed at Hertford House in Manchester Square, London, the former townhouse of the Seymour family, Marquesses of Hertford. It comprises a world-famous range of fine and decorative arts from the 15th to the 19th centuries with large holdings of French 18th-century paintings, furniture, arms & armour, porcelain and Old Master paintings arranged into 25 galleries.", 'http://www.wallacecollection.org/', 51.517462, -0.15297, 'London', 'Art Gallery'),
    }

    return museums

# Periods

def getPeriods():

    periods = [
        [True, datetime.time(10,0,0), datetime.time(17, 30, 0), None, True, 'British Museum'],
        [True, datetime.time(10,0,0), datetime.time(20, 30, 0), 4, True, 'British Museum'],
        [True, datetime.time(10,0,0), datetime.time(17, 45, 0), None, False, 'Design Museum'],
        [True, datetime.time(10,0,0), datetime.time(17, 00, 0), None, False, 'Dulwich Picture Gallery'],
        [False, datetime.time(12,0,0), datetime.time(12, 30, 0), 0, False, 'Dulwich Picture Gallery'],
        [True, datetime.time(10,30,0), datetime.time(17, 30, 0), None, True, 'Horniman Museum'],
        [True, datetime.time(10,00,0), datetime.time(18, 00, 0), None, True, 'Imperial War Museum'],
        [True, datetime.time(10,0,0), datetime.time(17, 00, 0), None, False, 'Jewish Museum London'],
        [False, datetime.time(12,0,0), datetime.time(12, 30, 0), 4, False, 'Jewish Museum London'],
        [True, datetime.time(10,0,0), datetime.time(18, 00, 0), None, False, 'London Transport Museum'],
        [True, datetime.time(11,0,0), datetime.time(18, 00, 0), 4, False, 'London Transport Museum'],
        [True, datetime.time(10,00,0), datetime.time(18, 00, 0), None, True, 'Museum of London'],
        [True, datetime.time(10,0,0), datetime.time(18, 00, 0), None, True, 'National Gallery'],
        [True, datetime.time(10,0,0), datetime.time(21, 00, 0), 4, True, 'National Gallery'],
        [True, datetime.time(10,0,0), datetime.time(17, 00, 0), None, True, 'National Maritime Museum'],
        [True, datetime.time(10,0,0), datetime.time(18, 00, 0), None, True, 'National Portrait Gallery'],
        [True, datetime.time(10,0,0), datetime.time(21, 00, 0), 3, True, 'National Portrait Gallery'],
        [True, datetime.time(10,0,0), datetime.time(21, 00, 0), 4, True, 'National Portrait Gallery'],
        [True, datetime.time(10,0,0), datetime.time(17, 50, 0), None, True, 'Natural History Museum'],
        [True, datetime.time(10,0,0), datetime.time(18, 00, 0), None, True, 'Science Museum'],
        [True, datetime.time(10,0,0), datetime.time(18, 00, 0), None, True, 'Tate Britain'],
        [True, datetime.time(10,0,0), datetime.time(18, 00, 0), None, True, 'Tate Modern'],
        [True, datetime.time(10,0,0), datetime.time(22, 00, 0), 4, True, 'Tate Modern'],
        [True, datetime.time(10,0,0), datetime.time(22, 00, 0), 5, True, 'Tate Modern'],
        [True, datetime.time(10,0,0), datetime.time(17, 45, 0), None, True, 'V&A'],
        [True, datetime.time(10,0,0), datetime.time(22, 00, 0), 4, True, 'V&A'],
        [True, datetime.time(10,00,0), datetime.time(17, 00, 0), None, True, 'Wallace Collection']
    ]

    return periods
