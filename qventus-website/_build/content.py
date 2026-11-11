"""All website copy lives here. Edit text in this file, then run:  python3 _build/build.py"""

# ---------------------------------------------------------------- company details
SITE_URL = "https://www.qventus.qa"
COMPANY = "Q Ventus"
EMAIL = "inquiry@qventus.qa"
# Phone numbers exactly as printed in the company profile.
PHONE_1 = "+974 6649 1649"
PHONE_1_LINK = "+97466491649"
PHONE_2 = "+974 5066 0546"
PHONE_2_LINK = "+97450660546"
WHATSAPP = "97466491649"           # digits only, used for wa.me links
# Enquiry form: submissions are delivered to EMAIL via FormSubmit (formsubmit.co).
# The first submission triggers a one-time activation email to EMAIL that must be confirmed.
FORM_ENDPOINT = "https://formsubmit.co/ajax/" + "inquiry@qventus.qa"
ADDRESS = "Office 81, Zone E, Al Mirqab Mall, Doha, Qatar"
MAP_QUERY = "Al Mirqab Mall, Doha, Qatar"
HOURS = [("Every day, including holidays", "Open 24 / 7")]
ISO = [
    ("ISO 9001:2015", "Quality Management", "Documented, audited processes for consistent engineering quality from survey to handover."),
    ("ISO 45001:2018", "Occupational Health & Safety", "Safety management embedded in every site, plant room and offshore operation we work in."),
    ("ISO 14001:2015", "Environmental Management", "Responsible refrigerant handling, waste control and energy-conscious engineering."),
]
STATS = [("15", "+", "Years of expertise"), ("100", "+", "Projects delivered"), ("60", "+", "Corporate clients"), ("98", "%", "Client satisfaction")]

CLIENTS = [
    ("halliburton.png", "Halliburton"), ("milaha.jpg", "Milaha"), ("weatherford.jpg", "Weatherford"),
    ("akh.jpg", "Aspire Katara Hospitality"), ("gl-events.png", "GL events"), ("flow.jpg", "Flow"),
    ("regency.jpg", "Regency Group Holding"), ("ramada.png", "Ramada by Wyndham"), ("edge.png", "Edge Fitness"),
    ("al-emadi.jpg", "Al Emadi Hospital"), ("baladna.png", "Baladna"),
]

