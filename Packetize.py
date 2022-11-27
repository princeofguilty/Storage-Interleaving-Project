from packets import packet

PACKET_SIZE = 32

def packetize(data):
    cursor = 0
    list_of_packets = []
    while cursor < len(data):
        new_packet = packet()
        new_packet.set_data(data[cursor:cursor+PACKET_SIZE])
        list_of_packets.append(new_packet)
        cursor += PACKET_SIZE
    
    # if(cursor < len(data)):


    return list_of_packets