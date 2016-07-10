import struct

v = -200
r = 500

velocity = int(v) & 0xffff
radius = int(r) & 0xffff
bytes = struct.unpack('4B', struct.pack('>2H', velocity, radius))

print 'bytes:'
print bytes
print
print
print 'wat'
bytes = tuple([10,10,10])
opcode = (137,)

data = opcode + bytes
print data
temp = struct.pack('B' * len(data), *data)
print
print
print temp