# ---------------------------------------------------------------- services
# group: hvac | systems | support | secondary
SERVICES = [
    dict(
        slug="commercial-hvac", group="hvac", icon="building", img="cassette-unit",
        name="Commercial HVAC",
        card="Chilled water, VRF/VRV, package and ducted systems for offices, hotels, retail and hospitals.",
        title="Commercial HVAC Engineering & Maintenance in Qatar",
        desc="Commercial HVAC engineering in Doha: chillers, AHUs, VRF/VRV, package rooftop units and cooling towers installed, commissioned and maintained by certified Q Ventus engineers.",
        h1="Commercial HVAC Engineering for Buildings That Can't Afford Downtime",
        lead="Reliable, energy-efficient commercial air conditioning built for performance, comfort and control — engineered, installed, commissioned and maintained by one accountable team.",
        chips=["Chilled water", "VRF / VRV", "Package rooftop units", "Ducted AHUs", "Cooling towers"],
        body=[
            "Hotels, hospitals, offices and retail centres in Qatar run their cooling plant close to full load for most of the year. When a system underperforms, guests notice, clinical spaces drift out of specification and tenants complain. Q Ventus approaches commercial HVAC as an engineering discipline: we start from the heat load and the duty the building actually sees, then select, install and maintain equipment to hold that duty reliably.",
            "Our teams work across the full commercial plant — from rooftop package units and ducted air handling units to air-cooled and water-cooled chiller systems, cooling towers and chilled water circulation pumps — including dedicated medical process chillers for MRI scanners in healthcare facilities (see our MRI & medical chiller service).",
        ],
        scope=["Package rooftop units (RTUs)", "Ducted air handling units", "Air-cooled & water-cooled chillers", "Cooling towers", "Chilled water circulation pumps", "MRI & medical process chillers", "VRF / VRV systems", "Cassette, ducted & floor-standing units"],
        table=[("Building types", "Hotels, hospitals, offices, malls, restaurants, fitness centres"), ("Service model", "Design · Supply · Install · Commission · AMC"), ("Typical works", "New installations, plant replacement, retrofits, performance upgrades"), ("Support", "Preventive maintenance and 24/7 breakdown response")],
        project="chiller-plant-hotel", related=["chiller-services", "preventive-maintenance", "hvac-design-engineering"],
    ),
    dict(
        slug="industrial-hvac", group="hvac", icon="factory", img="condenser-bank",
        name="Industrial HVAC",
        card="Chiller plants, AHUs, FCUs, FAHUs and ventilation for plants, warehouses and process areas.",
        title="Industrial HVAC Systems & Ventilation in Qatar",
        desc="Industrial HVAC in Qatar: chiller plants, AHUs, FCUs, fresh air handling units and ventilation systems engineered for continuous duty in harsh conditions.",
        h1="Industrial HVAC Engineered for Continuous Duty",
        lead="Cooling and ventilation systems for industrial facilities where temperature, air quality and uptime directly affect production and safety.",
        chips=["Chiller plants", "AHU / FCU / FAHU", "Ventilation", "Pumps & motors"],
        body=[
            "Industrial environments push HVAC equipment harder than any office building: high ambient temperatures, dust, heat-generating processes and 24-hour operation. Q Ventus designs and maintains systems that are sized for that reality, with the redundancy and serviceability that industrial operators need.",
            "Beyond installation, our in-house mechanical capability — motor rewinding, pump overhauling and compressor overhauling — means we can restore critical rotating equipment rather than wait for replacement parts, reducing downtime for our industrial clients.",
        ],
        scope=["Chiller plants", "Air handling units (AHU)", "Fan coil units (FCU)", "Fresh air handling units (FAHU)", "Industrial ventilation & extraction", "Cooling towers & pumps", "Motor, pump & compressor overhauls", "Industrial air filtration"],
        table=[("Facilities", "Manufacturing, warehouses, workshops, utilities, process areas"), ("Conditions", "High ambient, dust-laden air, continuous operation"), ("Engineering", "Heat load, airflow and ventilation-rate design"), ("Support", "Planned maintenance programmes and rapid emergency response")],
        project="offshore-pressurized", related=["mechanical-overhauling", "air-quality-filtration", "preventive-maintenance"],
    ),
    dict(
        slug="offshore-hvac", group="hvac", icon="rig", img="offshore-platform",
        name="Offshore HVAC",
        card="Offshore cabin HVAC, pressurized modules and chiller plants by QP/QG safety-certified teams.",
        title="Offshore HVAC for Oil & Gas Platforms in Qatar",
        desc="Offshore HVAC engineering for oil & gas platforms: cabin air conditioning, pressurized containers, chiller plants, AHU, FCU and FAHU by QP and QG safety-certified technicians.",
        h1="Offshore HVAC for Oil & Gas Platforms",
        lead="Specialised HVAC solutions for harsh offshore environments, delivered by technicians certified and trained to Qatar Petroleum standards.",
        chips=["Offshore cabin HVAC", "Pressurized modules", "Chiller plants", "AHU · FCU · FAHU", "QP & QG certified"],
        body=[
            "On an offshore platform, HVAC is not a comfort system — it protects people, control equipment and the integrity of pressurized accommodation and control modules. A failure can stop operations. Q Ventus brings strong expertise in offshore cabin air conditioning engineering and installation, with a focus on precision, safety and compliance.",
            "Our offshore personnel hold QP and QG approved safety training. We engineer upgrades for pressurized containers that must maintain positive pressure in high ambient temperatures, and we maintain chiller plants, AHUs, FCUs, FAHUs and ventilation systems on operating facilities.",
        ],
        scope=["Offshore cabin HVAC", "Pressurized container HVAC", "Chiller plants", "AHU, FCU & FAHU", "Ventilation systems", "Engineering assessments & redesign", "Commissioning & performance testing", "Certified offshore manpower"],
        table=[("Approvals", "QP and QG approved safety-training-certified manpower"), ("Environment", "Salt-laden air, high ambient, vibration, hazardous areas"), ("Scope", "Engineering, upgrades, installation, maintenance, manpower supply"), ("Related", "Offshore containers & accommodation modules")],
        project="offshore-pressurized", related=["offshore-containers", "technical-manpower", "marine-hvac"],
    ),
    dict(
        slug="marine-hvac", group="hvac", icon="anchor", img="marine-yacht",
        name="Marine HVAC",
        card="Chilled water systems, self-contained units, cabin AC and marine refrigeration for vessels.",
        title="Marine HVAC & Yacht Air Conditioning in Qatar",
        desc="Marine air conditioning in Qatar: chilled water systems, self-contained units, cabin AC and marine refrigeration for yachts and vessels. Installation, retrofit and repair.",
        h1="Marine Air Conditioning, Engineered for Life at Sea",
        lead="Professional service and specialised advice for the installation and repair of nautical and land equipment — engineered for reliability, corrosion resistance and uninterrupted performance at sea.",
        chips=["Chilled water systems", "Self-contained units", "Cabin AC", "Marine refrigeration"],
        body=[
            "Marine HVAC operates under continuous vibration, high humidity, corrosive salt air and tight machinery spaces — while guests and crew still expect precise comfort. Q Ventus engineers marine systems with those constraints in mind, from component selection to installation practice and commissioning.",
            "We have completed full chilled water plant retrofits on luxury superyachts, including chiller replacement, complete AHU replacement and dual-station monitoring from the engine room and bridge.",
        ],
        scope=["Self-contained marine AC units", "Chilled water systems", "Cabin air conditioning", "Marine refrigeration", "Marine AHU replacement", "Monitoring & control systems", "Retrofits & upgrades", "Repair & preventive maintenance"],
        table=[("Vessels", "Superyachts, workboats, commercial and offshore vessels"), ("Typical works", "Chiller replacement, AHU replacement, controls upgrades"), ("Design focus", "Corrosion resistance, vibration, serviceability"), ("Support", "Breakdown response and planned maintenance")],
        project="superyacht-retrofit", related=["offshore-hvac", "commercial-refrigeration", "preventive-maintenance"],
    ),
    dict(
        slug="commercial-refrigeration", group="hvac", icon="snow", img="cold-room",
        name="Commercial Refrigeration",
        card="Blast chillers, walk-in chillers and freezers, display cabinets and beverage coolers.",
        title="Commercial Refrigeration Systems in Qatar",
        desc="Commercial refrigeration in Doha: blast chillers, cold rooms, walk-in chillers and freezers, island freezers, display cabinets and beverage coolers — design, installation and maintenance.",
        h1="Commercial Refrigeration That Protects Your Cold Chain",
        lead="Q Ventus designs, fabricates and installs custom cold storage solutions for warehouses, restaurants, supermarkets and kitchens — backed by reliable repair and maintenance services.",
        chips=["Blast chillers", "Cold rooms", "Walk-in chiller / freezer", "Island freezers", "Display cabinets", "Beverage coolers"],
        body=[
            "When refrigeration fails, stock is lost within hours. We treat commercial refrigeration as a critical system: correctly sized condensing units and evaporators, properly installed insulated panels and doors, reliable door heaters and pressure relief valves, and controls that hold temperature.",
            "Where systems must stay online during upgrades, we plan phased replacements and can arrange temporary refrigerated (reefer) units so the cold chain is never broken.",
        ],
        scope=["Blast chillers & blast freezers", "Cold rooms", "Walk-in chillers & freezers", "Island freezers", "Display cabinets", "Beverage coolers", "Condensing unit & evaporator replacement", "Door heaters & pressure relief valves"],
        table=[("Clients", "Hotels, restaurants, supermarkets, food processors, warehouses"), ("Temperatures", "Chilled storage to −22 °C frozen storage and blast freezing"), ("Continuity", "Phased works with temporary reefer backup"), ("Support", "AMC and breakdown service")],
        project="cold-storage", related=["cold-rooms", "preventive-maintenance", "marine-hvac"],
    ),
    dict(
        slug="hvac-design-engineering", group="hvac", icon="drawing", img="duct-shop-drawing",
        name="HVAC Design & Engineering",
        card="Heat load calculation, HVAC-R design, equipment selection and shop drawings.",
        title="HVAC Design, Heat Load Calculation & Shop Drawings | Qatar",
        desc="HVAC design and engineering in Qatar: heat load calculations, HVAC-R system design, equipment selection and shop drawings for commercial, industrial and offshore projects.",
        h1="HVAC Design & Engineering, From Heat Load to Shop Drawing",
        lead="Every reliable system starts on paper. Our engineers size, select and detail HVAC-R systems so that what gets installed performs as intended.",
        chips=["Heat load calculation", "HVAC-R design", "Equipment selection", "Shop drawings"],
        body=[
            "Oversized equipment short-cycles and wastes energy; undersized equipment never catches up in a Qatari summer. Our design work starts with an accurate heat load calculation and carries through system selection, duct and pipe design, and coordinated shop drawings ready for installation.",
            "Because our engineers also commission and maintain what they design, our drawings reflect how systems are actually built and serviced — access, maintainability and redundancy are designed in from day one.",
        ],
        scope=["Heat load calculation", "HVAC-R system design", "Equipment selection", "Duct & pipe sizing", "Shop drawings", "Retrofit & upgrade engineering", "Site surveys & assessments", "Commissioning plans"],
        process=[("Survey", "Site inspection, existing system review and operating requirements."), ("Calculate", "Heat load, airflow and refrigeration capacity calculations."), ("Select", "Equipment selection against duty, efficiency and serviceability."), ("Detail", "Shop drawings, schedules and installation details."), ("Verify", "Commissioning, balancing and performance verification.")],
        project="superyacht-retrofit", related=["commercial-hvac", "industrial-hvac", "chiller-services"],
    ),
    dict(
        slug="preventive-maintenance", group="hvac", icon="wrench", img="technicians",
        name="Preventive Maintenance & Emergency Support",
        card="AMC programmes, planned maintenance, duct and coil cleaning, and 24/7 breakdown response.",
        title="HVAC Preventive Maintenance & AMC Contracts in Qatar",
        desc="HVAC preventive maintenance and annual maintenance contracts (AMC) in Qatar, with 24/7 emergency breakdown support for chillers, AHUs, refrigeration and offshore systems.",
        h1="Preventive Maintenance That Keeps Critical Systems Running",
        lead="Planned maintenance programmes and annual maintenance contracts that extend equipment life, reduce breakdowns and protect your operation — backed by rapid emergency response.",
        chips=["AMC contracts", "Planned preventive maintenance", "Breakdown service", "24/7 emergency"],
        body=[
            "The cheapest breakdown is the one that never happens. Our preventive maintenance programmes are built around your equipment and your operating hours, covering inspections, cleaning, refrigerant and electrical checks, performance logging and early fault detection.",
            "When something does fail, our rapid-response technicians diagnose and correct faults quickly — on land, at sea and offshore.",
        ],
        scope=["Annual maintenance contracts (AMC)", "Planned preventive maintenance (PPM)", "Breakdown & corrective maintenance", "Duct cleaning", "Filter replacement", "Coil cleaning", "Performance inspections", "Standby technical teams"],
        extra="emergency",
        project="chiller-plant-hotel", related=["chiller-services", "commercial-refrigeration", "air-quality-filtration"],
    ),
    dict(
        slug="chiller-services", group="systems", icon="chiller", img="commercial-rooftop-plant",
        name="Chiller Systems & Cooling Towers",
        card="Air-cooled and water-cooled chiller replacement, commissioning and AMC.",
        title="Chiller Maintenance, Replacement & Cooling Tower Services | Qatar",
        desc="Chiller services in Qatar: air-cooled and water-cooled chiller replacement, commissioning, maintenance and AMC, cooling towers and chilled water pumps.",
        h1="Chiller Plant Services: Replacement, Commissioning & Maintenance",
        lead="The chiller plant is the heart of a commercial building. We help keep it efficient, reliable and supported for the long term.",
        chips=["Air-cooled chillers", "Water-cooled chillers", "Cooling towers", "CHW pumps", "AMC"],
        body=[
            "Ageing chillers cost more to run, break down more often and put guest or occupant comfort at risk. Q Ventus supports chiller replacement programmes from decommissioning through to commissioning and performance verification, then keeps the new plant performing through structured preventive maintenance.",
            "We work on air-cooled and water-cooled chillers, cooling towers, chilled water circulation pumps and the controls that tie the plant together — including mobile chillers for temporary cooling.",
        ],
        scope=["Air-cooled chillers", "Water-cooled chillers", "Mobile / temporary chillers", "Cooling towers", "Chilled water pumps", "Decommissioning & replacement", "Commissioning & performance testing", "Chiller AMC"],
        project="chiller-plant-hotel", related=["commercial-hvac", "preventive-maintenance", "hvac-design-engineering"],
    ),
    dict(
        slug="cold-rooms", group="systems", icon="snow", img="cold-storage",
        name="Cold Rooms & Blast Freezers",
        card="Custom-built cold rooms, freezer rooms and blast freezers for food and logistics.",
        title="Cold Rooms, Freezer Rooms & Blast Freezers in Qatar",
        desc="Custom cold room and freezer room construction in Qatar: insulated panels, condensing units, evaporators, blast freezers, door heaters and maintenance.",
        h1="Cold Rooms & Blast Freezers, Designed and Built to Hold Temperature",
        lead="Custom cold storage for warehouses, hotels, restaurants, supermarkets and food processors — designed, fabricated, installed and maintained by Q Ventus.",
        chips=["Cold rooms", "Freezer rooms", "Blast freezers", "Walk-in units"],
        body=[
            "A cold room is only as good as its weakest component: panels, doors, door heaters, pressure relief valves, evaporators and condensing units all have to work together. We design and build complete cold storage rooms and modernise existing ones, with stable temperatures down to −22 °C for frozen storage.",
            "Upgrades can be phased with temporary reefer units on rental so stored product stays at temperature throughout the works.",
        ],
        scope=["Cold room design & fabrication", "Freezer rooms (to −22 °C and below)", "Blast freezers & blast chillers", "Insulated doors & panels", "Door heater systems", "Pressure relief valves", "Condensing units & evaporators", "Temporary reefer backup"],
        project="cold-storage", related=["commercial-refrigeration", "preventive-maintenance", "industrial-hvac"],
    ),
    dict(
        slug="mri-medical-chillers", group="systems", icon="thermo", img="condenser-bank",
        name="MRI & Medical Process Chillers",
        card="Supply, installation and 24/7 maintenance of MRI and diagnostic imaging chillers.",
        title="MRI Chiller Supplier & Medical Process Chiller Maintenance in Qatar",
        desc="MRI chiller supplier in Qatar: medical process chillers for MRI, CT and LINAC — supply, installation, AMC and 24/7 emergency maintenance in Doha, rated for 52 °C ambient.",
        h1="Medical Process Chillers & MRI Cooling Solutions",
        lead="Precision cooling supply, installation and 24/7 maintenance for healthcare facilities in Qatar — engineered to OEM specifications and rated for extreme Gulf ambient temperatures.",
        chips=["MRI · CT · LINAC", "Up to 52 °C ambient", "Dual-circuit redundancy", "BMS integration", "24/7 AMC"],
        body=[
            "Diagnostic imaging equipment — MRI scanners, CT systems and linear accelerators — requires uninterrupted, precision thermal management. Even a brief cooling interruption can cause costly scanner downtime or a critical helium quench.",
            "Q Ventus provides end-to-end supply, installation and preventive maintenance of dedicated medical process chillers across Doha and Qatar. Our systems are engineered to meet strict OEM flow, pressure and temperature tolerances and to perform reliably in Gulf summers of 50–52 °C ambient.",
        ],
        cols=[
            ("Supply & Turnkey Installation", [
                "OEM-compatible air-cooled and water-cooled medical chillers, sized to the thermal load of leading imaging platforms including Siemens, GE HealthCare, Philips and Canon.",
                "High-ambient rated systems for continuous 24/7 operation in summer conditions up to 52 °C.",
                "Built-in redundancy: dual-pump configurations, dual refrigeration circuits and automatic city-water bypass panels for zero-downtime protection.",
                "Complete hydronic integration: insulated buffer tanks, glycol loops, precision flow controls and BMS alarm integration.",
            ]),
            ("Preventive Maintenance (AMC)", [
                "Scheduled inspection of compressors, refrigerant pressures and condenser coils.",
                "Water quality, glycol concentration and flow / temperature sensor checks.",
                "Technicians following biomedical infrastructure protocols — not standard comfort-cooling routines.",
                "Annual Maintenance Contracts built around your scanner's uptime requirements.",
            ]),
            ("24/7 Emergency & Spares", [
                "Rapid on-site dispatch across Qatar under agreed Service Level Agreements (SLAs).",
                "Protection of MRI cold-head and gradient cooling systems.",
                "Genuine replacement pumps, controllers and heat exchangers.",
                "Retrofits and upgrades for ageing imaging chillers.",
            ]),
        ],
        scope=["OEM-compliant flow, pressure & temperature tolerances", "Local Qatar presence and fast response", "Thermal load sizing to commissioning to AMC — one partner", "Dual pumps & dual refrigeration circuits", "Automatic city-water bypass panels", "BMS alarm integration"],
        scope_title="Why healthcare facilities partner with us",
        table=[("Equipment served", "MRI scanners, CT systems, linear accelerators (LINAC)"), ("Imaging platforms", "Siemens, GE HealthCare, Philips, Canon"), ("Chiller types", "Air-cooled and water-cooled medical process chillers"), ("Design ambient", "Up to 52 °C, continuous 24/7 duty"), ("Service model", "Supply · Install · Commission · AMC · 24/7 emergency")],
        cta=("Request a technical consultation or AMC quote", "Talk to our medical cooling team about a new chiller, a replacement or an Annual Maintenance Contract.", "Contact Our Medical Cooling Team", "Request an AMC Proposal"),
        project=None, related=["chiller-services", "preventive-maintenance", "commercial-hvac"],
    ),
    dict(
        slug="air-quality-filtration", group="systems", icon="filter", img="air-filters",
        name="Air Quality & Filtration",
        card="Fabrication and supply of pre, fine, HEPA and bag filters, plus duct and coil cleaning.",
        title="Air Filter Fabrication & Indoor Air Quality Solutions | Qatar",
        desc="Air filter fabrication and supply in Qatar: pre-filters, fine filters, HEPA filters, bag filters and custom filtration for AHUs, plus duct and coil cleaning.",
        h1="Air Filtration & Indoor Air Quality Solutions",
        lead="Q Ventus specialises in the fabrication and supply of all types of air filters for air conditioning systems and Air Handling Units, for residential, commercial and industrial applications.",
        chips=["Pre-filters", "Fine filters", "HEPA filters", "Bag filters", "Custom filtration"],
        body=[
            "Correct filtration protects both people and plant: it keeps indoor air clean, protects coils and fans from dust, and preserves system efficiency. Our range includes pre-filters, fine filters, HEPA filters, bag filters and customised filtration solutions designed for specific operational and environmental requirements.",
            "We combine filter supply with duct cleaning and coil cleaning services, so the whole air path is restored — not just the filter bank.",
        ],
        scope=["Pre-filters", "Fine filters", "HEPA filters", "Bag filters", "Custom filter fabrication", "AHU filter replacement programmes", "Duct cleaning", "Coil cleaning"],
        project=None, related=["preventive-maintenance", "industrial-hvac", "commercial-hvac"],
    ),
    dict(
        slug="mechanical-overhauling", group="systems", icon="gear", img="compressor-overhaul",
        name="Motor, Pump & Compressor Overhauling",
        card="Motor rewinding, pump overhauls and compressor overhauls to restore critical equipment.",
        title="Motor Rewinding, Pump & Compressor Overhauling in Qatar",
        desc="Motor rewinding, pump overhauling and compressor overhauling services in Qatar for HVAC, marine, industrial and oil & gas applications.",
        h1="Motor Rewinding, Pump & Compressor Overhauling",
        lead="Restore performance and extend the life of critical rotating equipment across HVAC, refrigeration, marine and oil & gas applications.",
        chips=["Motor rewinding", "Pump overhauling", "Compressor overhauling"],
        body=[],
        blocks=[
            ("motor-rewinding", "Motor Rewinding Services", "Our motor rewinding services restore performance and extend the lifespan of electric motors across industrial and commercial applications. We carry out complete inspection, fault diagnosis, coil rewinding, insulation replacement and testing using high-quality materials and industry-standard techniques, with precise rewinding and balancing for efficiency and long-term reliability under demanding conditions."),
            ("pump-overhaul", "Pump Overhauling Services", "Our pump overhauling covers a wide range of centrifugal and industrial pumps used in HVAC, marine and oil & gas applications. We conduct detailed inspection, disassembly, component repair or replacement, seal and bearing servicing, and full reassembly with testing — restoring pumps to optimal performance, efficiency, reliability and operational safety."),
            ("compressor-overhaul", "Compressor Overhauling Services", "Q Ventus provides comprehensive compressor overhauling for HVAC and refrigeration systems: complete dismantling, inspection, replacement of worn components, reassembly and performance testing. We specialise in preventive and corrective overhauls that minimise downtime, improve operational efficiency and extend equipment life."),
        ],
        scope=["Fault diagnosis & inspection", "Coil rewinding & insulation", "Dynamic balancing", "Seal & bearing servicing", "Component repair / replacement", "Reassembly & performance testing"],
        project=None, related=["industrial-hvac", "chiller-services", "preventive-maintenance"],
    ),
    dict(
        slug="offshore-containers", group="support", icon="container", img="container-sleeper",
        name="Offshore Containers",
        card="DNV 2.7-1 certified offshore containers, skips and accommodation modules.",
        title="Offshore Containers & Accommodation Modules (DNV 2.7-1) | Qatar",
        desc="Offshore container supply and rental in Qatar: DNV 2.7-1 / EN 12079 certified cargo containers, open-top and waste skips, sleeper, recreation and office modules.",
        h1="Certified Offshore Containers & Accommodation Modules",
        lead="Fully certified offshore units built to stringent standards — for oil & gas platforms, drilling rigs and offshore projects, with flexible supply and rental options.",
        chips=["DNV 2.7-1", "EN 12079", "IMO", "SOLAS A60", "ATEX Zone 2"],
        body=[
            "Our offshore container fleet is designed for durability, safety and reliability in harsh marine environments. With a range of container types available, we provide flexible supply and rental solutions tailored to your operational requirements.",
        ],
        containers=[
            ("container-closed", "20' Offshore Container — New & Used", [("Use", "Safe, flexible storage and transport"), ("Build", "Harsh-condition construction, customisable sizes"), ("Cert.", "DNV 2.7-1 available")]),
            ("container-skip", "Open-Top, Basket & Waste Skips", [("Design temp.", "−20 °C to +30 °C"), ("Hazardous area", "Zone 2 (ATEX gas group IIB-T3)"), ("Cert.", "EN 12079, DNV 2.7-1, IMO, SOLAS (A60)")]),
            ("container-sleeper", "20' Sleeper Module (4 persons)", [("Design temp.", "−10 °C to +50 °C"), ("Hazardous area", "Zone 2 (ATEX gas group IIB-3G)"), ("Cert.", "EN 12079, DNV 2.7-1, IMO, SOLAS (A60)")]),
            ("container-sleeper", "20' Recreation Module", [("Design temp.", "−10 °C to +50 °C"), ("Hazardous area", "Zone 2 (ATEX gas group IIB-3G)"), ("Cert.", "EN 12079, DNV 2.7-1, IMO, SOLAS (A60)")]),
            ("container-sleeper", "20' Office Module", [("Design temp.", "−20 °C to +50 °C"), ("Hazardous area", "Zone 2 (ATEX gas group IIB-T3)"), ("Cert.", "EN 12079, DNV 2.7-1, IMO, SOLAS (A60)")]),
        ],
        scope=["Certified lifting slings supplied as standard", "New and used units", "Supply and rental", "Custom configurations", "DNV · LR · ABS · BV · EN 12079 certified units"],
        project="offshore-pressurized", related=["offshore-hvac", "technical-manpower", "event-support"],
    ),
    dict(
        slug="event-support", group="support", icon="event", img="exhibition-hall",
        name="Event Support",
        card="Temporary HVAC, cooling, generator and on-site technical teams for events and exhibitions.",
        title="Temporary HVAC & Technical Event Support in Qatar",
        desc="Temporary HVAC, cooling and generator support for events, exhibitions and temporary installations in Qatar. Proven at FIFA World Cup Qatar 2022 venues.",
        h1="Temporary HVAC & Technical Support for Events",
        lead="Specialised manpower and cooling support for events, exhibitions and temporary installations — ensuring seamless technical operations in time-critical environments.",
        chips=["Temporary HVAC", "Tents & halls", "Generators", "Standby teams", "FIFA 2022 experience"],
        body=[
            "We support event organisers, production companies and facility managers with skilled technicians who handle HVAC systems, temporary power set-ups and emergency maintenance. During FIFA World Cup Qatar 2022 we deployed around 50 engineers and technicians across multiple tournament venues.",
        ],
        cols=[
            ("HVAC & Cooling Support", ["Installation and monitoring of temporary HVAC systems", "Cooling for tents, halls and outdoor set-ups", "Emergency troubleshooting and repair", "Air distribution and ventilation optimisation"]),
            ("Electrical & Generator Support", ["Generator technicians for set-up and operation", "Temporary electrical support for event facilities", "Load monitoring and system stability management"]),
            ("On-Site Technical Teams", ["HVAC technicians", "Generator technicians", "Electricians", "Mechanical support technicians", "Standby emergency response teams"]),
        ],
        scope=["Rapid response & standby support", "Flexible, scalable workforce", "Experience in temporary installations", "Minimised downtime", "Safety & compliance", "Full decommissioning after the event"],
        project="fifa-2022", related=["technical-manpower", "chiller-services", "preventive-maintenance"],
    ),
    dict(
        slug="technical-manpower", group="support", icon="people", img="site-team",
        name="Skilled Technical Manpower",
        card="QP & QG safety-certified HVAC technicians, welders, painters and cleaners.",
        title="Offshore & Onshore Technical Manpower Supply in Qatar",
        desc="Skilled technical manpower in Qatar: QP and QG approved safety-certified HVAC technicians, offshore welders, painters and cleaners for oil & gas and industrial projects.",
        h1="Skilled Technical Manpower, Provided Responsibly",
        lead="Certified personnel for offshore oil & gas platforms and onshore projects — with QP and QG approved safety training.",
        chips=["HVAC technicians", "Welders", "Painters", "Cleaners", "QP & QG certified"],
        body=[
            "Behind every project is a team of professionals, engineers and technicians, each vital to safe, timely delivery. We invest in our people through fair wages, training and safety systems — because that is what makes a workforce reliable.",
        ],
        cols=[
            ("HVAC Technicians", ["Reliable climate control, maintenance and efficient system performance on offshore oil & gas platforms."]),
            ("Welders", ["Skilled offshore welders delivering precise, high-strength fabrication and repair work in compliance with strict safety and industry standards."]),
            ("Painters", ["Certified offshore painters providing protective coating and corrosion control for long-lasting structural integrity in harsh marine environments."]),
            ("Cleaners", ["Professional cleaning personnel maintaining high hygiene and safety standards across oil & gas platforms for smooth, compliant operations."]),
        ],
        scope=["QP & QG approved safety training", "Offshore & onshore deployment", "Short-term and long-term contracts", "Shutdown & turnaround support"],
        project="fifa-2022", related=["offshore-hvac", "offshore-containers", "event-support"],
    ),
    dict(
        slug="residential-hvac", group="secondary", icon="home", img="residential-villas",
        name="Residential & Villa HVAC",
        card="Air conditioning, water cooling and maintenance for villas, compounds and apartment buildings.",
        title="Villa & Residential Air Conditioning in Qatar",
        desc="Residential air conditioning in Qatar for villas, compounds and apartment buildings: split, ducted and VRF systems, tank chillers, duct cleaning and AMC contracts.",
        h1="Residential & Villa Air Conditioning",
        lead="Complete air conditioning solutions for apartment buildings, villas and residential compounds — including new installations and maintenance of existing systems.",
        chips=["Inverter technology", "Smart features", "Tropicalised T3 ACs"],
        body=[
            "We bring the same engineering approach we use on commercial and offshore projects to residential buildings: correct sizing, quality installation and dependable maintenance, with minimal disruption to your living space.",
        ],
        cols=[
            ("Air Conditioning", ["Split AC units (up to 10 TR)", "Multi-split systems", "VRF / VRV systems", "Cassette units", "Ducted units", "Floor-standing units", "Package units"]),
            ("Indoor Air Quality", ["Duct cleaning", "Filter replacement", "Coil cleaning"]),
            ("Water Cooling & Maintenance", ["Tank chillers", "Villa cooling systems", "AMC contracts", "Breakdown service"]),
        ],
        scope=[],
        project=None, related=["preventive-maintenance", "air-quality-filtration", "commercial-hvac"],
    ),
]

