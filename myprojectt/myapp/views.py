from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from .models import Package
from django.http import HttpResponse
from weasyprint import HTML
import tempfile
import os


def index(request):
    return render(request, 'customers/home.html')

def all_cars(request):
    return render(request, 'customers/allcars.html')

def about_view(request):
    return render(request, 'customers/about.html')

def contact_view(request):
    return render(request, 'customers/contact.html')

def domestic(request):
    return render(request, 'customers/domestic_tamilnadu.html')


def all_destinations(request):
    return render(request, 'customers/all_destination.html')

def destination_detail(request, destination_slug):
    # Complete destination data with detailed itineraries for all 30 destinations
    destination_data = {
        'madurai': {
            'name': 'Madurai',
            'tagline': 'City of Temples',
            'duration': '3 Days',
            'image_path': 'images/madurai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Meenakshi Temple',
                    'activities': [
                        'Arrive in Madurai and check into your hotel',
                        'Afternoon visit to the magnificent Meenakshi Amman Temple',
                        'Explore the temple complex with its 14 gopurams',
                        'Evening: Witness the evening ceremony at the temple'
                    ],
                    'highlight': 'Evening puja ceremony at Meenakshi Temple'
                },
                {
                    'day': 2,
                    'title': 'Historical Exploration',
                    'activities': [
                        'Morning visit to Thirumalai Nayakkar Palace',
                        'Explore the Gandhi Museum',
                        'Afternoon visit to Alagar Koyil',
                        'Evening shopping for Madurai specialties'
                    ],
                    'highlight': 'Light and sound show at Thirumalai Nayakkar Palace'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Vandiyur Mariamman Teppakulam',
                        'Last minute shopping for souvenirs',
                        'Depart from Madurai'
                    ],
                    'highlight': 'Boat ride in the temple tank (seasonal)'
                }
            ]
        },
        'ooty': {
            'name': 'Ooty',
            'tagline': 'Queen of Hill Stations',
            'duration': '4 Days',
            'image_path': 'images/ooty.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Local Sightseeing',
                    'activities': [
                        'Arrive in Ooty and check into your hotel',
                        'Visit the Botanical Gardens',
                        'Enjoy a ride on the Nilgiri Mountain Railway',
                        'Evening stroll around Ooty Lake'
                    ],
                    'highlight': 'Toy train ride through scenic landscapes'
                },
                {
                    'day': 2,
                    'title': 'Nature Exploration',
                    'activities': [
                        'Morning visit to Doddabetta Peak',
                        'Explore Pykara Lake and Waterfalls',
                        'Visit the Tea Museum',
                        'Evening at Rose Garden'
                    ],
                    'highlight': 'Boat ride in Pykara Lake'
                },
                {
                    'day': 3,
                    'title': 'Coonoor Excursion',
                    'activities': [
                        'Day trip to Coonoor',
                        'Visit Sims Park and Lamb\'s Rock',
                        'Explore tea plantations',
                        'Return to Ooty in evening'
                    ],
                    'highlight': 'View from Dolphin\'s Nose'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to local markets',
                        'Buy homemade chocolates and tea',
                        'Depart from Ooty'
                    ],
                    'highlight': 'Shopping for Ooty specialties'
                }
            ]
        },
        'mahabalipuram': {
            'name': 'Mahabalipuram',
            'tagline': 'UNESCO World Heritage Site',
            'duration': '2 Days',
            'image_path': 'images/mahabalipuram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Shore Temple',
                    'activities': [
                        'Arrive in Mahabalipuram and check in',
                        'Visit the Shore Temple complex',
                        'Explore Pancha Rathas',
                        'Evening at the beach'
                    ],
                    'highlight': 'Sunset view of Shore Temple'
                },
                {
                    'day': 2,
                    'title': 'Rock Cut Monuments',
                    'activities': [
                        'Morning visit to Arjuna\'s Penance',
                        'See Krishna\'s Butterball',
                        'Explore the Tiger Cave',
                        'Depart from Mahabalipuram'
                    ],
                    'highlight': 'Detailed guide of Arjuna\'s Penance'
                }
            ]
        },
        'kanyakumari': {
            'name': 'Kanyakumari',
            'tagline': 'Land\'s End of India',
            'duration': '2 Days',
            'image_path': 'images/kanyakumari.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Sunset View',
                    'activities': [
                        'Arrive in Kanyakumari and check in',
                        'Visit Vivekananda Rock Memorial',
                        'See Thiruvalluvar Statue',
                        'Witness sunset at Triveni Sangam'
                    ],
                    'highlight': 'Sunset viewing point'
                },
                {
                    'day': 2,
                    'title': 'Sunrise & Departure',
                    'activities': [
                        'Early morning sunrise viewing',
                        'Visit Kumari Amman Temple',
                        'See Gandhi Memorial',
                        'Depart from Kanyakumari'
                    ],
                    'highlight': 'Sunrise over the Bay of Bengal'
                }
            ]
        },
        'chettinad': {
            'name': 'Chettinad',
            'tagline': 'Land of Mansions & Spices',
            'duration': '2 Days',
            'image_path': 'images/chettinad.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Heritage Walk',
                    'activities': [
                        'Arrive in Chettinad and check in',
                        'Heritage walk through Chettinad mansions',
                        'Visit local craft workshops',
                        'Evening cooking demonstration'
                    ],
                    'highlight': 'Chettinad mansion architecture'
                },
                {
                    'day': 2,
                    'title': 'Cultural Experience',
                    'activities': [
                        'Visit Athangudi tile factory',
                        'Explore local markets for spices',
                        'Lunch with authentic Chettinad cuisine',
                        'Depart from Chettinad'
                    ],
                    'highlight': 'Authentic Chettinad meal'
                }
            ]
        },
        'kodaikanal': {
            'name': 'Kodaikanal',
            'tagline': 'Princess of Hill Stations',
            'duration': '3 Days',
            'image_path': 'images/kodainal.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Lake Tour',
                    'activities': [
                        'Arrive in Kodaikanal and check in',
                        'Boat ride on Kodai Lake',
                        'Walk through Coaker\'s Walk',
                        'Evening at Bryant Park'
                    ],
                    'highlight': 'Boat ride on the lake'
                },
                {
                    'day': 2,
                    'title': 'Nature Exploration',
                    'activities': [
                        'Visit Pillar Rocks and Guna Caves',
                        'See Silver Cascade waterfall',
                        'Explore Bear Shola Falls',
                        'Evening shopping'
                    ],
                    'highlight': 'View from Pillar Rocks'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Kurinji Andavar Temple',
                        'Buy homemade chocolates and oils',
                        'Depart from Kodaikanal'
                    ],
                    'highlight': 'Shopping for local products'
                }
            ]
        },
        'thanjavur': {
            'name': 'Thanjavur',
            'tagline': 'Rice Bowl of Tamil Nadu',
            'duration': '2 Days',
            'image_path': 'images/thanjavur.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Brihadeeswarar Temple',
                    'activities': [
                        'Arrive in Thanjavur and check in',
                        'Visit Brihadeeswarar Temple',
                        'Explore the Royal Palace',
                        'Evening at Sivaganga Park'
                    ],
                    'highlight': 'UNESCO World Heritage Site tour'
                },
                {
                    'day': 2,
                    'title': 'Art & Culture',
                    'activities': [
                        'Visit Saraswathi Mahal Library',
                        'See Thanjavur paintings demonstration',
                        'Explore local handicraft markets',
                        'Depart from Thanjavur'
                    ],
                    'highlight': 'Ancient manuscripts viewing'
                }
            ]
        },
        'rameshwaram': {
            'name': 'Rameshwaram',
            'tagline': 'Sacred Island Town',
            'duration': '2 Days',
            'image_path': 'images/rameshwaram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Temple Visit',
                    'activities': [
                        'Arrive in Rameshwaram and check in',
                        'Visit Ramanathaswamy Temple',
                        'Take holy bath in temple theerthams',
                        'Evening at Agnitheertham'
                    ],
                    'highlight': 'Temple rituals experience'
                },
                {
                    'day': 2,
                    'title': 'Dhanushkodi Excursion',
                    'activities': [
                        'Day trip to Dhanushkodi',
                        'Visit abandoned town and beach',
                        'See Adam\'s Bridge viewpoint',
                        'Depart from Rameshwaram'
                    ],
                    'highlight': 'Ghost town exploration'
                }
            ]
        },
        'yercaud': {
            'name': 'Yercaud',
            'tagline': 'Jewel of the South',
            'duration': '2 Days',
            'image_path': 'images/yercaud.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Local Sightseeing',
                    'activities': [
                        'Arrive in Yercaud and check in',
                        'Visit Yercaud Lake for boating',
                        'Explore Pagoda Point',
                        'Evening at Lady\'s Seat'
                    ],
                    'highlight': 'Sunset view from viewpoints'
                },
                {
                    'day': 2,
                    'title': 'Nature Walk & Departure',
                    'activities': [
                        'Morning coffee plantation visit',
                        'Trek to Kiliyur Falls (seasonal)',
                        'Buy local spices and coffee',
                        'Depart from Yercaud'
                    ],
                    'highlight': 'Coffee estate tour'
                }
            ]
        },
        'coonoor': {
            'name': 'Coonoor',
            'tagline': 'Tea Country Paradise',
            'duration': '2 Days',
            'image_path': 'images/coonoor.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Tea Estates',
                    'activities': [
                        'Arrive in Coonoor and check in',
                        'Visit tea estates and factories',
                        'Explore Sims Park',
                        'Evening at Dolphin\'s Nose viewpoint'
                    ],
                    'highlight': 'Tea tasting experience'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Morning visit to Lamb\'s Rock',
                        'Ride the Nilgiri Mountain Railway',
                        'Buy local tea and souvenirs',
                        'Depart from Coonoor'
                    ],
                    'highlight': 'Scenic train ride'
                }
            ]
        },
        'kumbakonam': {
            'name': 'Kumbakonam',
            'tagline': 'Temple Town',
            'duration': '2 Days',
            'image_path': 'images/kumbakonam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Temple Tour',
                    'activities': [
                        'Arrive in Kumbakonam and check in',
                        'Visit Adi Kumbeswarar Temple',
                        'Explore Nageswaran Temple',
                        'Evening at Mahamaham Tank'
                    ],
                    'highlight': 'Ancient temple architecture'
                },
                {
                    'day': 2,
                    'title': 'More Temples & Departure',
                    'activities': [
                        'Morning visit to Sarangapani Temple',
                        'See the famous bronze idols',
                        'Explore local handicrafts',
                        'Depart from Kumbakonam'
                    ],
                    'highlight': 'Bronze idol craftsmanship'
                }
            ]
        },
        'velankanni': {
            'name': 'Velankanni',
            'tagline': 'Lourdes of the East',
            'duration': '2 Days',
            'image_path': 'images/velankanni.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Basilica Visit',
                    'activities': [
                        'Arrive in Velankanni and check in',
                        'Visit Basilica of Our Lady of Good Health',
                        'Attend mass service',
                        'Evening beach walk'
                    ],
                    'highlight': 'Basilica architecture and history'
                },
                {
                    'day': 2,
                    'title': 'Spiritual Experience',
                    'activities': [
                        'Morning prayer and offerings',
                        'Visit museum and shrines',
                        'Explore local markets',
                        'Depart from Velankanni'
                    ],
                    'highlight': 'Spiritual atmosphere'
                }
            ]
        },
        'hogenakkal': {
            'name': 'Hogenakkal',
            'tagline': 'Niagara of India',
            'duration': '1 Day',
            'image_path': 'images/hogenakkal.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Waterfalls Experience',
                    'activities': [
                        'Morning drive to Hogenakkal',
                        'Coracle boat ride in the river',
                        'Swim in natural pools (seasonal)',
                        'Enjoy fish therapy',
                        'Return by evening'
                    ],
                    'highlight': 'Coracle ride through the falls'
                }
            ]
        },
        'courtallam': {
            'name': 'Courtallam',
            'tagline': 'Spa of South India',
            'duration': '1 Day',
            'image_path': 'images/courtallam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Waterfalls Tour',
                    'activities': [
                        'Morning drive to Courtallam',
                        'Visit Five Falls and Main Falls',
                        'Enjoy therapeutic bath in waterfalls',
                        'Explore local markets',
                        'Return by evening'
                    ],
                    'highlight': 'Medicinal properties of the falls'
                }
            ]
        },
        'kovalam': {
            'name': 'Kovalam',
            'tagline': 'Beach Paradise',
            'duration': '1 Day',
            'image_path': 'images/kovalam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Beach Day',
                    'activities': [
                        'Morning drive to Kovalam',
                        'Relax on the golden sands',
                        'Enjoy water sports (seasonal)',
                        'Fresh seafood lunch',
                        'Return by evening'
                    ],
                    'highlight': 'Serene beach experience'
                }
            ]
        },
        'pollachi': {
            'name': 'Pollachi',
            'tagline': 'Gateway to Western Ghats',
            'duration': '1 Day',
            'image_path': 'images/pollachi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Countryside Tour',
                    'activities': [
                        'Morning drive to Pollachi',
                        'Visit coconut and jaggery farms',
                        'Explore Anamalai Wildlife Sanctuary',
                        'Enjoy local cuisine',
                        'Return by evening'
                    ],
                    'highlight': 'Rustic countryside experience'
                }
            ]
        },
        'tranquebar': {
            'name': 'Tranquebar',
            'tagline': 'Danish Heritage Town',
            'duration': '1 Day',
            'image_path': 'images/tranquebar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Heritage Walk',
                    'activities': [
                        'Morning drive to Tranquebar',
                        'Visit Danish Fort Dansborg',
                        'Explore Zion Church and other colonial buildings',
                        'Beach walk and seafood lunch',
                        'Return by evening'
                    ],
                    'highlight': 'Colonial heritage exploration'
                }
            ]
        },
        'valparai': {
            'name': 'Valparai',
            'tagline': 'Emerald Green Plateau',
            'duration': '2 Days',
            'image_path': 'images/valparai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Tea Estates',
                    'activities': [
                        'Arrive in Valparai and check in',
                        'Visit tea and coffee plantations',
                        'Explore Sholayar Dam',
                        'Evening wildlife spotting'
                    ],
                    'highlight': 'Tea estate tour'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Morning visit to Aliyar Dam',
                        'Trek to Monkey Falls',
                        'Explore local markets',
                        'Depart from Valparai'
                    ],
                    'highlight': 'Scenic waterfalls'
                }
            ]
        },
        'dhanushkodi': {
            'name': 'Dhanushkodi',
            'tagline': 'Ghost Town',
            'duration': '1 Day',
            'image_path': 'images/dhanushkodi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Ghost Town Exploration',
                    'activities': [
                        'Morning drive to Dhanushkodi',
                        'Explore abandoned railway station and buildings',
                        'Visit Adam\'s Bridge viewpoint',
                        'Beach walk and photography',
                        'Return by evening'
                    ],
                    'highlight': 'Eerie abandoned town experience'
                }
            ]
        },
        'kolli-hills': {
            'name': 'Kolli Hills',
            'tagline': 'Land of 70 Hairpin Bends',
            'duration': '2 Days',
            'image_path': 'images/kolli-hills.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Scenic Views',
                    'activities': [
                        'Arrive in Kolli Hills and check in',
                        'Drive through 70 hairpin bends',
                        'Visit Agaya Gangai Waterfalls',
                        'Evening at Seekuparai Viewpoint'
                    ],
                    'highlight': 'Panoramic hill views'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Morning trek to Tampcol Medicinal Farm',
                        'Explore local tribal villages',
                        'Buy organic coffee and honey',
                        'Depart from Kolli Hills'
                    ],
                    'highlight': 'Tribal culture experience'
                }
            ]
        },
        'vellore': {
            'name': 'Vellore',
            'tagline': 'Fort City',
            'duration': '1 Day',
            'image_path': 'images/vellore.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Historical Tour',
                    'activities': [
                        'Morning drive to Vellore',
                        'Explore Vellore Fort',
                        'Visit Jalakandeswarar Temple',
                        'See the Golden Temple (Sripuram)',
                        'Return by evening'
                    ],
                    'highlight': 'Majestic fort architecture'
                }
            ]
        },
        'srirangam': {
            'name': 'Srirangam',
            'tagline': 'Temple Island',
            'duration': '1 Day',
            'image_path': 'images/srirangam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Tour',
                    'activities': [
                        'Morning drive to Srirangam',
                        'Explore Sri Ranganathaswamy Temple complex',
                        'Visit all 7 prakarams (enclosures)',
                        'See the famous golden vimana',
                        'Return by evening'
                    ],
                    'highlight': 'Massive temple complex exploration'
                }
            ]
        },
        'chidambaram': {
            'name': 'Chidambaram',
            'tagline': 'Dance of Shiva',
            'duration': '1 Day',
            'image_path': 'images/chidambaram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Experience',
                    'activities': [
                        'Morning drive to Chidambaram',
                        'Visit Nataraja Temple',
                        'Learn about cosmic dance of Shiva',
                        'Explore temple art and architecture',
                        'Return by evening'
                    ],
                    'highlight': 'Spiritual significance of the temple'
                }
            ]
        },
        'gangaikondacholapuram': {
            'name': 'Gangaikondacholapuram',
            'tagline': 'Chola Capital',
            'duration': '1 Day',
            'image_path': 'images/gangaikondacholapuram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'UNESCO Heritage Tour',
                    'activities': [
                        'Morning drive to Gangaikondacholapuram',
                        'Explore Brihadisvara Temple',
                        'Learn about Chola architecture',
                        'Visit nearby historical sites',
                        'Return by evening'
                    ],
                    'highlight': 'UNESCO World Heritage Site'
                }
            ]
        },
        'darasuram': {
            'name': 'Darasuram',
            'tagline': 'Chola Architectural Marvel',
            'duration': '1 Day',
            'image_path': 'images/darasuram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Exploration',
                    'activities': [
                        'Morning drive to Darasuram',
                        'Visit Airavatesvara Temple',
                        'Study intricate stone carvings',
                        'Learn about temple history',
                        'Return by evening'
                    ],
                    'highlight': 'Exquisite stone sculptures'
                }
            ]
        },
        'tiruvannamalai': {
            'name': 'Tiruvannamalai',
            'tagline': 'Spiritual Capital',
            'duration': '1 Day',
            'image_path': 'images/tiruvannamalai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple & Girivalam',
                    'activities': [
                        'Morning drive to Tiruvannamalai',
                        'Visit Arunachaleswarar Temple',
                        'Walk around the holy hill (Girivalam)',
                        'Visit Ramana Maharshi Ashram',
                        'Return by evening'
                    ],
                    'highlight': 'Spiritual energy of the mountain'
                }
            ]
        },
        'kanchipuram': {
            'name': 'Kanchipuram',
            'tagline': 'City of Thousand Temples',
            'duration': '1 Day',
            'image_path': 'images/kanchipuram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple & Silk Tour',
                    'activities': [
                        'Morning drive to Kanchipuram',
                        'Visit Ekambareswarar Temple',
                        'Explore Kailasanathar Temple',
                        'Silk saree shopping',
                        'Return by evening'
                    ],
                    'highlight': 'Ancient temples and silk weaving'
                }
            ]
        },
        'mudumalai': {
            'name': 'Mudumalai',
            'tagline': 'Wildlife Sanctuary',
            'duration': '2 Days',
            'image_path': 'images/mudumalai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Safari',
                    'activities': [
                        'Arrive in Mudumalai and check in',
                        'Afternoon jeep safari',
                        'Visit elephant camp',
                        'Evening nature walk'
                    ],
                    'highlight': 'Wildlife spotting'
                },
                {
                    'day': 2,
                    'title': 'More Wildlife & Departure',
                    'activities': [
                        'Morning bird watching',
                        'Visit tribal museum',
                        'Explore local markets',
                        'Depart from Mudumalai'
                    ],
                    'highlight': 'Elephant encounters'
                }
            ]
        },
        'vedanthangal': {
            'name': 'Vedanthangal',
            'tagline': 'Bird Watcher\'s Paradise',
            'duration': '1 Day',
            'image_path': 'images/vedanthangal.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Bird Sanctuary Visit',
                    'activities': [
                        'Early morning drive to Vedanthangal',
                        'Guided bird watching tour',
                        'Photography session',
                        'Learn about migratory birds',
                        'Return by evening'
                    ],
                    'highlight': 'Thousands of migratory birds'
                }
            ]
        },
        'pichavaram': {
            'name': 'Pichavaram',
            'tagline': 'Mangrove Forest',
            'duration': '1 Day',
            'image_path': 'images/pichavaram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Boat Ride Through Mangroves',
                    'activities': [
                        'Morning drive to Pichavaram',
                        'Boat ride through mangrove canals',
                        'Bird watching',
                        'Fresh seafood lunch',
                        'Return by evening'
                    ],
                    'highlight': 'Serene mangrove ecosystem'
                }
            ]
        },
        'yelagiri': {
            'name': 'Yelagiri',
            'tagline': 'Unexplored Hill Station',
            'duration': '2 Days',
            'image_path': 'images/yelagiri.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Nature Walk',
                    'activities': [
                        'Arrive in Yelagiri and check in',
                        'Visit Punganoor Lake Park',
                        'Explore Nature Park',
                        'Evening at Swamimalai Hills'
                    ],
                    'highlight': 'Peaceful hill station atmosphere'
                },
                {
                    'day': 2,
                    'title': 'Adventure & Departure',
                    'activities': [
                        'Morning paragliding (seasonal)',
                        'Visit Jalagamparai Waterfalls',
                        'Buy local honey and fruits',
                        'Depart from Yelagiri'
                    ],
                    'highlight': 'Adventure activities'
                }
            ]
        },
        'thoothukudi': {
            'name': 'Thoothukudi',
            'tagline': 'Pearl City',
            'duration': '1 Day',
            'image_path': 'images/tuticorin.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Port City Tour',
                    'activities': [
                        'Morning drive to Thoothukudi',
                        'Visit Harbour and beaches',
                        'Explore pearl markets',
                        'Enjoy famous Thoothukudi macaroon',
                        'Return by evening'
                    ],
                    'highlight': 'Pearl shopping'
                }
            ]
        },
        'karaikudi': {
            'name': 'Karaikudi',
            'tagline': 'Heart of Chettinad',
            'duration': '1 Day',
            'image_path': 'images/karaikudi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Chettinad Heritage',
                    'activities': [
                        'Morning drive to Karaikudi',
                        'Visit Chettinad mansions',
                        'Explore antique collections',
                        'Enjoy Chettinad lunch',
                        'Return by evening'
                    ],
                    'highlight': 'Grand mansions architecture'
                }
            ]
        },
        'kovilpatti': {
            'name': 'Kovilpatti',
            'tagline': 'Land of Sweets',
            'duration': '1 Day',
            'image_path': 'images/kovilpatti.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Culinary Tour',
                    'activities': [
                        'Morning drive to Kovilpatti',
                        'Visit kadalai mittai (peanut candy) factories',
                        'Explore local markets',
                        'Enjoy traditional sweets',
                        'Return by evening'
                    ],
                    'highlight': 'Famous peanut candy tasting'
                }
            ]
        },
        'salem': {
            'name': 'Salem',
            'tagline': 'Mango City',
            'duration': '1 Day',
            'image_path': 'images/salem.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'City Tour',
                    'activities': [
                        'Morning drive to Salem',
                        'Visit Sugavaneswarar Temple',
                        'Explore Kiliyur Falls',
                        'Shop for famous Salem silk',
                        'Return by evening'
                    ],
                    'highlight': 'Silk shopping'
                }
            ]
        },
        'erode': {
            'name': 'Erode',
            'tagline': 'Turmeric City',
            'duration': '1 Day',
            'image_path': 'images/erode.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Market Tour',
                    'activities': [
                        'Morning drive to Erode',
                        'Visit turmeric and textile markets',
                        'Explore Bhavani Sangameswarar Temple',
                        'Enjoy local cuisine',
                        'Return by evening'
                    ],
                    'highlight': 'Turmeric market experience'
                }
            ]
        }
    }
    
    destination = destination_data.get(destination_slug, {})
    return render(request, 'customers/destination_detail.html', {'destination': destination})

