import pytest
from TicketMaster import VenueFinder

def test_printed_results_has_venues_only_in_highestpop():
    api_key = 'secret'
    maps_api_key ="secret"
    artist_name = 'shakira'  
    
    venue_finder = VenueFinder(api_key, maps_api_key)  
    expected_output = """Finding venues for shakira ...
Venues in the highest popularity country:
Venue: The East Room, Location: 2503 Gallatin Pike, Nashville, TN 37216, USA
Venue: High Noon Saloon, Location: 701 E Washington Ave, Madison, WI 53703, USA

Venues not in the highest popularity country:"""
    actual_output = venue_finder.find_artist_venues(artist_name)
    assert expected_output == actual_output.strip()

def test_printed_results_has_no_venues_exception():
    api_key = 'secret'
    maps_api_key ="secret"
    artist_name = 'Future'  
    
    venue_finder = VenueFinder(api_key, maps_api_key)  
    expected_output = """Finding venues for Future ...
No events found for Future
Venues in the highest popularity country:

Venues not in the highest popularity country:"""
    actual_output = venue_finder.find_artist_venues(artist_name)
    assert expected_output == actual_output.strip()

def test_printed_results_has_no_venues():
    api_key = 'secret'
    maps_api_key ="secret"
    artist_name = 'cardi b'  
    
    venue_finder = VenueFinder(api_key, maps_api_key)  
    expected_output = """Finding venues for cardi b ...
No events found for cardi b
Venues in the highest popularity country:

Venues not in the highest popularity country:"""
    actual_output = venue_finder.find_artist_venues(artist_name)
    assert expected_output == actual_output.strip()

def test_printed_results_has_venues_only_in_both_FAIL():
    api_key = 'secret'
    maps_api_key ="secret"
    artist_name = 'Xavi'  
    
    venue_finder = VenueFinder(api_key, maps_api_key)  
    expected_output = """Finding venues for Xavi ...
Venues in the highest popularity country:
Venue: Roxy Theatre-CA, Location: 1242 Sunset Plaza Dr, Los Angeles, CA 90069, USA
Venue: The Novo by Microsoft, Location: 524 W Pico Blvd, Los Angeles, CA 90015, USA
Venue: Showbox SODO, Location: 2907 3rd Ave S, Seattle, WA 98134, USA
Venue: Roseland Theater, Location: 1303 NW Lovejoy St, Portland, OR 97209, USA
Venue: Knitting Factory - Boise, Location: 414 S 9th St, Boise, ID 83702, USA
Venue: Ruth Finley Person Theater- Luther Burbank Center, Location: 4032 Coffey Ln, Santa Rosa, CA 95403, USA
Venue: The Catalyst-CA, Location: 2VRG+F9 Bonny Doon, CA, USA
Venue: Fremont Theater, Location: 1166 Higuera St, San Luis Obispo, CA 93401, USA
Venue: Riverside Municipal Auditorium, Location: 473 Mission Inn Avenue, Riverside, CA 92501, USA
Venue: The Observatory, Location: 3503 S Harbor Blvd, Santa Ana, CA 92704, USA
Venue: The Observatory, Location: 3503 S Harbor Blvd, Santa Ana, CA 92704, USA
Venue: The Observatory North Park, Location: 2891-99 University Ave, San Diego, CA 92104, USA
Venue: Bakersfield Fox Theater, Location: 1614 27th St, Bakersfield, CA 93301, USA
Venue: House of Blues Las Vegas , Location: 3950 S Las Vegas Blvd, Las Vegas, NV 89119, USA
Venue: The Union, Location: 235 W 500 N, Salt Lake City, UT 84103, USA
Venue: The Van Buren, Location: 405 W Van Buren St, Phoenix, AZ 85003, USA
Venue: Rialto Theatre-Tucson, Location: 320 E Congress St, Tucson, AZ 85701, USA
Venue: The Hacienda Event Center, Location: 10211 W County Rd 54, Midland, TX 79707, USA
Venue: The Plaza Theatre Performing Arts Center, Location: 114 W Mills Ave, El Paso, TX 79901, USA
Venue: Tower Theatre - Oklahoma City, Location: 326 NW 20th St, Oklahoma City, OK 73103, USA
Venue: House of Blues Dallas , Location: 2401 N Houston St, Dallas, TX 75219, USA
Venue: House of Blues Houston, Location: 1209 Caroline St, Houston, TX 77002, USA
Venue: Aztec Theatre , Location: 280 W Crockett St, San Antonio, TX 78205, USA
Venue: Grant Park, Location: 309 E Balbo Dr, Chicago, IL 60605, USA
Venue: Huntington Bank Pavilion at Northerly Island, Location: 1300 S Linn White Dr, Chicago, IL 60605, USA

Venues not in the highest popularity country:
Venue: Baja Beach, Location: Independencia 2027, Independencia, 22055 Tijuana, B.C., Mexico"""
    actual_output = venue_finder.find_artist_venues(artist_name)
    assert expected_output == actual_output.strip()