GROUPS = [
    ("hvac", "G-01", "HVAC Engineering", "Engineered heating, ventilation, air conditioning and refrigeration for commercial, industrial, offshore and marine facilities."),
    ("systems", "G-02", "Specialized Systems", "Deep expertise in the equipment that critical facilities depend on — and the mechanical capability to restore it."),
    ("support", "G-03", "Industrial Support", "Certified offshore containers, event infrastructure support and skilled technical manpower."),
]

# Systems listed in the "Specialized Systems" group card (label, link slug)
SYSTEM_LINKS = [
    ("Chiller Systems", "chiller-services"), ("Cooling Towers", "chiller-services"), ("AHUs & FCUs", "industrial-hvac"),
    ("Cold Rooms", "cold-rooms"), ("Blast Chillers", "commercial-refrigeration"), ("VRF / VRV & Package Units", "commercial-hvac"),
    ("MRI & Medical Process Chillers", "mri-medical-chillers"), ("Air Quality Solutions", "air-quality-filtration"), ("Motor, Pump & Compressor Overhauls", "mechanical-overhauling"),
]

CAPABILITIES = [
    ("chiller", "Chillers", "Air-cooled, water-cooled and mobile chillers"),
    ("tower", "Cooling Towers", "Condenser water and heat rejection"),
    ("ahu", "AHUs", "Air handling and fresh air handling units"),
    ("fcu", "FCUs", "Fan coil units and terminal systems"),
    ("package", "Package Units", "Packaged DX air conditioning"),
    ("rooftop", "Rooftop Units", "Package rooftop units (RTU)"),
    ("vrf", "VRF / VRV Systems", "Variable refrigerant flow systems"),
    ("thermo", "Precision Cooling", "MRI & medical process chillers"),
    ("snow", "Cold Rooms", "Chiller and freezer rooms to −22 °C"),
    ("blast", "Blast Freezers", "Blast chillers and rapid freezing"),
    ("anchor", "Marine HVAC", "Chilled water and self-contained marine AC"),
    ("fan", "Ventilation Systems", "Supply, extract and pressurization"),
]