# admin
def admin_dashboard(request):
    packages = Package.objects.all()
    return render(request, 'customers/admin_dashboard.html', {'packages': packages})


def add_package(request):
    if request.method == "POST":
        name = request.POST["name"]
        customer = request.POST["customer"]
        destination = request.POST["destination"]
        start_date = request.POST["start_date"]
        duration = request.POST["duration"]
        pax = request.POST["pax"]
        amount = request.POST["amount"]

        day1 = request.POST["day1"]
        day2 = request.POST["day2"]
        day3 = request.POST["day3"]

        itinerary = f"Day 1: {day1}\nDay 2: {day2}\nDay 3: {day3}"

        Package.objects.create(
            name=name,
            customer=customer,
            destination=destination,
            start_date=start_date,
            duration=duration,
            pax=pax,
            amount=amount,
            itinerary=itinerary
        )
        return redirect("admin_dashboard")  

    return render(request, "customers/addpackage.html")


# pdf function
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_package_pdf(request, package_id):
    package = get_object_or_404(Package, pk=package_id)

    # Convert itinerary text to a dictionary format
    itinerary = {}
    lines = package.itinerary.strip().split('\n')
    for line in lines:
        if ':' in line:
            day, plan = line.split(':', 1)
            itinerary[day.strip()] = plan.strip()

    html_string = render_to_string("customers/pdfpage.html", {
        "package": {
            "name": package.name,
            "customer": package.customer,
            "amount": package.amount,
            "destination": package.destination,
            "start_date": package.start_date,
            "duration": package.duration,
            "pax": package.pax,
            "trip_id": package.trip_id,
            "itinerary": itinerary,
        }
    })


    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="Package_{package.name}.pdf"'
    return response