def test_printed_results_has_venues_only_in_both():
    api_key = 'v91P8cOBflgRpdlSf0AaB7hiozzrPZkD'
    maps_api_key ="AIzaSyCI74dgOWzxGn2uUiLQ20InRdUSfKsvVNA"
    artist_name = 'Xavi'  
    
    venue_finder = VenueFinder(api_key, maps_api_key)  
    expected_output = """Finding venues for Xavi ...
Venues in the highest popularity country:
Venue: Roxy Theatre-CA, Location: 1242 Sunset Plaza Dr, Los Angeles, CA 90069, USA
Venue: The Novo by Microsoft, Location: 524 W Pico Blvd, Los Angeles, CA 90015, USA
Venue: Showbox SODO, Location: 2907 3rd Ave S, Seattle, WA 98134, USA
Venue: Roseland Theater, Location: 1303 NW Lovejoy St, Portland, OR 97209, USA
Venue: Knitting Factory - Boise, Location: 414 S 9th St, Boise, ID 83702, USA
Venue: Arcata Theater Lounge, Location: 2524 Idylbear Ln, Arcata, CA 95521, USA
Venue: Ruth Finley Person Theater- Luther Burbank Center, Location: 4032 Coffey Ln, Santa Rosa, CA 95403, USA
Venue: The Catalyst-CA, Location: 2VRG+F9 Bonny Doon, CA, USA
Venue: Fremont Theater, Location: 1166 Higuera St, San Luis Obispo, CA 93401, USA
Venue: Riverside Municipal Auditorium, Location: 473 Mission Inn Avenue, Riverside, CA 92501, USA
Venue: The Observatory, Location: 3503 S Harbor Blvd, Santa Ana, CA 92704, USA
Venue: The Observatory, Location: 3503 S Harbor Blvd, Santa Ana, CA 92704, USA
Venue: The Observatory North Park, Location: 2891-99 University Ave, San Diego, CA 92104, USA
Venue: Bakersfield Fox Theater, Location: 1614 27th St, Bakersfield, CA 93301, USA
Venue: House of Blues Las Vegas , Location: 3950 S Las Vegas Blvd, Las Vegas, NV 89119, USA
Venue: The Union, Location: 235 W 500 N, Salt Lake City, UT 84103, USA
Venue: The Van Buren, Location: 405 W Van Buren St, Phoenix, AZ 85003, USA
Venue: Rialto Theatre-Tucson, Location: 320 E Congress St, Tucson, AZ 85701, USA
Venue: The Hacienda Event Center, Location: 10211 W County Rd 54, Midland, TX 79707, USA
Venue: The Plaza Theatre Performing Arts Center, Location: 114 W Mills Ave, El Paso, TX 79901, USA
Venue: Tower Theatre - Oklahoma City, Location: 326 NW 20th St, Oklahoma City, OK 73103, USA
Venue: House of Blues Dallas , Location: 2401 N Houston St, Dallas, TX 75219, USA
Venue: House of Blues Houston, Location: 1209 Caroline St, Houston, TX 77002, USA
Venue: Aztec Theatre , Location: 280 W Crockett St, San Antonio, TX 78205, USA
Venue: Grant Park, Location: 309 E Balbo Dr, Chicago, IL 60605, USA
Venue: Huntington Bank Pavilion at Northerly Island, Location: 1300 S Linn White Dr, Chicago, IL 60605, USA

Venues not in the highest popularity country:
Venue: Baja Beach, Location: Independencia 2027, Independencia, 22055 Tijuana, B.C., Mexico"""
    actual_output = venue_finder.find_artist_venues(artist_name)
    assert expected_output == actual_output.strip()