INDUSTRIES = [
    ("building", "Commercial Buildings"), ("bed", "Hotels & Hospitality"), ("health", "Healthcare"),
    ("factory", "Industrial Facilities"), ("server", "Data Centers"), ("anchor", "Marine"),
    ("rig", "Oil & Gas"), ("gov", "Government"), ("food", "Food Processing"),
    ("warehouse", "Warehouses"), ("plane", "Airports"), ("edu", "Educational Institutions"),
]

WHY = [
    ("Engineering-Led Solutions", "Every job starts with engineering — heat loads, duty and risk — not with a sales catalogue."),
    ("Qualified & Certified Technicians", "Trained, certified teams, including QP and QG safety-certified offshore personnel."),
    ("Commercial & Industrial Specialists", "Focused on facilities where cooling is critical to operations, not just comfort."),
    ("Offshore HVAC Expertise", "Proven on pressurized offshore modules, platforms and marine vessels."),
    ("Preventive Maintenance Programmes", "AMC and PPM plans that extend equipment life and cut breakdowns."),
    ("Rapid Emergency Response", "Fast fault diagnosis and repair when every hour of downtime counts."),
    ("Safety-Driven Operations", "ISO 45001:2018 certified health & safety management on every site."),
    ("Tailored Engineering Solutions", "Phased works, temporary cooling and custom designs around how you operate."),
]

