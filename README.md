# Saint George's interactive story:
## The Whatsapp bot that become viral on 23 April (27.325 users)

<p align="center">
 <img src="https://github.com/enric1994/santjordi/blob/master/images/SJB1-01.png" width="500">
</p>

In Catalonia (Spain), Saint Gerorge's day is one of the most original celebrations, book and flower stalls are set up along the streets of Barcelona 🌹📚

So I created a **gamechat** that explains the Saint George's story from the point of view of one the characters (🐮👸🏼🤴👑👨‍🌾🐲), in order to advance the users have to interact with other participants and find the next character that unlock his story. 

Let's see an example:

(Note that all the texts are in Catalan)

<p align="center">
 <img src="https://github.com/enric1994/santjordi/blob/master/images/sj1.jpg" width="300">
</p>

As you can see, to start the history you must start a conversation with the bot and text the keyword: **conte**.

Then, the bot explain the introduction of the story and assigns you a character (in this case the princess 👸🏼). To continue, the user need to find another participant with the king 👑 character and attach the contact:

<p align="center">
 <img src="https://github.com/enric1994/santjordi/blob/master/images/sj2.jpg" width="300">
</p>

Finally, to end the story, the princess must find the dragon 🐲

<p align="center">
 <img src="https://github.com/enric1994/santjordi/blob/master/images/sj3.jpg" width="300">
</p>

## Results
* **27.375** users started at least one story
* 133.707 messages and contacts processed by the chatbot during the event
* 2797 users complete the story as the cow 🐮 
* 3571 users complete the story as the 👸🏼
* 3196 users complete the story as the knight 🤴 
* 3281 users complete the story as the king 👑
* 2918 users complete the story as the farmer 👨‍🌾 
* 2067 users complete the story as the dragon 🐲 

## Infrastructure
I developed the Whatsapp bot using the following elements:
* A laptop with [this Python Whatsapp Web wrapper](https://github.com/mukulhase/WebWhatsapp-Wrapper)
* A mobile phone with Whatsapp installed (and a secondary telephone line)
* A MySQL database using Docker

## Issues during the event
I noticed several **scalability** problems when handling requests from more than 10k users.
The first hours the new users income where 2/hour (basically my family and friends), then it started growing exponentially until **1000 new users per hour**. 

At this point the system collapsed and the response time raised to 5 minutes in some cases, that delay stopped the exponentially growing curve :(

## Acknowledgements
I would like to thank my family and friends who trusted in my idea and forward the Whatsapp bot contact.
