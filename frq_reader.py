import struct

filename = raw_input("Enter file name:\n")

with open(filename, 'rb') as f:
    # Header.
    header_text = f.read(8).decode('utf-8')
    print header_text
    
    # Samples per frq value.  Should always be 256.
    samples_per_frq = struct.unpack("<i", f.read(4))
    print "Samples per frq:", samples_per_frq[0]
    
    # Average frequency.
    avg_frq = struct.unpack("<d", f.read(8))
    print "Average frq:", avg_frq[0]
    
    # Empty space.
    f.read(16)
    
    # Number of chunks.
    num_chunks_bytes = f.read(4)
    num_chunks = struct.unpack("<i", num_chunks_bytes)
    print "Number of chunks:", num_chunks[0]
    
    print "\nFrequency | Amplitude"
    for chunk in range(num_chunks[0]):
    	frequency = struct.unpack("<d", f.read(8))
    	amplitude = struct.unpack("<d", f.read(8))
    	print frequency[0], "|", amplitude[0]
    	
    print "Successfully parsed frq file!"
    	
    
    
