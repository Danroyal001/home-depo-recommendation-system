import products as st

# Define mock product data with placeholder images
products = {
    180158: {
        'name': "ProCom 80,000 BTU Portable Single Convection Heater",
        'description': "ProCom Heating's Portable Convection Outdoor Propane Heaters, also referred to as \"trash can\" heaters in the trade, offer an inexpensive solution for temporary space heating especially for applications where there is no electricity. Compact, lightweight and clean burning, these heaters also feature a 360 heating radius which allows quick and efficient hot air distribution. These commercial grade heaters offer a perfect solution for temporary heating jobs such as garages, construction sites, warehouses, agricultural and industrial applications.California residents: see&nbsp;Proposition 65 information80,000 BTU variable convection heaters3 heat settings - 40,000, 60,000 and 80,000 BTUCirculates convection heat 360 in a degree radiusHeats up to 1,800 sq. ft.No electricity requiredPiezo matchless ignitionCSA  certifiedIncludes 10 ft. hose and regulatorHome Depot Protection Plan:",
        'image_url': "https://www.amazon.ca/ProCom-PCC80V-Portable-Single-Convection/dp/B00IPUFS4U"
    },

    111110: {
        'name': "HDX 4 ft. x 50 ft. 14-Gauge Green PVC-Coated Welded Wire",
        'description': "The HDX 4 ft. x 50 ft. Vinyl-Coated Welded Wire is made of galvanized and welded steel for long-lasting use. The green PVC coating helps create an upscale appearance that can complement natural surroundings. The general purpose fence is ideal for property delineation or the temporary confinement of non-aggressive animals.Galvanized and welded steel construction for long-lasting useMesh size: 3 in. x 2 in.14-GaugeGreen PVC coating helps create an upscale appearance that can complement natural surroundingsBuying Guide:",
        'image_url': "https://images.app.goo.gl/KXiymCPcFukdesxf7"
    },

    102816: {
        'name': "Delta Classic 400 32 in. x 60 in. x 60 in. 3-Piece Direct-to-Stud Tub Surround in High Gloss White",
        'description': "The Classic 400 32 in. X 60 in. x 60 in. 3-Piece Direct-to-Stud Tub Surround in High Gloss White is designed to fit 32 in. x 60 in. x 60 in. alcoves. This wall set offers an attractive design with the strength and durability of acrylic. This wall set also features six corner shelves and one center shelf for maximum storage. Classic 400 bathing systems offer style and design with the strength and durability of acrylic material. ProCrylic is a durable, bright white, high-gloss acrylic that provides all of the benefits of acrylic without the need for the rough, abrasive fiberglass backing.Actual product dimensions 60 in. W x 32.5 in. D x 60.38 in. HFits alcoves 32 in. x 60 in. x 60 in.Pairs with aspiration 38 in. x 48 in. single threshold shower base in high gloss white (model # 40034L or 40034R - sold separately) for a complete showering unitPremium high-gloss non-porous acrylic surface is durable and easy to cleanDirect-to-stud installation helps to create a long-lasting and secure unit7 built-in shelves provide much-needed storage spaceBuilt-in nailing flange to help ease installation3-piece design is easy to transportTub surround wall onlyBright white finish matches porcelain fixturesEasy to clean surface resists mildewEasy to handle material with no fiberglass backingNo mortar bed required saves time and money",
        'image_url': "https://images.app.goo.gl/wcxVvLTsXrDrqu8i7"
    },

    153802: {
        'name': "SharkBite 3/4 in. Copper Crimp Rings (100-Pack)",
        'description': "The SharkBite barb connection system is the best option for connecting PEX tubing in water distribution systems when lower material cost is desired. Constructed of copper, the SharkBite copper crimp rings are used in conjunction with barb fittings and crimp tools. And with a wide range of fittings, manifolds, regulator, thermostatic, and ball valves available, the SharkBite barb connection system is perfect for your next plumbing project.CopperCrimp tool allows each joint to be checked with go/no-go gaugeUsed in conjunction with PEX tubing and barb fittings, valves, and manifoldsAvailable in 3/8 in., 1/2 in., 3/4 in., & 1 in. sizesTool required has interchangeable jaws that do not require calibration",
        'image_url': "https://www.sharkbite.com/us/en/pex-pipe/pex-cutters-accessories/copper-crimp-ring"
    },

    150321: {
        'name': "6 ft. x 8 ft. Pressure-Treated Pine Shadowbox Fence Panel",
        'description': "Use the 6 ft. x 8 ft. Pressure Treated Spruce Shadowbox Fence Panel to help provide privacy in your yard. This panel is made of solid unpainted spruce, and is treated to provide resistance to termites and fungal decay. It can also be stained or painted as you see fit.California residents: see&nbsp;Proposition 65 informationPressure treated for long lifeNatural wood appearance can be stained or painted to suit your locationDesigned to enhance the appearance of your yardPanel measures 8 ft. wideNote: Product may vary by store",
        'image_url': "https://images.app.goo.gl/2tuNGoTrvr2WQ8kSA"
    },

    189550: {
        'name': "Hampton Bay Mix &amp; Match Chrome Double Glass Orb Table Lamp-Title 20",
        'description': "Hampton Bay's Mix and Match lamp program allows you to create your own signature lamp style. Create your lamp by choosing a shade or base from 2-sizes, (A) accent or (B) table, then pick from an array of traditional, contemporary, or transitional styles. The numerous choices of shades and bases are the perfect opportunity to refresh an outdated lamp, or you can start from scratch and design a whole lamp that's right for you.Beautifully crafted in metal / poly for added eleganceMix & match for additional looks for all seasons, moods and decorUse 1-standard medium base 13 watt CFL bulb (included)Choose any matching size shade to finish your lookEasy to install - harp and finial included where neededHome Depot Protection Plan:",
        'image_url': "https://images.app.goo.gl/smPgibjL92FYh2rBA"
    },

    146952: {
        'name': "Hitachi 7/8 in. x 0.120 in. Full Round-Head Smooth Shank Electro Galvanized Wire Coil Roofing Nails (7,200-Pack)",
        'description': "The Full Round-Head Smooth Shank Wire Coil Electro-Galvanized Roofing Nails fit Hitachi NV45AB, NV45AB2, NV45AB2S, NV45AE and NV45AES roofing nailers. These nails have a smooth shank with an Electro-Galvanized finish. This item is 7/8 in. in length x 0.120 in. in diameter and comes in a (7,200-pack). Every Hitachi accessory is designed to the highest standards and is rigorously tested for both performance and durability. Since its inception, Hitachi has pioneered innovative technologies that have improved the quality of craftsmanship worldwide. Hitachi is a leader in power tool research and development and has achieved many firsts in the power tool industry. Today, Hitachi continues the tradition of innovation and engineering with new features in addition to classic quality.Full round-head wire coil electro-galvanized roofing nailsFits Hitachi NV45AB, NV45AB2, NV45AB2S, NV45AE and NV45AES roofing nailersNails have a smooth shank and an electro-galvanized finishHas a 7/8 in. length x 0.120 in. diameter and comes in a 7,200-pack",
        'image_url': "https://images.app.goo.gl/nhEaT38B2aUaEarT9"
    },

    129672: {
        'name': "Bell 1-Gang Weatherproof Box with 3 1/2 in. Outlets",
        'description': "BELL weatherproof boxes are designed for use in branch circuit wiring in wet, damp, or dry locations.  Boxes house receptacles, switches, and GFCI's.  BELL Boxes may also be used as a weatherproof junction box. Closure plugs and installation hardware included. Ground screw is installed.State of the art powder coat finish provides maximum weatherability and scratch resistanceRugged die cast aluminum constructionInternal hub threads comply with NEMA requirements and will accept all threaded fittings and threaded conduit8 box mounting options with detachable lugs2 in. deep18.3 cubic in. capacityNEMA 3R Compliant",
        'image_url': "https://images.app.goo.gl/Zw66NKkWp6E2G9FcA"
    },

    167756: {
        'name': "Rust-Oleum Universal 12 oz. All Surface Satin White Spray Paint and Primer in One",
        'description': "Rust-Oleum Universal 12 oz. All Surface Satin White Spray Paint and Primer in One is designed for diverse substrates and works on virtually any surface: vinyl, metal, plastic, fiberglass, concrete, glass, wicker and wood. Universal is suitable for interior or exterior environments. Oil based formula covers up to 35 sq. ft., protects surfaces from rust and dries to the touch in as little as 30 minutes. A specially designed nozzle eliminates finger fatigue, protects against dripping and sprays from any angle, even upside down.California residents: see&nbsp;Proposition 65 informationInterior/exterior use, designed for diverse substrates and works on virtually any surface: vinyl, metal, plastic, fiberglass, concrete, glass, wicker and woodRust and corrosion resistant for enhanced durabilityCovers up to 35 sq. ft.Satin finish offers a soft, low-sheen look for any surfaceErgonomic cap eliminates finger fatigue and offers 360-degree, any-angle spray technologyOil-based formula with excellent adhesion resists fading and chippingDries to the touch in 30 minutesPaint and primer in oneClean up with mineral spiritsActual paint colors may vary from on-screen and printer representationsSee below for the full line of Universal products",
        'image_url': "https://images.app.goo.gl/3MYoV5kD7RAa9AmQ9"
    },

    106723: {
        'name': "Hampton Bay 3-Light Crawley Oil Rubbed Bronze Vanity Fixture",
        'description': "The versatile Crawley vanity fixtures feature a classic timeless architecture that adds an element of distinction to any bathroom. The Oil Rubbed Bronze hand applied finish coordinates with most faucet and hardware manufacturers for easy selection. The fixtures can be mounted in either the up or down position depending on the consumer's choice. The white glass shades provides modern day clean feel with old world design.White glass shadesMount with glass up or downCoordinates with most bronze faucetsEasy to installOil rubbed bronze finishHome Depot Protection Plan:",
        'image_url': "https://images.app.goo.gl/yMUQitZbRCRM66UC7"
    },

    175434: {
        'name': "LR Resources Vivid Floral Brown and Grey with a Purple Haze 5 ft. x 7 ft. 9 in. Indoor Area Rug-DISCONTINUED",
        'description': "A Single Outlined Flower Rests on a Monochromatic Ground, Creating a Look that is both Modern and Dramatic. 100% Acrylic Pile, Hand-Tufted in China. Durable Rug with a Minimal Shed Construction. Adds Flair to Any Home Environment with Hook and Cut Pile TePile Height (approximate) 1/2\"100% Acrylic PileDurable, minimal-shed constructionRug pad recommendedSpot clean, blot spills immediately and vacuum regularly",
        'image_url': "https://images.app.goo.gl/SAtwqsByiguoZ1LG8"
    },

    173941: {
        'name': "Wiremold 500 and 700 Series 5-1/2 in. Open Base Extension Box",
        'description': "Legrand/Wiremold small surface metal raceway systems are the ideal choice for a homeowner that wants to extend circuits or communication cabling in their home. Surface metal raceway allows you to extend circuits, add fixtures or outlets without disturbing the drywall, plaster or insulation in your home. All parts are paintable to blend with room decor. The leading choice of professionals is now available for your DIY project.90_ twist elbow kit enables a turn around an outside corner while changing the raceway channel's orientationAccommodates fixtures with 2-3/4 in. 3-1/2 in. and 4-1/16 in. mounting patternsCompatible with both Legrand/Wiremold 500 series (B-series) and 700 series (BW series) racewaysIvory finishPaintable and stainable using latex based productsUL listedNote: product may vary by store",
        'image_url': "https://images.app.goo.gl/e14DTqiSbJMA7fz16"
    },

    188002: {
        'name': "Builders Edge 15 in. x 52 in. Louvered Vinyl Exterior Shutters Pair in #002 Black",
        'description': "Builders Edge decorative 15 in. x 52 in. Louvered Vinyl Exterior Shutters Pair in #002 Black (actual 14.5 in. x 51.75 in.) are designed with a deep wood-grain texture for the appearance of wood shutters without the maintenance worries of wood. Durable copolymer construction features molded-through color so there is no paint to ever scratch or flake. Our shutters install on any surface: wood, vinyl, stucco, brick, or fiber cement. Includes Shutter-Lok fasteners for installation. Limited lifetime warranty.Available in 20 maintenance-free accent colors or a separate paintable optionMatching color installation hardware includedDue to materials, widths and lengths are nominalProduct cannot be paintedSold in pairsAK, HI ship to store onlyLimited lifetime warranty",
        'image_url': "https://images.app.goo.gl/xFum1r3A3j9LHiW67"
    },

    195936: {
        'name': "Leaktite Premium 5-gal. Food Storage Container (10-Pack)",
        'description': "Leaktite's 5 Gal. premium storage containers are manufactured to be safe for food storage. The premium design is manufactured from high quality plastic and is tough enough to store nails and screws along with any standard home or food needs. Includes 10 containers. Lids are available.All pails have a sturdy wire bail with a plastic handgripStrong reinforcing ribs guarantee that the containers keep their shapeThe wall thickness is .090 in.Made with a tapered design, pails nest to save space, and they separate easilyLids are not included with the buckets",
        'image_url': "https://images.app.goo.gl/NgjNvpk34yvZiLNy9"
    },

    112517: {
        'name': "KOHLER Wheatland Self-Rimming Cast Iron 33x22x9.625 4-Hole Kitchen Sink in White",
        'description': "A fresh new take on traditional sink design, Wheatland offers innovative features in a stylish package. Crafted from enameled cast iron, this sink resists scratching, burning, and staining for years of beauty and reliable performance. Large/medium bowls allow you to keep clean and dirty dishes separate, and the large bowl is extra-spacious to accommodate your biggest pots and pans.Click here to explore the Strength, Style, and Soul, of KOHLER Enameled Cast Iron.36-inch minimum base cabinet widthLarge/medium bowls9-inch depthThree faucet holes with one accessory hole to the rightRear drain increases workspace in the sink and storage space underneathKOHLER enameled cast ironTop-mountClick here to learn more about kitchen sinks",
        'image_url': "https://images.app.goo.gl/JKxfCzbuBnz7CCTF7"
    },

    100480: {
        'name': "Cub Cadet 3X 26 in. 357cc 3-Stage Electric Start Gas Snow Blower with Power Steering and Heated Grips",
        'description': "Introducing the revolutionary new Cub Cadet 3X 3-Stage snow blower. These industry exclusive cuts through tough packed snow and ice like no other machine available today. The 3X's unique high-speed Induction Accelerator draws snow through the system, creating an effortless forward motion. No backups. No ride ups. No spill over. This new 3X technology easily cuts through deep snowfall up to 50% faster than 2-Stage snow blowers. There's no stopping the next generation of Cub Cadet snow blowers.California residents: see&nbsp;Proposition 65 informationIdeal snowfall range: 6 in. to 16 in.Ideal surfaces: smooth and gravel surfaces; flat to slight slope26 in. clearing width, 21 in. intake height357cc electric start Cub Cadet 4-cycle OHV engineClear snow faster: new 3X induction accelerator moves snow up to 50% faster than 2X snow throwersTrigger controlled power steering at your fingertips for unmatched control, effortless maneuverability and 1-hand operationHeated hand grips for added comfortRevolutionary cool blue skid shoes glide along surfaces for better maneuverability and won't rust or damage your driveway6 forward and 2 reverse speeds allow for easy snow clearing at your pacePush button electric start makes it incredibly easy to start in tough winter conditionsSingle-hand 4-way chute control adjusts the chute rotation and pitch with 1-hand for the ultimate snow throwing controlIn-dash headlight allows you to clear your driveway any time of the day or night15 in. x 5 in. X-TRAC tires provide solid traction in extreme weather conditionsThrows snow up to 40 ft.Use 5-Walt-30 engine oil for easy starting at all temperaturesYou're covered winter after winter with a premium 3-year limited residential and 1-year limited commercial warranty and 5-year limited auger gearboxHome Depot Protection Plan:",
        'image_url': "https://images.app.goo.gl/PscQUbqrne8nGBau8"
    },

    139340: {
        'name': "Martha Stewart Living 1-3/8 in. Wood Single Bracket in Antique Mahogany",
        'description': "Martha Stewart Living 1-3/8 in. Brackets decorate your window with the inherent beauty of natural wood. The natural beauty of wood brackets adds style to any decor. The brackets screw into a wall to securely attach a wood pole to the surface for hanging window treatments.Use with 1-3/8 in. wood poleInclude 1-pair wood brackets and mounting hardwareUse 1-bracket for every 4 ft. of pole lengthExclusively at the Home Depot",
        'image_url': "https://images.app.goo.gl/hj8PZT72AHR6jsjAA"
    },

    203654: {
        'name': "Fathead 20 in. x 32 in. Troy Polamalu Pittsburgh Steelers Wall Decal",
        'description': "Your  Fathead Jr. has all the fun action and real-life graphics of Real. Big. Fathead Wall Graphics in a more space-friendly size. Fathead Jr. fits all kinds of spaces including doors, fridges, windows, tables, dorm rooms, etc.  And best of all, it is completely repositionable, and will not leave any residue on your wall.Rich, vivid, precision cut imagesEasy to apply: Just peel and stickMoveable and safe for wallsExtra coordinating images includedClick here to learn more about wall decor",
        'image_url': "https://images.app.goo.gl/RU2w68w9XkCpDuHt9"
    },

    115426: {
        'name': "Magic Chef 3.5 cu. ft. Mini Refrigerator in Stainless Look, ENERGYSTAR",
        'description': "Whether you're college-bound or simply want a little extra refrigerator space in your home, this Magic Chef 3.5 cu. ft. Compact Refrigerator has the storage options you're looking for. The sleek appearance is matched by its well-designed interior a can dispenser conveniently keeps soda in the door while additional door shelves provide space for other frequently used items. Glass refrigerator shelves are easy to clean.Energy Star qualified - meets or exceeds federal guidelines for energy efficiency, which means year-round energy savingsUpfront Interior analog controls for making quick adjustments to internal temperature3 fresh-food shelves provide storage for both larger items and smaller items to efficiently utilize interior capacityDoor shelves help you keep frequently used items up front for easy accessCan dispenser keeps soda cans neat and convenient3.5 cu. ft. capacity mini refrigerator is manual defrostFull width freezer compartment allows for freezing of smaller frozen food itemsInterior light for easy viewing of stored itemsWarranty is 1 Year Parts and Labor; 5 Years on compressor (parts only)This item does not qualify for the Major Appliance Delivery and Haul Away or Installation ServicesThis item does not qualify for the Major Appliance Delivery and Haul Away or Installation ServicesHome Depot Protection Plan:",
        'image_url': "https://images.app.goo.gl/o84RtpUkvQb8uYxT7"
    },
                                
    139589: {
        'name': "Sparkle Magic Red Laser Illuminator",
        'description': "The Illuminator Laser Light is the future of indoor/outdoor decorative lighting. Designed with simplicity and ease-of-use in mind, the Illuminator is a patent-pending, high tech laser light that allows you to cast dazzling, colorful lights onto any surface. The hassle-free setup allows you to install it anywhere in minutes, just remove the light from the box, attach the flexible stem and base, then plug in and point. Its as simple as that. Compared to traditional Landscaping or party lighting, the Illuminator is more energy efficient and easier to use and our patent-pending light has an adjustable dial that can produce seven different lighting effects, allowing you to change the appearance nightly. The Illuminator Laser light is ideal for weddings, holiday lighting, special occasions, or for adding a distinctive touch to any landscape. Built with quality, durable components, the Illuminator was designed from the ground up to be a lightweight and portable lighting solution. Made from aluminum casing and weighing only 3 oz., the Illuminator is designed to withstand the effects of harsh weather and is engineered to provide years of enjoyment.Significantly less than a traditional light bulb at less than 5-Watt7,000 to 10,000 hours of continuous use life spanLess than 5mW (Class 3A)Indoor/outdoor25 ft. x 25 ft. at a distance of 35 ft.Home Depot Protection Plan:",
        'image_url': "https://images.app.goo.gl/RYjizg6LN3H9HHEp7"
    },

    159041: {
        'name': "2-Handle Kitchen Faucet in Chrome",
        'description': "The Glacier Bay 2-Handle Kitchen Faucet in Chrome features a unique wall-mount design that enables you to install it regardless of your sink's existing fixture holes. Its design also saves you counterspace. This faucet is equipped with an elegant high arc spout and 7-9 in. adjustable center distance for versatile installation and hookup.Polished chrome finish to give your kitchen a clean, polished lookWall-mount design for use in sinks regardless of existing spread/fixture holes7-9 in. adjustable center distanceQuarter-turn drip-free cartridgesDual temperature controls",
        'image_url': "https://images.app.goo.gl/LjwEmYXcnZfba3xw8"
    },

    197780: {
        'name': "Hampton Bay Windward 44 in. Red Ceiling Fan",
        'description': "Modern styling and energy efficiency make the 44 in. Windward ceiling fan the perfect choice for any small room application. The Home Decorators Collection took the larger Windward IV and created a compact version without sacrificing style or function. The high efficiency blades move plenty of air and the included light kit comes with two 14-Watt CFL bulbs. Installation is a breeze with QuickInstall snap-in blades and the threaded downrod ensures stability and wobble free operation.Red finishPowerful 3-speed reversible motorFrosted white bowl light kit5 high efficiency bladesTwo 14-Watt CFL bulbs includedQuickInstall blades snap securely into place with no need for screwsQuickInstall mounting bracketConcealed hardware for added style and beautyPull chain operationDesigned for indoor use onlyCompatible with a variety of 3/4 in. extension downrods (sold separately)Compatible with LED bulbs (sold separately)Tri-mount installation (standard, close-to-ceiling, or angled mount)Lifetime limited warranty",
        'image_url': "https://images.app.goo.gl/YGsdPiSNYVfKx4EK8"
    },

    163663: {
        'name': "Philips 54-Watt 46 in. T5 Natural High Output Linear Fluorescent Light Bulb (15-Pack)",
        'description': "The Philips 54-Watt Linear Fluorescent Light Bulb is ideal for residential use in kitchens, bathrooms, garages and basements. It's also great for commercial use in medium and high-bay retail and industrial applications. It provides general room lighting, simulating a natural light and creating a lively environment, while also offering energy savings and long use.Brightness: 4800 LumensLife expectancy: 22.8 years (based on three hours/day)Light appearance: 5000K (natural)Energy used: 54-WattIdeal for residential use in laundry rooms and bathrooms, as well as for commercial use in medium and high-bay retail and industrial applicationsSimulates natural light, creating a lively environmentT5 shape, mini bi-Pin base",
        'image_url': "https://images.app.goo.gl/Ku5J4NXiniLa3qsh7"
    },

    106020: {
        'name': "Globe Electric 40-Watt Incandescent S60 E26 Vintage Edison Squirrel Cage Filament Light Bulb - Antique Edison",
        'description': "Globe Electric 01324 60-Watt S60 Vintage Squirrel Cage Incandescent Medium Base Light Bulb. This handcrafted antique style light bulb will add a vintage feel to any room. Ideal for use in exposed light fixtures, this light bulb is fully dimmable and provides a warm, pleasant light.Vintage Edison light bulb has an antique Edison color with a color temperature of 2700K, which is great to provide a warm ambient lightHandcrafted light bulb is perfect for adding a vintage feel to any room, providing a tinted and warm glowFilament light bulb has a lifespan of 3000 hours, reducing the need for frequent bulb replacementsVintage light bulb is ideal for general household use in exposed bulb lamps, wall sconces and ceiling fixturesVintage incandescent E26 base light bulb is dimmable to add desired mood and ambiance",
        'image_url': "https://images.app.goo.gl/cGmmrskDzsmTwq4D6"
    },

    126119: {
        'name': "Woods 24-Hour In-Wall Mechanical Programmable Timer - White",
        'description': "The In-Wall Mechanical Timer with Daily Settings turns indoor lighting on and off at set times. This timer is ideal for common areas in commercial and residential settings such as overhead lighting, ceiling fans, porch lighting, watering equipment or other medium-duty applications. Programming can be set in 30 minute intervals with segment pins that are permanently attached so they won't get lost. There are up to 24 on/off settings per day for flexible programming, and a manual override switch which temporarily suspends switch operation without affecting the set schedule. This 24-hour in-wall timer conveniently replaces a standard wall switch and fits a single or multi-Gang electrical box. Features also include a warm neutral color pallet to compliment any commercial or residential decor. The In-Wall Mechanical 24-Hour Timer provides added security, by programming your overhead lights to turn on while your away, making you home appear occupied and less attractive to burglars. This timer is compatible with compact fluorescent lighting (CFL), LED bulbs and CSA listed for quality assurance. The Woods brand of timers and home controls bring simplicity to your life, by maximizing convenience, security and energy savings.Up to 24 on and off settings per day, programmable in 30 minute intervals, settings repeat dailyAutomates overhead lighting, ceiling fans and porch lighting so you arrive to a safe and secure homeEasily installs in place of existing wall switchFits any single or multi-Gang decorator switch plateRatings: 125-Volt, 60 Hz/20-Amp, 2500-Watt resistive/8-Amp, 1000-Watt tungsten/8-Amp ballast/1 HP",
        'image_url': "https://images.app.goo.gl/DJmN6jki6ZNBh4SV7"
    },

    108726: {
        'name': "Home Decorators Collection Hampton Bay 44 in. Vanity in Sequoia with Granite Vanity Top in Black",
        'description': "Bring an elegant touch to your decor with this Hampton Bay bathroom vanity cabinet. You can keep your bath essentials tucked away in one of the eight drawers or center cabinet space, or on the interior shelf. This vanity features extra-dense, no-warp wood composite and wood veneer for exceptional durability and beauty. With recessed-paneling, crown moulding and bun feet, this piece was crafted with attention to detail.Includes a 3/4 in. thick hand-polished granite top and porcelain basinSingle basin44 in. W x 35 in. H x 22 in. DTwo doors and one adjustable interior shelfTwo faux decorative drawersPre-drilled holes for drain and faucet installationMinor assembly requiredConstructed of solid wood and hardwood veneerFinished backTakes a standard 8 in. 3-hole faucet set (sold separately)Drain sold separately",
        'image_url': "https://images.app.goo.gl/6iZeXGoorawDpHxT6"
    },

    124901: {
        'name': "Prime-Line Brass Victorian Glass Knob (2-Pack)",
        'description': "The Defender Security Brass Victorian Glass Knob (2-Pack) is made with a brass-plated base for a beautiful appearance. The knob handles feature a 2 in. diameter and a glass design for an elegant look.Compatible with most passage doors including older stylesGlass handled knobs feature a 2 in. diameterBrass-plated base5/16 in. square spindle shaft for simple operationIncludes 2 knobs, 1 spindle and mounting hardware",
        'image_url': "https://images.app.goo.gl/ZFdTtskwSguXwGwn6"
    },

    195894: {
        'name': "Elementz 12.5 in. x 12.5 in. Capri Azzurro Mix Glossy Glass Tile-DISCONTINUED",
        'description': "The Capri product line offers a unique, solid body, glass mosaic tile that is suitable for residential and commercial floor, wall and countertop installations. Capri is manufactured by grinding and pressing recycled glass creating a beautiful and extremely durable product suitable for heavy traffic environments. Capri is made using 95% post-consumer recycled glass content combined with an innovative, low energy production process. Available in solid colors and color mixes, glossy finish or \"grip\" finish. The optional grip finish provides enhanced slip resistance in showers, pools and other wet environments. The Capri product combines unique style with exceptional technical performance to give you the ultimate in design flexibility.First quality glass mosaic tile manufactured using 95% post-consumer recycled glass2 in. x 2 in. individual glass mosaic tiles mesh mounted on 12.5 in. x 12.5 in. x .25 in. sheetHigh gloss finish with unique color blend and slight variation in surface textureHighly resistant to abrasion and suitable for all residential and commercial applications including floor, wall and countertop installationsHighly stain resistant and easy to clean and maintainCompletely frost resistant for indoor or outdoor use1.09 sf per sheet. Sold by each sheet. 2.89 lbs per sheetDon't forget your coordinating trim pieces, grout, backerboard, thinset and installation toolsAll online orders for this item ship via parcel ground and may arrive in multiple boxesLearn how to get a Lifetime Warranty by using Custom Building Products from The Home Depot. Visit www.homedepot.com/CBPDon't forget your coordinating trim pieces, grout, backerboard, thinset and installation tools",
        'image_url': "https://images.app.goo.gl/sVV1PLQ6HgErcKRU6"
    },

    167137: {
        'name': "Everbilt Galvanized Slide Bolt",
        'description': "The Everbilt Slide Action Bolt is great for gates and sheds. Can be used in either right-handed or left-handed applications. The slide action bolt is for use on flush-mounted gates and doors. Easy to install.California residents: see&nbsp;Proposition 65 informationMade of steelGalvanized finishRust resistantScrews includedAdjustable backsetCan be used in out-swinging or in-swinging doorsCompatible with a padlock for extra security (sold separately)",
        'image_url': "https://images.app.goo.gl/vqQG4VUjvmL7f6Zd8"
    },

    192828: {
        'name': "BDK Warner Brothers Batman Steering Wheel Cover",
        'description': "BDK USA Batman steering wheel cover is colorful and durable steering wheel cover that is sure to enhance the appearance of your vehicles interior while allowing you to show off your lighter side. The steering wheel cover features and benefits are cover fits most medium size vehicles, provides comfortable grip on the steering wheel, dresses up the interior of your vehicle, easily slips over most medium size steering wheels and no tools needed.Fit most standard 14.5 in. to 15.5 in. diameter steering wheelsSoft black PU leather material with embossed Superman sidesProvides better grip and handling while drivingEasy to installOfficially licensed by Warner Brothers",
        'image_url': "https://images.app.goo.gl/rFgeLghmLpdhQSg38"
    },

    119322: {
        'name': "Nance Carpet and Rug 12 ft. x 15 ft. Beige Unbound Carpet Remnant",
        'description': "Why pay full price for carpet when you can buy a carpet remnant for half of the price? Carpet remnants provide stylish and affordable alternatives for your interior renovations. The money you save can be used for other projects. This stylish 12 ft. x 15 ft. Textured Beige Carpet Remnant is neutral and goes with virtually any design. 24 to 35 ounce face weight. The carpet remnant is unbound for wall-to-wall application. Carpet pad recommended for prolonged life and comfort. Carpet only.Textured/plush carpet materialCarpet pad recommended  (sold separately)Made in the USAWrapped in heavy-duty plastic to protect the product throughout the shipping process24 oz - 35 oz face weight",
        'image_url': "https://images.app.goo.gl/byMZ6GzLs9oTJ1uh7"
    },

    117870: {
        'name': "Prime-Line Bypass Closet Door Top-Hung Back Rollers and Brackets (2-Pack)",
        'description': "These Prime-Line Products Bypass Closet Door Top-Hung Back Rollers and Brackets (2-Pack) feature a round-edge nylon wheel fixed to an offset bracket that can adjust to fit as needed.Fits 3/4 - 1-3/8 in. by-passing closet doorsNylon wheel fixed to a steel bracket3/4 in. diameter ball bearing wheel with rounded edgeAdjustable bracket design with 1/2 in. offsetMounts easily to the side of the back by-passing door",
        'image_url': "https://images.app.goo.gl/m5RUFQ4EkxTkjWWk8"
    },

    139917: {
        'name': "Toledo Fine Locks Segovia Antique Brass Keyed Entry Lever Lockset",
        'description': "Toledo and Co. offers our customers superior quality locks made by strict specifications to ensure an outstanding security. Toledo Fine Locks is a combination of the latest technology and a traditional craftsmanship with a lifetime warranty. For added security, the entry lock set features an anti-bump key cylinder system. Toledo Fine Locks is perfect for designers and homeowners looking for alternatives that provide distinguished quality, high security, beautiful designs and fine finishes. The Antique Brass Keyed Entry Lever is a perfect blend of timeless design and classic finish. Change your home appearance with this exceptional option.Fits 1-3/8 in. to 1-3/4 in. doorsAdjustable backsetLever-styled lockset is reversibleAntique brass finish complements most home decorMeets or surpasses ANSI grade 3 standards for strength and securityADA compliantFor residential use",
        'image_url': "https://images.app.goo.gl/WFor6GU95bHdFJVi7"
    },

    188779: {
        'name': "T-Fal Total Non-Stick 8-qt. Stock Pot, Black",
        'description': "8-quart stock pot made of heavy gauge aluminum for excellent heat conduction. Durable non-stick coating on the interior and exterior for quick clean up. Ergonomic, stay-cool silicone handles; glass lid with vent hole.Non-stick inside and out for easy cooking and clean upEven heat base delivers even heat distribution for reliable cooking resultsVented glass lid maximizes visibility for optimum cooking controlSoft touch handles for comfort grippingDishwasher safeOven safe up to 350 F",
        'image_url': "https://images.app.goo.gl/R6BDhrU9kDwQ8N9E8"
    },

    149047: {
        'name': "Firebuggz 40 in. Round Fire Pit Snuffer Cover",
        'description': "The Fire Snuffer. Put out that campfire safely. Fits round fire pits up to 38 in. O.D.Stainless steel fire pit safety coverConstructed from 430 stainless steel materialHandles/slots for easy installationNew hinged style for easy storage",
        'image_url': "https://images.app.goo.gl/yjT7TQ3pBaM4fbzP6"
    },

    107093: {
        'name': "Brinkmann 6-Burner Dual Fuel Gas Grill",
        'description': "Have it all with the feature packed Brinkmann Select 6 Burner Gas Grill with Fryer, Rotisserie, and Sear-X. This versatile grill comes complete with a rotisserie kit and a 6.5 quart pot and basket for the stainless steel side burner fryer. The innovative Sear-X feature adds an additional 12,000 BTUs to a single burner for precisely one minute, providing a burst of intense heat that allows for perfect sear marks every time. Lighting this grill is easy with the electronic ignition, and the dual fuel valves allow you to easily convert from LP to natural gas. Grill a perfectly cooked meal for the whole family on 801 square inches of cooking space with 85,800 BTUs total. Complete with the thickest cast iron grates on the market, which create beautiful sear marks and make clean-up a breeze.California residents: see&nbsp;Proposition 65 information6 stainless steel burners for 60,000 BTURotisserie kit included26,000 BTU Sear X BurnerSide fryer system - 6.5 qt pot and basket includedElectronic ignitionHeavy-duty, porcelain coated cast iron cooking gratesFuel gaugeDual fuel valves for conversion to natural gasLifetime Burner WarrantyHome Depot Protection Plan:",
        'image_url': "https://images.app.goo.gl/bbKqv3FdRjRafEWC9"
    },

    174050: {
        'name': "2 gal. Deck and Home Sprayer",
        'description': "The Deck and Home Sprayer is ideal for cleaning and sealing deck`s. This sprayer can also be used as a lawn and garden applicator and for insect control. Included is a high performance foaming nozzle that produces a thick visible penetrating foam.California residents: see&nbsp;Proposition 65 information4 nozzle system-includes poly adjustable, 2 flat fans and a high performance foaming nozzle36 in. reinforced hose provides user with longer reachCustom designed shut-off with lock-on feature for continuous sprayingLarge funnel fill top",
        'image_url': "https://images.app.goo.gl/L6mPGPEEgvdNk7qo7"
    },

    114776: {
        'name': "Hembry Creek Ka Bath Suite with 36 in. Vanity in Brown Finish, White Carrara Marble Vessel Top and Charcoal-Tinted Glass Vessel Sink",
        'description': "The simple design elements of this 36 in. Ka vanity combo is inspired by ancient Japanese designs. This combo includes a rich, White Carrara Marble vessel top, pre-drilled for a vessel sink drain. A Charcoal-tinted, tempered glass vessel completes the suite. The vanity top includes a matching backsplash, and is without faucet drillings to allow for use with either wall-mounted or deck-mounted faucets.Includes adjustable leg-levelersIncludes a white carrara marble vanity top with pre-drilled vessel sink drain openingIncludes charcoal-tinted, tempered-glass round vessel sinkVanity top is without faucet drillingsMatching backsplash includedCARB compliant",
        'image_url': "https://via.placeholder.com/150"
    },

    202068: {
        'name': "Hoover 64 oz. 2X Floor Mate Multi-Floor Plus Hard Floor Cleaning Solution",
        'description': "This solution deep cleans and quickly removes stubborn everyday dirt and grime from hard floor surfaces. It's ideal for use in high traffic areas. This solution is designed to allow quick, easy and effective cleaning on sealed hard floors such as: marble, tile, wood, vinyl, laminate, granite and acrylic.Cleans sealed hard floors2X ConcentratedNew fresh linen scentImproved cleaning performance with new proprietary formula100% biodegradable and non-toxicClean for all - provides a great clean for any machine64 oz.",
        'image_url': "https://via.placeholder.com/150"
    },

    183583: {
        'name': "Nylo-Tec #10 x 2 in. Nylon White Bi-Hex Head Self Drill Screw (100 per Pack)",
        'description': "Nylo-Tec is a unique Nylon headed fastener that is a rugged, industrial screw. The specially designed head eliminates the unsightly corrosion that appears on other standard steel fasteners. The head is made to withstand the harsh environment and weather that an outdoor screw is exposed to. A perfect direct replacement for original installed fasteners on your screen enclosures, roll down shutters, sign installations and more. Use it for fastening items to metal, wood or composites.Special nylon head which will not corrodeStrong underlying carbon steel integrated fastener for maximum performanceFastener will withstand many years in harsh conditions compared to standard steel screws10 year manufacturers limited warrantyEvery Nylo-Tec utilizes the same size head, no tool swapping necessaryUnique bi-hexagonal drive affords security and aesthetic benefitsColor molded throughout head with UV stabilization for years of performance",
        'image_url': "https://via.placeholder.com/150"
    },
}


