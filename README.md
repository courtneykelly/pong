# Pong Networking Project

## Summary

Create a multiplayer game that allows a minimum of two players to compete (or cooperate!)
via a network connection. The network architecture may be direct (peer-to-peer), or may use a server. You
must use the PyGame and Twisted libraries. 

We decided to recreate the two-player Pong game over a network connection.

## Learning objectives

What you’re really practicing here is the clock-tick design paradigm. Clock-tick is a very popular way of
handling programs that have mixed automated and interactive elements. It is also useful in programs where
many semi-autonomous components need to be synchronized to some degree of precision, as in distributed
sensor networks or control systems.

You are also practicing collaborative software development. Very few programs are commercially
developed by only one person. Software companies place a high value on team courtesy and knowledge of
the division of labor. Oftentimes, the hard work comes during integration, when software components
written by different persons are stitched together into a final product. 
