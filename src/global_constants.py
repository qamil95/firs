# changing the order of items in econmy list breaks savegames, don't do it.
economies = ["FIRS", "BASIC_TEMPERATE", "BASIC_ARCTIC", "BASIC_TROPIC", "MISTAH_KURTZ"]

# stuff for configuring supply boost behaviour (relying on list positions is evil, but I want to get this done).
supply_requirements = {'ENSP': [21, 84, 'PRIMARY'], 'FMSP': [14, 56, 'PRIMARY'], 'import_export': [56, 224, 'PORT']}

# Definition of the IDs of the single industries
industry_numeric_ids = dict(coal_mine = 0x00,
                            lime_kiln = 0x01,
                            metal_fabrication_plant = 0x02,
                            sugar_plantation = 0x03,
                            iron_ore_mine = 0x04,
                            bauxite_mine = 0x05,
                            smithy_forge = 0x06,
                            steel_mill = 0x07,
                            aluminium_plant = 0x08,
                            metal_workshop = 0x09,
                            quarry = 0x0A,
                            forest = 0x0B,
                            sawmill = 0x0C,
                            furniture_factory = 0x0D,
                            paper_mill = 0x0E,
                            oil_wells = 0x0F,
                            oil_rig = 0x10,
                            oil_refinery = 0x11,
                            plastics_plant = 0x12,
                            sugar_refinery = 0x13,
                            dredging_site = 0x14,
                            iron_works = 0x15,
                            glass_works = 0x16,
                            recycling_plant = 0x17,
                            recycling_depot = 0x18,
                            junk_yard = 0x19,
                            arable_farm = 0x1A,
                            sheep_farm = 0x1B,
                            dairy_farm = 0x1C,
                            mixed_farm = 0x1D,
                            fruit_plantation = 0x1E,
                            fishing_harbour = 0x1F,
                            fishing_grounds = 0x20,
                            basic_farm = 0x21,
                            grain_mill = 0x22,
                            brewery = 0x23,
                            dairy = 0x24,
                            stockyard = 0x25,
                            machine_shop = 0x26,
                            port = 0x27,
                            fertiliser_plant = 0x28,
                            lumber_yard = 0x29,
                            textile_mill = 0x2A,
                            cement_plant = 0x2B,
                            clay_pit = 0x2C,
                            brick_works = 0x2D,
                            biorefinery = 0x2E,
                            orchard_piggery = 0x2F,
                            ranch = 0x30,
                            copper_mine = 0x31,
                            coffee_estate = 0x32,
                            bulk_terminal = 0x33,
                            trading_post = 0x34,
                            rubber_plantation = 0x35,
                            fibre_crop_farm = 0x36,
                            diamond_mine = 0x37,
                            food_processor = 0x38,
                            hardware_store = 0x39,
                            hotel = 0x3A,
                            food_market = 0x3B,
                            petrol_pump = 0x3C,
                            general_store = 0x3D,
                            #IND_VACANT_ID = 0x3E,
                            builders_yard = 0x3F)
#3F is last ID to be used (64 industry limit)

chameleon_cache_dir = 'chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = 'generated'

# this is for nml or grfcodec, don't need to use python path module here
graphics_path = 'generated/graphics/'

openttd_climates = ["CLIMATE_TEMPERATE", "CLIMATE_ARCTIC", "CLIMATE_TROPIC", "CLIMATE_TOYLAND"]