# Function to search for products


def search_products(query):
    results = {}
    for pid, prod in products.items():
        if (query.lower() in prod['name'].lower() or
            query.lower() in prod['description'].lower() or
                query.lower() in prod['image_url'].lower()):
            results[pid] = prod
    return results


# Main page function with product search and enhanced display


def main_page():
    st.title('Home Depot Shopping Platform')
    query = st.text_input('Search for products',
                          on_change=clear_product_selection)

    if query:
        results = search_products(query)
        if results:
            for product_id, product in results.items():
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.image(product['image_url'], width=100)
                with col2:
                    st.subheader(product['name'])
                    if st.button('View', key=product_id):
                        st.session_state['product_id'] = product_id
                        st.session_state['navigation'] = 'Product Details'
                        st.experimental_rerun()
        else:
            st.warning(
                "No products found matching your search. Please try again with a different query.")

# Helper function to clear product selection when initiating a new search


def clear_product_selection():
    if 'product_id' in st.session_state:
        del st.session_state['product_id']

# Product details page function


def product_page(product_id):
    product = products[product_id]
    st.title(product['name'])
    st.image(product['image_url'], width=150)
    st.write(product['description'])
    # if st.button('Add to Cart'):
    #     st.success('Product added to cart!')


# Initialize session state for navigation
if 'navigation' not in st.session_state:
    st.session_state['navigation'] = 'Home'

# Sidebar navigation setup
st.sidebar.title("Navigation")
st.sidebar.radio("Go to", ('Home', 'Product Details'),
                 index=0 if st.session_state['navigation'] == 'Home' else 1)

# Conditional rendering based on navigation state
if st.session_state['navigation'] == 'Home':
    main_page()
elif st.session_state['navigation'] == 'Product Details' and 'product_id' in st.session_state:
    product_page(st.session_state['product_id'])
else:
    st.session_state['navigation'] = 'Home'
    st.experimental_rerun()
