# Pong Networking Project

Courtney Kelly && Katie Schermerhorn

## Libraries
There are several different libraries needed in order to compile and run our game. First, you need to be using any version of `python 2`. If you have a later version of python installed and cannot install additional modules to `python2` then we suggest creating a virtual environment. Here is a helpful [article](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) on how to do so. You will also need to install `pygame` and `twisted`. These modules may have additional dependencies you will need to install as well such as `mercial` or `zope.interface`. 

`twisted` can be installed using your favorite package manager (i.e., `anaconda` or `pip`), but `pygame` must be installed using `pip`. If you do not have `pip` installed, please install it. 

**Summary**
* must be run using `Python 2`
* install `pip`
* Python modules
  * `pygame`
  * `twisted`
  * `mercurial`
* Additional (possible) installations
  * `zope.interface`

## How to Run
Running our game is quite simple. Once you have the necessary packages installed, execute the following steps:
1. Player 2 should open the `Address.py` file and enter the IP address of Player 1's computer network. 
2. Both Player 1 and 2 should have the same port number in the `Address.py` file. This value must be >= 9000.
3. Player 1 executes:
```bash
python Host.py
```
4. Player 2 should wait a couple seconds after Player 1 runs `Host.py` to execute:
```bash
python Client.py
```
5. Have fun!

## How to Play
Player 1 uses the paddle on the left and Player 2 uses the paddle on the right.  Both players should use the UP and DOWN arrows on his or her keyboards to control his or her paddle.  In level 1, a Professor McMillan will appear in the middle of the screen.  It will start moving. The goal is to keep the Professor from passing your paddle.  The game continues until one player has a score of 10.  Once this has happened, the second level will start- this time with two Professors.  Once one player receives a score of 10, the third level will start with three Professors.  The overall winner of all three games is announced once the third level is over.  To exit at any time, exit out of the window.