INNOVATION = [
    ("monitor", "Remote Monitoring", "Live visibility of plant status, temperatures and alarms."),
    ("chart", "Predictive Maintenance", "Trend data to catch faults before they become breakdowns."),
    ("bolt", "Energy Optimization", "Tuning plant operation to cut energy use without losing capacity."),
    ("smart", "Smart Building Solutions", "Integrated controls that make buildings easier to run."),
]

# ---------------------------------------------------------------- featured engineering projects
PROJECTS = [
    dict(
        id="cold-storage", n="01", img="cold-storage",
        title="Cold Storage Refrigeration System Modernization for a Large Hospitality Facility",
        short="Phased replacement of six freezer room systems with zero product loss — stable at −22 °C.",
        client="Leading Hospitality & Food Service Group, Qatar", industry="Hospitality & Commercial Refrigeration",
        kpis=[("−22 °C", "Stable freezer temp."), ("0", "Product loss"), ("20 days", "Programme")],
        overview="Q Ventus was appointed to modernize the refrigeration infrastructure of a large commercial food storage facility supporting multiple hospitality outlets. The existing freezer rooms had become increasingly unreliable due to ageing refrigeration equipment, resulting in unstable storage temperatures and increasing the risk of product loss. The objective was to engineer a long-term refrigeration solution that would restore system reliability while ensuring uninterrupted operation of the client's food supply chain throughout the project.",
        challenge=("The facility consisted of multiple commercial freezer rooms operating continuously. An engineering assessment identified several critical issues:", [
            "Ageing 3 HP condensing units operating beyond their reliable service life.",
            "Declining refrigeration capacity causing unstable freezer temperatures.",
            "Temperature fluctuations compromising food storage conditions.",
            "Damaged insulated freezer doors from failed anti-condensation door heater systems.",
            "Faulty pressure relief valves affecting door operation and chamber pressure equalization.",
            "Growing risk of refrigeration failure during peak operating periods.",
        ], "Prolonged shutdowns were not acceptable due to continuous food storage requirements."),
        solution=("Following a detailed site survey and system evaluation, Q Ventus developed a phased replacement strategy to eliminate operational downtime:", [
            "Replacement of six 3 HP commercial condensing units.",
            "Installation of six new evaporator units across the North and South freezer facilities.",
            "Refrigerant piping modifications and system integration.",
            "Repair and restoration of damaged insulated freezer doors.",
            "Replacement and calibration of electric door heater systems.",
            "Repair and servicing of pressure relief valves.",
            "System testing, balancing and commissioning.",
        ], "The first two systems were commissioned within three days. During each phase, temporary refrigerated (reefer) units were provided on rental, maintaining cold chain integrity throughout the 20-day programme."),
        results=("All freezer rooms consistently maintained −22 °C after commissioning:", [
            "Stable freezer temperatures at −22 °C.",
            "Zero product loss throughout the project.",
            "Continuous operations via temporary refrigerated backup.",
            "Increased reliability and reduced breakdown frequency.",
            "Improved efficiency, cooling performance and equipment life.",
            "Reduced maintenance requirements.",
        ]),
        value="Through detailed planning, staged execution and refrigeration expertise, Q Ventus modernized a mission-critical refrigeration facility without interrupting daily operations — where operational continuity mattered as much as engineering excellence.",
    ),
    dict(
        id="chiller-plant-hotel", n="02", img="commercial-rooftop-plant",
        title="Chiller Plant Modernization for a Luxury Hospitality Property",
        short="York to Trane air-cooled chiller replacement support, followed by an AMC award for the new plant.",
        client="International Hotel Group", industry="Hospitality · Chiller Plant",
        kpis=[("York → Trane", "Chiller replacement"), ("AMC", "Awarded post-handover")],
        overview="As part of a comprehensive HVAC modernization program, the client initiated the replacement of aging air-cooled chillers to improve cooling performance, operational efficiency and long-term reliability across the hotel. Q Ventus was engaged to support the chiller replacement program and provide ongoing preventive maintenance after completion.",
        challenge=("The existing air-cooled chiller plant had reached the later stages of its lifecycle. The client required:", [
            "Improved cooling reliability.",
            "Increased energy efficiency.",
            "Reduced maintenance costs.",
            "Minimal disruption to hotel operations during replacement.",
            "Long-term technical support after installation.",
        ], "Maintaining uninterrupted guest comfort throughout the project was a critical requirement."),
        solution=("Q Ventus participated in replacing the existing York air-cooled chillers with new Trane air-cooled chillers. The scope included:", [
            "Decommissioning support for existing chillers.",
            "Mechanical and HVAC coordination during replacement.",
            "System commissioning assistance.",
            "Operational testing and performance verification.",
            "Preventive maintenance planning.",
        ], "Following successful commissioning, Q Ventus was awarded the Annual Maintenance Contract (AMC) for the new chiller plant."),
        results=("The completed project delivered:", [
            "Improved cooling reliability.",
            "Higher plant efficiency.",
            "Reduced breakdown frequency.",
            "Optimized preventive maintenance scheduling.",
            "Long-term operational support through the AMC program.",
        ]),
        value="The client continues to benefit from planned maintenance designed to maximize equipment life while maintaining uninterrupted cooling performance.",
    ),
    dict(
        id="offshore-pressurized", n="03", img="offshore-platform",
        title="Offshore Pressurized HVAC System Engineering Upgrade",
        short="Redesign and upgrade of HVAC for pressurized offshore accommodation and control containers.",
        client="Leading Offshore Drilling Contractor", industry="Oil & Gas · Offshore HVAC",
        kpis=[("Positive", "Pressurization held"), ("↑ Uptime", "Operational")],
        overview="An offshore drilling operation experienced recurring HVAC reliability issues within pressurized accommodation and control containers operating in harsh offshore conditions. Given the mission-critical nature of the facility, any HVAC failure could impact operational continuity and personnel safety. Q Ventus was appointed to engineer a permanent upgrade.",
        challenge=("The existing system could no longer consistently maintain required conditions inside the pressurized containers:", [
            "Frequent equipment failures.",
            "Reduced cooling capacity.",
            "High ambient operating temperatures.",
            "Continuous operation under demanding offshore conditions.",
            "Need to maintain positive pressurization.",
            "Risk of operational downtime.",
        ], None),
        solution=("Following a comprehensive engineering evaluation, Q Ventus redesigned and upgraded the system:", [
            "Detailed HVAC engineering assessment.",
            "System redesign for offshore operating conditions.",
            "Upgraded air conditioning equipment.",
            "Improved airflow distribution.",
            "Optimization of cooling performance.",
            "Mechanical modifications where required.",
            "Full commissioning and performance testing.",
        ], "All work was carried out while meeting the operational requirements of the offshore facility."),
        results=("The upgraded system significantly improved operational reliability:", [
            "Elimination of recurring cooling failures.",
            "Stable conditions inside pressurized containers.",
            "Reduced maintenance interventions.",
            "Improved equipment reliability and uptime.",
            "Enhanced support for continuous drilling operations.",
        ]),
        value="The engineered upgrade gave the client a dependable HVAC solution capable of supporting critical offshore operations in demanding marine environments.",
    ),
    dict(
        id="superyacht-retrofit", n="04", img="marine-yacht",
        title="Complete Marine HVAC Retrofit for a 121-Foot Luxury Superyacht",
        short="Four new 105,000 BTU Dometic chillers, full AHU replacement and dual-station monitoring.",
        client="Private Luxury Yacht Owner, Qatar", industry="Marine HVAC Engineering",
        kpis=[("121 ft", "Superyacht"), ("4 × 105k", "BTU chillers"), ("2", "Monitoring stations")],
        overview="Q Ventus was appointed to modernize the air conditioning system aboard a 121-foot luxury superyacht. The existing chilled water HVAC system had become unreliable due to ageing equipment, reduced capacity and declining efficiency. The objective was a modern, high-performance marine HVAC solution with improved efficiency, monitoring and long-term reliability.",
        challenge=("Marine HVAC faces continuous vibration, high humidity, corrosive salt air and confined machinery spaces. The existing system suffered from:", [
            "Aging water-cooled chillers operating below design performance.",
            "Reduced cooling capacity in peak ambient conditions.",
            "Increased maintenance requirements.",
            "Limited system monitoring.",
            "Declining reliability affecting comfort throughout the vessel.",
        ], "The upgrade had to improve performance without compromising the vessel's integrity or luxury standards."),
        solution=("Q Ventus designed and executed a complete retrofit tailored to the vessel's chilled water distribution network:", [
            "Removal of four existing water-cooled marine chillers.",
            "Installation of four new 105,000 BTU Dometic water-cooled chillers in the engine room.",
            "Integration into the vessel's chilled water circuit.",
            "Complete replacement of all marine AHUs with modern Dometic units.",
            "Dual monitoring and control system with stations in the engine room and on the bridge.",
            "System balancing, commissioning and full performance testing.",
        ], None),
        results=("The upgraded system delivered a significant improvement in performance and control:", [
            "Complete modernization of the chilled water HVAC plant.",
            "Increased cooling capacity throughout the yacht.",
            "Improved guest and crew comfort.",
            "Enhanced reliability and reduced maintenance.",
            "Dual-location monitoring for better oversight.",
            "Improved serviceability and efficiency.",
        ]),
        value="This project demonstrates Q Ventus' capability to engineer complex marine HVAC retrofits involving chilled water systems, advanced controls and precision installation within the constraints of a luxury vessel.",
    ),
    dict(
        id="fifa-2022", n="05", img="exhibition-hall",
        title="Temporary HVAC Infrastructure for FIFA World Cup Qatar 2022",
        short="~50 engineers and technicians across stadiums, fan zone and broadcast facilities — install to decommission.",
        client="International Event Infrastructure Contractor", industry="Major Events & Temporary Infrastructure",
        kpis=[("~50", "Engineers & technicians"), ("24 h", "Operational monitoring"), ("6+", "Venues & facilities")],
        venues=["Al Bayt Stadium", "Lusail Stadium", "Education City Stadium", "FIFA Fan Zone – Al Bidda Park", "International Broadcast Facilities (FOX Sports)", "Temporary Hospitality & Leisure Facilities"],
        overview="Q Ventus was selected to support one of the world's largest sporting events, providing complete HVAC installation, commissioning, operational support and decommissioning for multiple temporary facilities across several tournament venues — supporting visitors, event personnel, broadcast teams and operational staff.",
        challenge=("Temporary event infrastructure must be designed, installed, commissioned, operated and removed within extremely tight schedules. The project demanded:", [
            "Rapid mobilisation across multiple venues.",
            "Continuous cooling reliability throughout the tournament.",
            "Immediate emergency response to equipment failures.",
            "Coordination between multiple contractors and stakeholders.",
            "Installation in temporary structures exposed to harsh outdoor conditions.",
            "Zero disruption to event operations.",
        ], "With millions of spectators and global television coverage, equipment reliability was mission-critical."),
        solution=("Q Ventus deployed approximately 50 HVAC engineers and technicians across all phases:", [
            "Mobile water-cooled chiller systems.",
            "25 TR Air Handling Units, 15 TR packaged units and 10 TR floor-standing split systems.",
            "Flexible disposable ducting for temporary air distribution.",
            "Electrical and mechanical integration, airflow balancing and commissioning.",
            "24-hour monitoring, preventive maintenance and emergency breakdown response.",
            "Standby engineering teams across multiple venues.",
            "Full post-event decommissioning, duct removal, site restoration and equipment recovery.",
        ], None),
        results=("One of the region's largest temporary HVAC support operations:", [
            "Successful deployment across multiple tournament venues.",
            "Continuous HVAC operation throughout the event.",
            "Rapid response to operational breakdowns.",
            "Reliable climate control for hospitality, broadcast and operational facilities.",
            "Safe execution and successful decommissioning.",
            "Zero disruption to scheduled event operations within Q Ventus' scope.",
        ]),
        value="Delivering HVAC for an international sporting event demands planning, logistics, rapid mobilisation, continuous monitoring and immediate technical response. Q Ventus managed every phase across multiple iconic venues.",
    ),
]
