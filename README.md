# Decentralized-Storage-Network
A Decentralized Cloud Storage based on Erasure coding.
### INTRO
This project is a Python implementation of a Decentralized Network for file storage with less storage overhead than replication of data across nodes for same durability, using Cauchy Matrix and Field Theory.

In general, replicated-type system, takes a data piece and distribute it over to multiple nodes for durability. In contrast, erasure coding uses different approach. In erasure coding on Reed-Solomon encoding, data is broken into fragments of two kinds : data block and parity block. If drive fails or gets corrupted, parity blocks are used to rebuild data.

### ALGO
Three elements are - Satellite, Data Nodes and Client.

Encoding: Client will go to satellite with request to store the data, in return Satellite will send an n,k coding matrix exploting properties of Cauchy Matrix, and Prime Field Theory and a list of n active nodes. Then on client side, file would be broken into k chunks and encoded in n chunks and send to the nodes from satellite.
Repair and Monitoring: Satellite will ping the nodes after a interval to check whether they are active, if more than a threshold(2k/3) nodes are shut, it'll call for repair over some node, consolidate the data, encode again and send the regenerated lost pieces to new nodes, modify the routing table and send it to the client.
Decoding: Client will look upon roting table and contact top n nodes, the data nodes will respond with the packets, and decode with coding matrix.