#international

def home(request): 
    return render(request,'International/international.html')
def all_international(request):
    return render(request, 'International/all_international.html')
def destination_detail_inter(request, destination_slug):
    # Complete international destination data with detailed itineraries
    destination_data = {
        'paris': {
            'name': 'Paris',
            'tagline': 'City of Love',
            'duration': '5 Days',
            'image_path': 'images/paris.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Eiffel Tower',
                    'activities': [
                        'Arrive in Paris and check into your hotel',
                        'Afternoon visit to the Eiffel Tower',
                        'Seine River cruise in the evening',
                        'Dinner in Montmartre'
                    ],
                    'highlight': 'Eiffel Tower views at sunset'
                },
                {
                    'day': 2,
                    'title': 'Art & History',
                    'activities': [
                        'Morning visit to the Louvre Museum',
                        'Explore Notre-Dame Cathedral',
                        'Walk along Champs-Élysées',
                        'Evening at Arc de Triomphe'
                    ],
                    'highlight': 'Seeing Mona Lisa at the Louvre'
                },
                {
                    'day': 3,
                    'title': 'Palace of Versailles',
                    'activities': [
                        'Day trip to Palace of Versailles',
                        'Tour of the Hall of Mirrors',
                        'Explore the royal gardens',
                        'Return to Paris for evening leisure'
                    ],
                    'highlight': 'Grandeur of Versailles Palace'
                },
                {
                    'day': 4,
                    'title': 'Cultural Exploration',
                    'activities': [
                        'Visit Musée d\'Orsay',
                        'Explore Latin Quarter',
                        'See Sacré-Cœur Basilica',
                        'Evening cabaret show at Moulin Rouge'
                    ],
                    'highlight': 'Montmartre artists\' square'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Last minute shopping at Galeries Lafayette',
                        'Visit Opera Garnier',
                        'Final French pastry tasting',
                        'Depart from Paris'
                    ],
                    'highlight': 'Shopping on Rue du Faubourg Saint-Honoré'
                }
            ]
        },
        'rome': {
            'name': 'Rome',
            'tagline': 'Eternal City',
            'duration': '4 Days',
            'image_path': 'images/rome.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Ancient Rome',
                    'activities': [
                        'Arrive in Rome and check into your hotel',
                        'Visit Colosseum and Roman Forum',
                        'See Palatine Hill',
                        'Evening walk through Piazza Navona'
                    ],
                    'highlight': 'Colosseum underground tour'
                },
                {
                    'day': 2,
                    'title': 'Vatican City',
                    'activities': [
                        'Morning visit to Vatican Museums',
                        'See Sistine Chapel',
                        'Tour St. Peter\'s Basilica',
                        'Evening at Trastevere district'
                    ],
                    'highlight': 'Michelangelo\'s Sistine Chapel ceiling'
                },
                {
                    'day': 3,
                    'title': 'Historic Center',
                    'activities': [
                        'Visit Pantheon',
                        'Throw coin in Trevi Fountain',
                        'Explore Spanish Steps',
                        'Evening food tour'
                    ],
                    'highlight': 'Gelato tasting near Pantheon'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Borghese Gallery',
                        'Last minute shopping',
                        'Final Italian espresso',
                        'Depart from Rome'
                    ],
                    'highlight': 'Borghese Gardens walk'
                }
            ]
        },
        'santorini': {
            'name': 'Santorini',
            'tagline': 'Greek Island Paradise',
            'duration': '4 Days',
            'image_path': 'images/santorini.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Oia Sunset',
                    'activities': [
                        'Arrive in Santorini and check into your hotel',
                        'Explore Fira town',
                        'Sunset viewing in Oia',
                        'Dinner with caldera views'
                    ],
                    'highlight': 'Famous Santorini sunset'
                },
                {
                    'day': 2,
                    'title': 'Volcano & Hot Springs',
                    'activities': [
                        'Boat tour to Nea Kameni volcano',
                        'Swim in hot springs',
                        'Visit Thirassia island',
                        'Evening in Imerovigli'
                    ],
                    'highlight': 'Volcanic hot springs swim'
                },
                {
                    'day': 3,
                    'title': 'Beach Day',
                    'activities': [
                        'Visit Red Beach',
                        'Relax at Perissa black sand beach',
                        'Wine tasting at local winery',
                        'Dinner in Pyrgos village'
                    ],
                    'highlight': 'Santorini wine tasting'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Akrotiri ruins',
                        'Last minute shopping for souvenirs',
                        'Final Greek coffee',
                        'Depart from Santorini'
                    ],
                    'highlight': 'Ancient Akrotiri archaeological site'
                }
            ]
        },
        'barcelona': {
            'name': 'Barcelona',
            'tagline': 'Gaudi\'s Masterpiece',
            'duration': '4 Days',
            'image_path': 'images/barcelona.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Gothic Quarter',
                    'activities': [
                        'Arrive in Barcelona and check into your hotel',
                        'Explore Gothic Quarter',
                        'Visit Barcelona Cathedral',
                        'Evening tapas tour'
                    ],
                    'highlight': 'Historic Gothic Quarter walk'
                },
                {
                    'day': 2,
                    'title': 'Gaudi Architecture',
                    'activities': [
                        'Visit Sagrada Familia',
                        'Explore Park Güell',
                        'See Casa Batlló',
                        'Evening at Magic Fountain show'
                    ],
                    'highlight': 'Sagrada Familia towers'
                },
                {
                    'day': 3,
                    'title': 'Montserrat & Local Culture',
                    'activities': [
                        'Day trip to Montserrat Monastery',
                        'Visit La Boqueria market',
                        'Walk along Las Ramblas',
                        'Flamenco show in evening'
                    ],
                    'highlight': 'Montserrat mountain views'
                },
                {
                    'day': 4,
                    'title': 'Beach & Departure',
                    'activities': [
                        'Morning at Barceloneta beach',
                        'Visit Picasso Museum',
                        'Last minute shopping',
                        'Depart from Barcelona'
                    ],
                    'highlight': 'Fresh seafood paella lunch'
                }
            ]
        },
        'tokyo': {
            'name': 'Tokyo',
            'tagline': 'Neon Metropolis',
            'duration': '5 Days',
            'image_path': 'images/tokyo.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Shibuya',
                    'activities': [
                        'Arrive in Tokyo and check into your hotel',
                        'See Shibuya Crossing',
                        'Visit Hachiko statue',
                        'Evening in Shinjuku'
                    ],
                    'highlight': 'Shibuya skyline view'
                },
                {
                    'day': 2,
                    'title': 'Traditional Tokyo',
                    'activities': [
                        'Visit Senso-ji Temple',
                        'Explore Asakusa district',
                        'Sumida River cruise',
                        'Evening at Tokyo Skytree'
                    ],
                    'highlight': 'Traditional tea ceremony'
                },
                {
                    'day': 3,
                    'title': 'Modern Tokyo',
                    'activities': [
                        'Visit teamLab Planets digital museum',
                        'Explore Akihabara electronics district',
                        'Harajuku and Takeshita Street',
                        'Robot Restaurant show'
                    ],
                    'highlight': 'Akihabara anime shopping'
                },
                {
                    'day': 4,
                    'title': 'Day Trip Options',
                    'activities': [
                        'Option 1: Nikko temples and nature',
                        'Option 2: Hakone hot springs',
                        'Option 3: Kamakura Great Buddha',
                        'Evening izakaya experience'
                    ],
                    'highlight': 'Onsen (hot spring) relaxation'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Tsukiji Outer Market',
                        'Visit Imperial Palace East Gardens',
                        'Last minute shopping in Ginza',
                        'Depart from Tokyo'
                    ],
                    'highlight': 'Fresh sushi breakfast'
                }
            ]
        },
        'bali': {
            'name': 'Bali',
            'tagline': 'Island of Gods',
            'duration': '6 Days',
            'image_path': 'images/bali.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Ubud',
                    'activities': [
                        'Arrive in Bali and transfer to Ubud',
                        'Visit Sacred Monkey Forest',
                        'Explore Ubud art market',
                        'Evening cultural performance'
                    ],
                    'highlight': 'Monkey Forest encounters'
                },
                {
                    'day': 2,
                    'title': 'Temples & Rice Terraces',
                    'activities': [
                        'Sunrise at Besakih Temple',
                        'Visit Tegallalang Rice Terraces',
                        'See Goa Gajah (Elephant Cave)',
                        'Evening Balinese cooking class'
                    ],
                    'highlight': 'Rice terrace swing photos'
                },
                {
                    'day': 3,
                    'title': 'Waterfalls & Volcano',
                    'activities': [
                        'Visit Tegenungan Waterfall',
                        'See Mount Batur volcano',
                        'Relax at hot springs',
                        'Sunset at Tanah Lot Temple'
                    ],
                    'highlight': 'Volcano views'
                },
                {
                    'day': 4,
                    'title': 'Beach Transfer & Relaxation',
                    'activities': [
                        'Transfer to Seminyak beach area',
                        'Relax at beach club',
                        'Sunset at Uluwatu Temple',
                        'Kecak fire dance performance'
                    ],
                    'highlight': 'Beach club luxury'
                },
                {
                    'day': 5,
                    'title': 'Island Exploration',
                    'activities': [
                        'Day trip to Nusa Penida island',
                        'See Kelingking Beach',
                        'Snorkel at Manta Point',
                        'Return to mainland'
                    ],
                    'highlight': 'Nusa Penida cliff views'
                },
                {
                    'day': 6,
                    'title': 'Departure',
                    'activities': [
                        'Morning spa treatment',
                        'Last minute shopping',
                        'Final Balinese meal',
                        'Depart from Bali'
                    ],
                    'highlight': 'Traditional Balinese massage'
                }
            ]
        },
        'dubai': {
            'name': 'Dubai',
            'tagline': 'City of Superlatives',
            'duration': '4 Days',
            'image_path': 'images/dubai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Modern Dubai',
                    'activities': [
                        'Arrive in Dubai and check into your hotel',
                        'Visit Burj Khalifa (At the Top)',
                        'Explore Dubai Mall and fountains',
                        'Evening desert safari with dinner'
                    ],
                    'highlight': 'Burj Khalifa observation deck'
                },
                {
                    'day': 2,
                    'title': 'Cultural & Traditional',
                    'activities': [
                        'Visit Dubai Museum',
                        'Explore Al Fahidi Historic District',
                        'Abra ride across Dubai Creek',
                        'Gold and spice souk shopping'
                    ],
                    'highlight': 'Traditional abra boat ride'
                },
                {
                    'day': 3,
                    'title': 'Palm Island & Luxury',
                    'activities': [
                        'Visit Palm Jumeirah',
                        'Aquaventure Waterpark',
                        'Lunch at Atlantis',
                        'Evening at The Pointe'
                    ],
                    'highlight': 'Palm Jumeirah monorail ride'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Jumeirah Beach',
                        'Visit Miracle Garden (seasonal)',
                        'Last minute shopping',
                        'Depart from Dubai'
                    ],
                    'highlight': 'Beach relaxation with Burj view'
                }
            ]
        },
        'newyork': {
            'name': 'New York',
            'tagline': 'The Big Apple',
            'duration': '5 Days',
            'image_path': 'images/newyork.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Manhattan',
                    'activities': [
                        'Arrive in NYC and check into your hotel',
                        'Times Square exploration',
                        'Broadway show in evening',
                        'Walk through Bryant Park'
                    ],
                    'highlight': 'First Broadway show experience'
                },
                {
                    'day': 2,
                    'title': 'Landmarks & Views',
                    'activities': [
                        'Statue of Liberty cruise',
                        'Visit Ellis Island',
                        'Walk across Brooklyn Bridge',
                        'Evening in DUMBO'
                    ],
                    'highlight': 'Statue of Liberty up close'
                },
                {
                    'day': 3,
                    'title': 'Museums & Central Park',
                    'activities': [
                        'Visit Metropolitan Museum of Art',
                        'Explore Central Park',
                        'See Guggenheim Museum',
                        'Evening rooftop bar'
                    ],
                    'highlight': 'Central Park bike ride'
                },
                {
                    'day': 4,
                    'title': 'Neighborhood Exploration',
                    'activities': [
                        'Explore Greenwich Village',
                        'Walk the High Line',
                        'Visit Chelsea Market',
                        'Evening in SoHo'
                    ],
                    'highlight': 'High Line elevated park'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Grand Central Terminal',
                        'Visit Top of the Rock or Edge',
                        'Last minute shopping',
                        'Depart from NYC'
                    ],
                    'highlight': 'Skyline views from observation deck'
                }
            ]
        },
        'machupicchu': {
            'name': 'Machu Picchu',
            'tagline': 'Lost City of the Incas',
            'duration': '4 Days',
            'image_path': 'images/machupicchu.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival in Cusco',
                    'activities': [
                        'Arrive in Cusco and acclimatize',
                        'Explore Plaza de Armas',
                        'Visit Sacsayhuamán ruins',
                        'Evening briefing'
                    ],
                    'highlight': 'First views of Cusco'
                },
                {
                    'day': 2,
                    'title': 'Sacred Valley',
                    'activities': [
                        'Visit Pisac market and ruins',
                        'Explore Ollantaytambo fortress',
                        'Train to Aguas Calientes',
                        'Prepare for Machu Picchu'
                    ],
                    'highlight': 'Sacred Valley scenery'
                },
                {
                    'day': 3,
                    'title': 'Machu Picchu',
                    'activities': [
                        'Sunrise at Machu Picchu',
                        'Guided tour of the citadel',
                        'Optional hike to Sun Gate',
                        'Return to Cusco'
                    ],
                    'highlight': 'First glimpse of Machu Picchu'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Visit Koricancha temple',
                        'Explore San Pedro market',
                        'Final Peruvian meal',
                        'Depart from Cusco'
                    ],
                    'highlight': 'Last minute alpaca souvenirs'
                }
            ]
        },
        'sydney': {
            'name': 'Sydney',
            'tagline': 'Harbor City',
            'duration': '4 Days',
            'image_path': 'images/sydney.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Harbor',
                    'activities': [
                        'Arrive in Sydney and check into your hotel',
                        'Visit Sydney Opera House',
                        'Walk across Harbour Bridge',
                        'Evening at The Rocks'
                    ],
                    'highlight': 'Opera House guided tour'
                },
                {
                    'day': 2,
                    'title': 'Beaches & Coastal Walk',
                    'activities': [
                        'Bondi Beach visit',
                        'Bondi to Coogee coastal walk',
                        'Relax at Bronte Beach',
                        'Evening in Darling Harbour'
                    ],
                    'highlight': 'Coastal walk scenery'
                },
                {
                    'day': 3,
                    'title': 'Blue Mountains',
                    'activities': [
                        'Day trip to Blue Mountains',
                        'See Three Sisters rock formation',
                        'Scenic World rides',
                        'Return to Sydney'
                    ],
                    'highlight': 'Blue Mountains vistas'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Manly Beach',
                        'Visit Taronga Zoo',
                        'Last minute shopping',
                        'Depart from Sydney'
                    ],
                    'highlight': 'Ferry ride to Manly'
                }
            ]
        },
        'kyoto': {
        'name': 'Kyoto',
        'tagline': 'Ancient Capital of Japan',
        'duration': '4 Days',
        'image_path': 'images/kyoto.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Higashiyama',
                'activities': [
                    'Arrive in Kyoto and check into ryokan',
                    'Visit Kiyomizu-dera Temple',
                    'Walk through Higashiyama district',
                    'Evening at Gion district'
                ],
                'highlight': 'Spotting geisha in Gion'
            },
            {
                'day': 2,
                'title': 'Golden Pavilion & Arashiyama',
                'activities': [
                    'Visit Kinkaku-ji (Golden Pavilion)',
                    'Explore Ryoan-ji rock garden',
                    'Bamboo forest in Arashiyama',
                    'Monkey Park visit'
                ],
                'highlight': 'Bamboo forest walk'
            },
            {
                'day': 3,
                'title': 'Fushimi & Nara Day Trip',
                'activities': [
                    'Fushimi Inari Shrine (thousand torii gates)',
                    'Day trip to Nara',
                    'See Todai-ji Temple and Great Buddha',
                    'Feed deer in Nara Park'
                ],
                'highlight': 'Fushimi Inari early morning'
            },
            {
                'day': 4,
                'title': 'Departure',
                'activities': [
                    'Morning at Nishiki Market',
                    'Tea ceremony experience',
                    'Last minute shopping',
                    'Depart from Kyoto'
                ],
                'highlight': 'Matcha tasting'
            }
        ]
    },
    'iceland': {
        'name': 'Iceland',
        'tagline': 'Land of Fire and Ice',
        'duration': '7 Days',
        'image_path': 'images/iceland.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Reykjavik',
                'activities': [
                    'Arrive in Reykjavik and check in',
                    'Explore Hallgrímskirkja church',
                    'Visit Harpa Concert Hall',
                    'Northern Lights hunt (seasonal)'
                ],
                'highlight': 'First glimpse of aurora'
            },
            {
                'day': 2,
                'title': 'Golden Circle',
                'activities': [
                    'Visit Thingvellir National Park',
                    'See Geysir geothermal area',
                    'Gullfoss waterfall',
                    'Secret Lagoon hot spring'
                ],
                'highlight': 'Strokkur geyser eruption'
            },
            {
                'day': 3,
                'title': 'South Coast',
                'activities': [
                    'Seljalandsfoss waterfall',
                    'Skogafoss waterfall',
                    'Black sand beach at Reynisfjara',
                    'Vik village visit'
                ],
                'highlight': 'Walking behind waterfalls'
            },
            {
                'day': 4,
                'title': 'Glacier & Lagoon',
                'activities': [
                    'Skaftafell National Park',
                    'Glacier hike on Vatnajökull',
                    'Jökulsárlón Glacier Lagoon',
                    'Diamond Beach'
                ],
                'highlight': 'Glacier lagoon boat tour'
            },
            {
                'day': 5,
                'title': 'East Fjords',
                'activities': [
                    'Scenic drive through fjords',
                    'Visit fishing villages',
                    'Hengifoss waterfall hike',
                    'Local seafood dinner'
                ],
                'highlight': 'Remote fjord landscapes'
            },
            {
                'day': 6,
                'title': 'Lake Myvatn',
                'activities': [
                    'Dettifoss waterfall',
                    'Myvatn geothermal area',
                    'Grjótagjá lava cave',
                    'Myvatn Nature Baths'
                ],
                'highlight': 'Blue Lagoon alternative'
            },
            {
                'day': 7,
                'title': 'Departure',
                'activities': [
                    'Whale watching tour',
                    'Last minute Reykjavik shopping',
                    'Try fermented shark (if brave)',
                    'Depart from Iceland'
                ],
                'highlight': 'Whale sightings'
            }
        ]
    },
    'cairo': {
        'name': 'Cairo',
        'tagline': 'City of a Thousand Minarets',
        'duration': '4 Days',
        'image_path': 'images/cairo.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Pyramids',
                'activities': [
                    'Arrive in Cairo and check in',
                    'Visit Giza Pyramids',
                    'See Great Sphinx',
                    'Sound and Light show at night'
                ],
                'highlight': 'First view of the pyramids'
            },
            {
                'day': 2,
                'title': 'Museum & Old Cairo',
                'activities': [
                    'Egyptian Museum visit',
                    'See Tutankhamun treasures',
                    'Explore Coptic Cairo',
                    'Khan el-Khalili bazaar'
                ],
                'highlight': 'Golden mask of Tutankhamun'
            },
            {
                'day': 3,
                'title': 'Islamic Cairo',
                'activities': [
                    'Visit Citadel of Saladin',
                    'Mohamed Ali Mosque',
                    'Al-Azhar Mosque',
                    'Dinner cruise on Nile'
                ],
                'highlight': 'Panoramic city views from Citadel'
            },
            {
                'day': 4,
                'title': 'Day Trip & Departure',
                'activities': [
                    'Day trip to Memphis and Saqqara',
                    'See Step Pyramid',
                    'Final Egyptian meal',
                    'Depart from Cairo'
                ],
                'highlight': 'Ancient Step Pyramid'
            }
        ]
    },
    'queenstown': {
        'name': 'Queenstown',
        'tagline': 'Adventure Capital of the World',
        'duration': '5 Days',
        'image_path': 'images/queenstown.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Scenic Views',
                'activities': [
                    'Arrive in Queenstown and check in',
                    'Gondola ride up Bob\'s Peak',
                    'Luge rides',
                    'Dinner with lake views'
                ],
                'highlight': 'Sunset over Lake Wakatipu'
            },
            {
                'day': 2,
                'title': 'Adventure Day',
                'activities': [
                    'Bungee jumping at Kawarau Bridge',
                    'Jet boat ride',
                    'Shotover Canyon Swing',
                    'Relax at Onsen Hot Pools'
                ],
                'highlight': 'First bungee jump'
            },
            {
                'day': 3,
                'title': 'Milford Sound',
                'activities': [
                    'Scenic drive to Milford Sound',
                    'Boat cruise on the fjord',
                    'See waterfalls and wildlife',
                    'Return to Queenstown'
                ],
                'highlight': 'Mitre Peak views'
            },
            {
                'day': 4,
                'title': 'Wine & Relaxation',
                'activities': [
                    'Gibbston Valley wine tour',
                    'Visit Arrowtown historic village',
                    'Fergburger experience',
                    'Evening lake walk'
                ],
                'highlight': 'Pinot Noir tasting'
            },
            {
                'day': 5,
                'title': 'Departure',
                'activities': [
                    'Morning hike to Queenstown Hill',
                    'Last minute shopping',
                    'Final NZ flat white coffee',
                    'Depart from Queenstown'
                ],
                'highlight': 'Panoramic hike views'
            }
        ]
    },
    'capetown': {
        'name': 'Cape Town',
        'tagline': 'Mother City',
        'duration': '5 Days',
        'image_path': 'images/capetown.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Waterfront',
                'activities': [
                    'Arrive in Cape Town and check in',
                    'Explore V&A Waterfront',
                    'Sunset at Signal Hill',
                    'Dinner with mountain views'
                ],
                'highlight': 'First view of Table Mountain'
            },
            {
                'day': 2,
                'title': 'Table Mountain & Penguins',
                'activities': [
                    'Cable car up Table Mountain',
                    'Hike to Maclear\'s Beacon',
                    'Visit Boulders Beach penguins',
                    'Chapman\'s Peak drive'
                ],
                'highlight': 'Penguin encounters'
            },
            {
                'day': 3,
                'title': 'Cape Peninsula',
                'activities': [
                    'Drive to Cape of Good Hope',
                    'Visit Cape Point lighthouse',
                    'Scenic coastal walks',
                    'Kirstenbosch Gardens'
                ],
                'highlight': 'Southernmost point of Africa'
            },
            {
                'day': 4,
                'title': 'Wine Lands',
                'activities': [
                    'Day trip to Stellenbosch',
                    'Wine tasting at 3-4 estates',
                    'Explore Franschhoek village',
                    'Wine tram experience'
                ],
                'highlight': 'South African wine tasting'
            },
            {
                'day': 5,
                'title': 'Departure',
                'activities': [
                    'Morning at Camps Bay beach',
                    'Visit Bo-Kaap colorful houses',
                    'Last minute shopping',
                    'Depart from Cape Town'
                ],
                'highlight': 'Bo-Kaap photography'
            }
        ]
    },
    'prague': {
        'name': 'Prague',
        'tagline': 'City of a Hundred Spires',
        'duration': '4 Days',
        'image_path': 'images/prague.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Old Town',
                'activities': [
                    'Arrive in Prague and check in',
                    'Old Town Square exploration',
                    'See Astronomical Clock',
                    'Charles Bridge at sunset'
                ],
                'highlight': 'Astronomical Clock show'
            },
            {
                'day': 2,
                'title': 'Castle & Lesser Town',
                'activities': [
                    'Prague Castle complex tour',
                    'St. Vitus Cathedral visit',
                    'Golden Lane exploration',
                    'Petrin Hill lookout'
                ],
                'highlight': 'Castle complex views'
            },
            {
                'day': 3,
                'title': 'Jewish Quarter & Culture',
                'activities': [
                    'Jewish Quarter walking tour',
                    'Visit Old Jewish Cemetery',
                    'Czech beer tasting',
                    'Black Light Theater show'
                ],
                'highlight': 'Historic Jewish sites'
            },
            {
                'day': 4,
                'title': 'Day Trip & Departure',
                'activities': [
                    'Day trip to Kutná Hora',
                    'See Sedlec Ossuary (Bone Church)',
                    'Last minute souvenir shopping',
                    'Depart from Prague'
                ],
                'highlight': 'Unique bone chapel'
            }
        ]
    },
    'maldives': {
        'name': 'Maldives',
        'tagline': 'Tropical Paradise',
        'duration': '5 Days',
        'image_path': 'images/maldives.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Resort',
                'activities': [
                    'Seaplane transfer to resort',
                    'Check into overwater bungalow',
                    'Resort orientation',
                    'Sunset cocktails on the beach'
                ],
                'highlight': 'First view of turquoise water'
            },
            {
                'day': 2,
                'title': 'Snorkeling & Relaxation',
                'activities': [
                    'House reef snorkeling',
                    'Relax on private deck',
                    'Spa treatment',
                    'Stargazing from bungalow'
                ],
                'highlight': 'Swimming with tropical fish'
            },
            {
                'day': 3,
                'title': 'Island Hopping',
                'activities': [
                    'Visit local fishing village',
                    'Picnic on deserted island',
                    'Dolphin watching cruise',
                    'Beach barbecue dinner'
                ],
                'highlight': 'Private island experience'
            },
            {
                'day': 4,
                'title': 'Water Activities',
                'activities': [
                    'Scuba diving (optional)',
                    'Stand-up paddleboarding',
                    'Sunset sailing',
                    'Underwater restaurant dinner'
                ],
                'highlight': 'Coral reef exploration'
            },
            {
                'day': 5,
                'title': 'Departure',
                'activities': [
                    'Final morning swim',
                    'Relax on beach until transfer',
                    'Seaplane back to Male',
                    'Depart from Maldives'
                ],
                'highlight': 'Last moments in paradise'
            }
        ]
    },
    'vienna': {
        'name': 'Vienna',
        'tagline': 'City of Music',
        'duration': '4 Days',
        'image_path': 'images/vienna.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Imperial Vienna',
                'activities': [
                    'Arrive in Vienna and check in',
                    'Visit Schönbrunn Palace',
                    'Walk through palace gardens',
                    'Evening classical concert'
                ],
                'highlight': 'Palace grandeur'
            },
            {
                'day': 2,
                'title': 'Historic Center',
                'activities': [
                    'St. Stephen\'s Cathedral',
                    'Hofburg Palace complex',
                    'Spanish Riding School',
                    'Café Central experience'
                ],
                'highlight': 'Viennese coffee culture'
            },
            {
                'day': 3,
                'title': 'Art & Culture',
                'activities': [
                    'Kunsthistorisches Museum',
                    'Belvedere Palace (Klimt\'s Kiss)',
                    'Prater amusement park',
                    'Heuriger wine tavern'
                ],
                'highlight': 'Seeing The Kiss painting'
            },
            {
                'day': 4,
                'title': 'Day Trip & Departure',
                'activities': [
                    'Day trip to Wachau Valley',
                    'Melk Abbey visit',
                    'Danube river cruise',
                    'Depart from Vienna'
                ],
                'highlight': 'Danube Valley scenery'
            }
        ]
    },
    'lisbon': {
        'name': 'Lisbon',
        'tagline': 'City of Seven Hills',
        'duration': '4 Days',
        'image_path': 'images/lisbon.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Alfama',
                'activities': [
                    'Arrive in Lisbon and check in',
                    'Explore Alfama district',
                    'Visit São Jorge Castle',
                    'Fado music evening'
                ],
                'highlight': 'Castle views over city'
            },
            {
                'day': 2,
                'title': 'Belém & Discoveries',
                'activities': [
                    'Jerónimos Monastery',
                    'Belém Tower',
                    'Pasteis de Belém tasting',
                    'Discoveries Monument'
                ],
                'highlight': 'Original custard tarts'
            },
            {
                'day': 3,
                'title': 'Sintra Day Trip',
                'activities': [
                    'Pena Palace visit',
                    'Quinta da Regaleira',
                    'Moorish Castle',
                    'Cabo da Roca sunset'
                ],
                'highlight': 'Colorful Pena Palace'
            },
            {
                'day': 4,
                'title': 'Departure',
                'activities': [
                    'Tram 28 ride',
                    'LX Factory exploration',
                    'Last minute shopping',
                    'Depart from Lisbon'
                ],
                'highlight': 'Iconic tram experience'
            }
        ]
    },
    'budapest': {
        'name': 'Budapest',
        'tagline': 'Pearl of the Danube',
        'duration': '4 Days',
        'image_path': 'images/budapest.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Pest Side',
                'activities': [
                    'Arrive in Budapest and check in',
                    'Heroes\' Square visit',
                    'Vajdahunyad Castle',
                    'Evening at ruin pub'
                ],
                'highlight': 'First ruin pub experience'
            },
            {
                'day': 2,
                'title': 'Buda Castle & Views',
                'activities': [
                    'Fisherman\'s Bastion',
                    'Matthias Church',
                    'Buda Castle tour',
                    'Danube cruise at night'
                ],
                'highlight': 'City views from Bastion'
            },
            {
                'day': 3,
                'title': 'Thermal Baths',
                'activities': [
                    'Széchenyi Thermal Baths',
                    'Andrássy Avenue walk',
                    'Opera House tour',
                    'Great Market Hall'
                ],
                'highlight': 'Thermal bath relaxation'
            },
            {
                'day': 4,
                'title': 'Departure',
                'activities': [
                    'Gellért Hill hike',
                    'Liberty Statue views',
                    'Last minute shopping',
                    'Depart from Budapest'
                ],
                'highlight': 'Final panoramic views'
            }
        ]
    },
    'amsterdam': {
        'name': 'Amsterdam',
        'tagline': 'Venice of the North',
        'duration': '4 Days',
        'image_path': 'images/amsterdam.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Canals',
                'activities': [
                    'Arrive in Amsterdam and check in',
                    'Canal cruise',
                    'Dam Square walk',
                    'Evening in Jordaan district'
                ],
                'highlight': 'First canal views'
            },
            {
                'day': 2,
                'title': 'Museums & Culture',
                'activities': [
                    'Rijksmuseum visit',
                    'Van Gogh Museum',
                    'Anne Frank House',
                    'Vondelpark relaxation'
                ],
                'highlight': 'Seeing Van Gogh\'s works'
            },
            {
                'day': 3,
                'title': 'Day Trip & Windmills',
                'activities': [
                    'Zaanse Schans windmills',
                    'Edam cheese tasting',
                    'Volendam fishing village',
                    'Evening bike tour'
                ],
                'highlight': 'Traditional windmills'
            },
            {
                'day': 4,
                'title': 'Departure',
                'activities': [
                    'Albert Cuyp Market',
                    'Last minute shopping',
                    'Final Dutch pancake',
                    'Depart from Amsterdam'
                ],
                'highlight': 'Local market experience'
            }
        ]
    },
    'seoul': {
        'name': 'Seoul',
        'tagline': 'Dynamic City',
        'duration': '5 Days',
        'image_path': 'images/seoul.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Modern Seoul',
                'activities': [
                    'Arrive in Seoul and check in',
                    'Lotte World Tower visit',
                    'Dongdaemun Design Plaza',
                    'Evening in Myeongdong'
                ],
                'highlight': 'City views from Lotte'
            },
            {
                'day': 2,
                'title': 'Palaces & History',
                'activities': [
                    'Gyeongbokgung Palace',
                    'Bukchon Hanok Village',
                    'Changdeokgung Palace',
                    'Insadong cultural street'
                ],
                'highlight': 'Palace guard ceremony'
            },
            {
                'day': 3,
                'title': 'DMZ Tour',
                'activities': [
                    'DMZ day tour',
                    'Third Infiltration Tunnel',
                    'Dora Observatory',
                    'Return to Seoul'
                ],
                'highlight': 'View into North Korea'
            },
            {
                'day': 4,
                'title': 'Markets & Street Food',
                'activities': [
                    'Gwangjang Market',
                    'Namsan Seoul Tower',
                    'Hongdae street performances',
                    'Korean BBQ dinner'
                ],
                'highlight': 'Street food tasting'
            },
            {
                'day': 5,
                'title': 'Departure',
                'activities': [
                    'Morning at Han River',
                    'Last minute shopping',
                    'Final Korean meal',
                    'Depart from Seoul'
                ],
                'highlight': 'Relaxing by Han River'
            }
        ]
    },
    'bangkok': {
        'name': 'Bangkok',
        'tagline': 'City of Angels',
        'duration': '4 Days',
        'image_path': 'images/bangkok.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Temples',
                'activities': [
                    'Arrive in Bangkok and check in',
                    'Grand Palace visit',
                    'Wat Pho (Reclining Buddha)',
                    'Evening at Khao San Road'
                ],
                'highlight': 'Emerald Buddha'
            },
            {
                'day': 2,
                'title': 'Markets & River',
                'activities': [
                    'Chatuchak Weekend Market',
                    'Chao Phraya River cruise',
                    'Wat Arun at sunset',
                    'Chinatown street food'
                ],
                'highlight': 'Massive market shopping'
            },
            {
                'day': 3,
                'title': 'Cultural Experiences',
                'activities': [
                    'Thai cooking class',
                    'Muay Thai boxing match',
                    'Traditional Thai massage',
                    'Rooftop bar evening'
                ],
                'highlight': 'Learning Thai cooking'
            },
            {
                'day': 4,
                'title': 'Day Trip & Departure',
                'activities': [
                    'Day trip to Ayutthaya',
                    'Ancient ruins exploration',
                    'Last minute shopping',
                    'Depart from Bangkok'
                ],
                'highlight': 'Historic Ayutthaya'
            }
        ]
    },
    'istanbul': {
        'name': 'Istanbul',
        'tagline': 'City on Two Continents',
        'duration': '5 Days',
        'image_path': 'images/istanbul.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Old City',
                'activities': [
                    'Arrive in Istanbul and check in',
                    'Hagia Sophia visit',
                    'Blue Mosque exploration',
                    'Evening in Sultanahmet'
                ],
                'highlight': 'First view of Hagia Sophia'
            },
            {
                'day': 2,
                'title': 'Topkapi & Bazaars',
                'activities': [
                    'Topkapi Palace tour',
                    'Grand Bazaar shopping',
                    'Spice Market visit',
                    'Bosphorus cruise'
                ],
                'highlight': 'Palace harem rooms'
            },
            {
                'day': 3,
                'title': 'Asian Side & Modern',
                'activities': [
                    'Cross to Asian side',
                    'Üsküdar and Kadıköy',
                    'Istiklal Street walk',
                    'Galata Tower sunset'
                ],
                'highlight': 'Two continents in one day'
            },
            {
                'day': 4,
                'title': 'Cultural Experiences',
                'activities': [
                    'Turkish bath experience',
                    'Whirling Dervish show',
                    'Traditional Turkish dinner',
                    'Nighttime city views'
                ],
                'highlight': 'Authentic hamam'
            },
            {
                'day': 5,
                'title': 'Departure',
                'activities': [
                    'Süleymaniye Mosque',
                    'Final Turkish coffee',
                    'Last minute shopping',
                    'Depart from Istanbul'
                ],
                'highlight': 'Mosque architecture'
            }
        ]
    }
       
    }
    
    destinationinter= destination_data.get(destination_slug, {})
    return render(request, 'International/destination_detail_inter.html', {'destinationinter': destinationinter})